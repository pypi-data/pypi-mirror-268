import pandas as pd
from typing import Optional, List, Dict, Literal, Hashable, Any, Tuple
from pathlib import Path
import warnings
import copy
from pandas.api.types import is_string_dtype

import polars as pl

from tidydata.dtype import DtypeMappings, DtypeStr, PANDASDTYPE_TO_ALIAS
from tidydata.utils import (
    is_default_index,
    set_range,
    convert_dtype_backend,
    free_astype,
    free_fillna,
    log_error,
)


warnings.simplefilter(action="ignore", category=FutureWarning)
# pd.options.mode.use_inf_as_na = True
pd.options.mode.copy_on_write = True


class TableBase(object):
    """TableBase类"""

    def _repr_html_(self):
        return self.data._repr_html_()

    def __getitem__(self, key):
        return self.data[key]

    @classmethod
    def from_file(
        cls,
        path: Path | str,
        name: Optional[str] = None,
        tag: Optional[str] = None,
        description: Optional[str] = None,
        columns: Optional[List[str]] = None,
        column_aliases: Optional[Dict[str, str]] = None,
        column_labels: Optional[Dict[str, str]] = None,
        column_dtypes: Optional[Dict[str, DtypeStr]] = None,
        value_repls: Optional[Dict[str, Dict[Hashable, Any]]] = None,
        value_ranges: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None,
        value_nafills: Optional[Dict[str, Any]] = None,
        **options,
    ):
        from tidydata.io import read_file

        source = Path(path)

        obj = read_file(source, columns=columns, **options)

        if isinstance(obj, TableBase):
            data = obj.data
            name = name or obj.name
            tag = tag or obj.tag
            description = description or obj.description
        else:
            data = obj

        return cls(
            data=data,
            source=source,
            name=name,
            tag=tag,
            description=description,
            column_aliases=column_aliases,
            column_labels=column_labels,
            column_dtypes=column_dtypes,
            value_repls=value_repls,
            value_ranges=value_ranges,
            value_nafills=value_nafills,
        )

    def __init__(
        self,
        data: pd.DataFrame | pl.DataFrame | Dict[str, List | pd.Index | pd.Series],
        name: str,
        tag: str,
        description: str,
        source: Path | str,
        columns: Optional[List[str]] = None,
        column_labels: Optional[Dict[str, str]] = None,
        column_dtypes: Optional[Dict[str, DtypeStr]] = None,
        column_aliases: Optional[Dict[str, str]] = None,
        value_repls: Optional[Dict[str, Dict[Hashable, Any]]] = None,
        value_ranges: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None,
        value_nafills: Optional[Dict[str, Any]] = None,
    ) -> None:
        if isinstance(data, pl.DataFrame):
            self.data = (
                data.to_pandas(use_pyarrow_extension_array=True)
                if columns is None
                else data.select(columns).to_pandas(use_pyarrow_extension_array=True)
            )

        else:
            self.data = pd.DataFrame(data, columns=columns)

            if not is_default_index(self.data.index):
                log_error(
                    f"Invalid Index: DataFrame in 'data' is not default range index, please use 'reset_index()' in pandas"
                )
            if isinstance(self.data.columns, pd.MultiIndex):
                log_error(
                    f"Invalid Column names: DataFrame column names in 'data' has multiple index, please flatten it"
                )

            if not is_string_dtype(self.data.columns):
                log_error(
                    f"Invalid Column names: DataFrame column names in 'data' is not string dtype"
                )

        self.name = name
        self.tag = tag
        self.description = description
        self.source = source
        self._column_labels = self.data.columns.to_series()

        (
            self.label_column_names(column_labels)
            .fill_column_missings(value_nafills)
            .replace_column_values(value_repls)
            .convert_column_dtypes(column_dtypes)
            .limit_column_ranges(value_ranges)
            .alias_column_names(column_aliases)
        )

    def copy(self):
        return copy.deepcopy(self)

    @property
    def index(self):
        return self.data.index

    @property
    def size(self):
        return self.data.size

    @property
    def columns(self):
        return self.data.columns

    @property
    def column_labels(self):
        return self._column_labels.reindex(self.columns).combine_first(
            self.column_names
        )

    @property
    def column_names(self):
        return self.data.columns.to_series()

    @property
    def column_dtypes(self):
        return self.data.dtypes.replace(PANDASDTYPE_TO_ALIAS)

    @property
    def column_ranges(self):
        result = {
            series.name: (
                (series.min(), series.max())
                if series.dtype.is_numeric() or series.dtype.is_temporal()
                else dict(enumerate(series.cat.get_categories()))
                if series.dtype == pl.Categorical
                else series.drop_nulls().unique().to_list()
                if series.dtype != pl.Null
                else []
            )
            for series in pl.from_pandas(self.data).iter_columns()
        }

        return pd.Series(result)

    @property
    def column_missings(self):
        return pd.Series(
            pl.from_pandas(self.data).null_count().transpose()["column_0"],
            index=self.data.columns,
        )

    def reset_table_name(self, value: Optional[str] = None):
        if value is not None:
            self.name = value
        return self

    def reset_table_tag(self, value: Optional[str] = None):
        if value is not None:
            self.tag = value
        return self

    def reset_table_description(self, value: Optional[str] = None):
        if value is not None:
            self.description = value
        return self

    def reset_table_source(self, value: Optional[str] = None):
        if value is not None:
            self.source = value

        return self

    def label_column_names(
        self,
        mapping: Optional[Dict[str, str]] = None,
    ):
        if mapping is not None:
            self._column_labels = (
                pd.Series(mapping)
                .reindex(self.data.columns)
                .combine_first(self._column_labels)
            )
        return self

    def replace_column_values(
        self,
        mapping: Optional[Dict[str, Dict[Any, Any]]] = None,
    ):
        if mapping is not None:
            self.data.replace(mapping, inplace=True)
        return self

    def fill_column_missings(
        self,
        mapping: Optional[Dict[str, Any]] = None,
    ):
        if mapping is not None:
            self.data = self.data.transform(
                lambda x: free_fillna(x, mapping.get(x.name)), axis=0
            )
        return self

    def convert_column_dtypes(
        self,
        mapping: Optional[Dict[str, DtypeStr]] = None,
    ):
        if mapping is not None:
            mapping = pd.Series(mapping).replace(DtypeMappings).to_dict()
            self.data = self.data.transform(
                lambda x: free_astype(x, mapping.get(x.name)), axis=0
            )
        return self

    def limit_column_ranges(
        self,
        mapping: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None,
    ):
        if mapping is not None:
            self.data = self.data.apply(
                lambda x: set_range(x, mapping.get(x.name)), axis=0
            )
        return self

    def alias_column_names(
        self,
        mapping: Optional[Dict[str, str]] = None,
    ):
        if mapping is not None:
            self._column_labels.index = self._column_labels.index.map(
                lambda x: mapping.get(x, x)
            )
            self.data.rename(columns=mapping, inplace=True)
        return self

    def select_columns(
        self,
        columns: Optional[List[str] | str] = None,
    ):
        if columns is not None:
            if isinstance(columns, list):
                self.data = self.data[columns]
            else:
                self.data = self.data.filter(regex=columns)
            self._column_labels = self._column_labels.reindex(self.data.columns)
        return self

    def select_rows(
        self,
        rows: Optional[str | int | List[str]] = None,
    ):
        if rows is not None:
            if isinstance(rows, str):
                self.data = self.data.query(rows)
            elif isinstance(rows, list):
                self.data = self.data.query(
                    "&".join([f"({row.strip()})" for row in rows])
                )
            else:
                self.data = self.data.iloc[0:rows]

        return self

    def convert_dtype_backend(
        self,
        value: Optional[Literal["numpy", "numpy_nullable", "pyarrow"]] = None,
    ):
        if value is None:
            return self

        self.data = convert_dtype_backend(self.data)

        return self

    def drop_duplicate_values(
        self, columns: Optional[List[str] | Literal["all"]] = None
    ):
        if columns is None:
            return self

        columns = self.data.columns if columns == "all" else columns

        self.data.drop_duplicates(subset=columns, ignore_index=True, inplace=True)

        return self
