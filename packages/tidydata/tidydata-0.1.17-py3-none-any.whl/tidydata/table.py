from tidydata.base import TableBase
import pandas as pd
import polars as pl
from typing import Optional, List, Literal, Dict, Any, Tuple, Hashable, Iterable
from tidydata.dtype import DtypeStr, DtypeMappings
from tidydata.utils import (
    convert_dtype_backend,
    reshape_frame,
    concat_frames,
    log_error,
    split_frame,
)
from pathlib import Path
import numpy as np
import itertools
import warnings

pd.options.mode.copy_on_write = True
warnings.simplefilter(action="ignore", category=RuntimeWarning)


class Table(TableBase):
    def describe(
        self,
        destype: Literal["metafile", "summary"] = "summary",
    ):
        if destype == "metafile":
            described_df = pd.DataFrame(
                {
                    "Column": self.column_names,
                    "Column_Label": self.column_labels,
                    "Column_Alias": pd.Series(index=self.columns, dtype="string"),
                    "Column_Dtype": self.column_dtypes,
                    "Value_Range": self.column_ranges,
                    "Value_PreFill": pd.Series(index=self.columns, dtype="string"),
                    "Value_PreRepl": pd.Series(index=self.columns, dtype="string"),
                    "Is_Use": pd.Series(data=True, index=self.columns, dtype="bool"),
                }
            ).reset_index(drop=True)

        else:
            described_df = pd.DataFrame(
                {
                    "Column": self.column_names,
                    "Column_Label": self.column_labels,
                    "Column_Dtype": self.column_dtypes,
                    "Value_Range": self.column_ranges,
                    "Value_Missing": self.column_missings,
                }
            ).reset_index(drop=True)

        return self.__class__(
            data=described_df,
            name=f"{destype}_Name:{self.name}",
            tag=f"{destype}_Tag:{self.tag}",
            description=f"{destype}_{self.name}_Description:{self.description}",
            source=f"{destype}_{self.name}_Source:{self.source}",
        )

    def mutate(
        self,
        exprs: List[str],
        repl_dict: Optional[Dict[str, str]] = None,
        engine: Optional[Literal["numexpr", "python"]] = None,
    ):

        NA = pd.NA
        nan = np.nan
        NaT = pd.NaT
        empty = pd.Series(index=self.index,dtype='object')

        import tidydata.pandas_extension

        expr_df = (
            pd.Series(exprs)
            .str.strip()
            .str.split("=", n=1, expand=True)
            .rename(columns={0: "lhs", 1: "rhs"})
            .dropna(how="any")
        )

        if repl_dict is not None:
            expr_df["rhs"] = expr_df["rhs"].replace(repl_dict, "", regex=True)

        expr = expr_df["lhs"].str.cat(expr_df["rhs"], sep="=").str.cat(sep="\n")

        if engine is None:
            try:
                self.data = self.data.eval(expr, engine="numexpr")
            except:
                self.data = self.data.eval(expr, engine="python")
        else:
            self.data = self.data.eval(expr, engine=engine)

        return self

    def reshape(
        self,
        to_shape: Literal["long", "wide"],
        groups: str | List[str] | Dict[str, List[str]],
        i: Optional[str | List[str]] = None,
        j: Optional[str | List[str]] = None,
        sep: str = "_",
        suffix: str = r".*",
        dropna: bool = False
    ):  
        self.data = reshape_frame(
            self.data, to_shape, groups=groups, i=i, j=j, 
            sep=sep, suffix=suffix,dropna=dropna
        )
        
        

        return self

    def concat(
        self,
        others: Iterable["Table"],
        by_axis: Literal["column", "row"],
        on: Optional[List[str]] = None,
        how: Literal["left", "inner", "outer"] = "outer",
        keycol: Optional[Dict[str, int | str]] = None,
    ):

        
        self.data = concat_frames(
            itertools.chain([self.data], (oth.data for oth in others)),
            by_axis,
            on=on,
            how=how,
            keycol=keycol,
        )
        
        return self


    def format(
        self,
        name: Optional[str] = None,
        tag: Optional[str] = None,
        description: Optional[str] = None,
        columns: Optional[List[str] | str] = None,
        rows: Optional[Any] = None,
        column_labels: Optional[Dict[str, str]] = None,
        column_dtypes: Optional[Dict[str, DtypeStr]] = None,
        value_repls: Optional[Dict[str, Dict[Hashable, Any]]] = None,
        value_nafills: Optional[Dict[str, Any]] = None,
        value_ranges: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None,
        dtype_backend: Optional[Literal["numpy", "numpy_nullable", "pyarrow"]] = None,
        drop_duplicates: Optional[List[str] | Literal["all"]] = None,
        column_aliases: Optional[Dict[str, str]] = None,
    ):
        return (
            self.reset_table_name(name)
            .reset_table_tag(tag)
            .reset_table_description(description)
            .select_columns(columns)
            .label_column_names(column_labels)
            .replace_column_values(value_repls)
            .fill_column_missings(value_nafills)
            .convert_column_dtypes(column_dtypes)
            .limit_column_ranges(value_ranges)
            .convert_dtype_backend(dtype_backend)
            .drop_duplicate_values(drop_duplicates)
            .select_rows(rows)
            .alias_column_names(column_aliases)
        )

    def split(
        self,
        by_columns: Optional[str | List[str]] = None,
        by_rows: Optional[int] = None,
    ):
        splited_dfs = split_frame(self.data, by_columns=by_columns, by_rows=by_rows)
        for k, df in splited_dfs:
            yield f"{self.name}_{k}", Table(
                data=df.reset_index(drop=True),
                name=f"{self.name}_{k}",
                tag=f"{self.tag}_{k}",
                description=self.description,
                source=self.source,
            )

    def to_datafile(self, path: Path | str, **options):
        from tidydata.io import write_file

        write_file(data=self, to_file=path, **options)

    def to_metafile(self, path: Path | str, **options):
        from tidydata.io import write_file

        write_file(data=self.describe(destype="metafile"), to_file=path, **options)

    def to_statfile(self, path: Path | str, **options):
        from tidydata.io import write_file

        write_file(data=self.describe(destype="summary"), to_file=path, **options)
