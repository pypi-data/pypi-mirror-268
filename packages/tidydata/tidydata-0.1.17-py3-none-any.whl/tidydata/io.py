from pathlib import Path
from typing import Optional, List, Dict, Literal, Iterable, Any
import pandas as pd
import pyreadstat
from ulid import ULID
from pydantic import BaseModel
from tidydata.dtype import DtypeStr, DtypeMappings

from tidydata.utils import (
    is_default_index,
    infer_stata_bin,
    cast_mix_dtype,
    log_error,
    convert_dtype_backend,
)
from tidydata.table import Table
from loguru import logger

ulid = ULID()

FileSuffixStr = Literal[
    ".csv",
    ".tsv",
    ".parquet",
    ".pq",
    ".dta",
    ".pickle",
    ".pkl",
    ".feather",
    ".fea",
    ".xlsx",
    ".xls",
]

FILE_SUFFIES = [
    ".csv",
    ".tsv",
    ".parquet",
    ".pq",
    ".dta",
    ".pickle",
    ".pkl",
    ".feather",
    ".fea",
    ".xlsx",
    ".xls",
]


def read_dta(
    path: str | Path,
    columns: Optional[List[str]] = None,
    binary: Optional[str | Path] = None,
    version: Literal["mp", "se", "be"] = "mp",
    engine: Literal["pandas", "stata-bin"] = "pandas",
):
    from_file = Path(path)

    if not from_file.suffix == ".dta":
        logger.error(f"Not a DTA file: {path}")

    if engine == "stata-bin":
        import stata_setup

        stata_setup.config((binary or infer_stata_bin()), edition=version, splash=False)
        from pystata import stata

        temp_csv = Path(f"TempFile_{ulid.generate()}.csv")

        stata.run(
            f"use {' '.join(columns) if columns is not None else ''} using {from_file},clear",
            quietly=True,
        )
        stata.run(f"export delimited using {temp_csv}, quote datafmt", quietly=True)
        df = pd.read_csv(temp_csv, columns=columns)
        temp_csv.unlink()
        return df

    else:
        return pd.read_stata(from_file, columns=columns)


def read_csv(
    path: str | Path,
    columns: Optional[List[str]] = None,
    sep: str = ",",
):
    return pd.read_csv(
        path, usecols=columns, sep=sep, engine="pyarrow", dtype_backend="pyarrow"
    )


def read_tsv(
    path: str | Path,
    columns: Optional[List[str]] = None,
):
    return pd.read_csv(
        path, usecols=columns, sep=r"\t", engine="pyarrow", dtype_backend="pyarrow"
    )


def read_parquet(
    path: str | Path,
    columns: Optional[List[str]] = None,
):
    return pd.read_parquet(
        path, columns=columns, engine="pyarrow", dtype_backend="pyarrow"
    )


def read_feather(
    path: str | Path,
    columns: Optional[List[str]] = None,
):
    return pd.read_feather(path, columns=columns, dtype_backend="pyarrow")


def read_pickle(
    path: str | Path,
    columns: Optional[List[str]] = None,
):
    obj = pd.read_pickle(path)

    if not isinstance(obj, pd.DataFrame) and columns is not None:
        log_error(
            f"Value conflict: 'columns' should be None when not a pandas DataFrame object in pickle file:{path}"
        )

    if isinstance(obj, pd.DataFrame) and columns is not None:
        return obj[columns]
    else:
        return obj


def read_excel(
    path: str | Path,
    columns: Optional[List[str]] = None,
    sheet: int | str = 0,
):
    return pd.read_excel(path, usecols=columns, sheet_name=sheet)


class StataReadOption(BaseModel):
    binary: Optional[Path | str] = None
    version: Literal["mp", "se", "be"] = "mp"
    engine: Literal["stata-bin", "pyreadstat", "pandas"] = "pandas"


class ExcelReadOption(BaseModel):
    sheet: int | str = 0


class CSVReadOption(BaseModel):
    sep: str = ","


class PickleReadOption(BaseModel):
    validate_table: bool = False


class ParquetReadOption(BaseModel):
    pass


class FeatherReadOption(BaseModel):
    pass


SUFFIX_TO_READERS = {
    ".csv": (read_csv, CSVReadOption),
    ".tsv": (read_tsv, CSVReadOption),
    ".dta": (read_dta, StataReadOption),
    ".xlsx": (read_excel, ExcelReadOption),
    ".xls": (read_excel, ExcelReadOption),
    ".pickle": (read_pickle, PickleReadOption),
    ".pkl": (read_pickle, PickleReadOption),
    ".parquet": (read_parquet, ParquetReadOption),
    ".pq": (read_parquet, ParquetReadOption),
    ".feather": (read_feather, FeatherReadOption),
    ".fea": (read_feather, FeatherReadOption),
}


def read_file(path: str | Path, columns: Optional[List[str]] = None, **options):
    read_func, read_option = SUFFIX_TO_READERS.get(Path(path).suffix, (None, None))
    if read_func is None:
        log_error(
            f"Unsupported File Type: file's suffix in '{path}' is not in {list(SUFFIX_TO_READERS.keys())}"
        )

    return read_func(path, columns=columns, **(read_option(**options).model_dump()))


# SUFFIX_TO_READERS = {
#     ".csv": read_csv,
#     ".dta": read_dta,
#     ".parquet": read_parquet,
#     ".pq": read_parquet,
#     ".tsv": read_tsv,
#     ".feather": read_feather,
#     ".fea": read_feather,
#     ".pickle": read_pickle,
#     ".pkl": read_pickle,
#     ".xlsx": read_excel,
#     ".xls": read_excel,
# }

# SUFFIX_TO_OPTIONS = {
#     ".csv": "csv",
#     ".dta": "stata",
#     ".parquet": "parquet",
#     ".pq": "parquet",
#     ".tsv": "tsv",
#     ".feather": "feather",
#     ".fea": "feather",
#     ".pickle": "pickle",
#     ".pkl": "pickle",
#     ".xlsx": "excel",
#     ".xls": "excel",
# }


class StataWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"
    var_labels: Optional[Dict[str,str]] = None


class CSVWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"
    sep: str = ","


class TSVWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"
    sep: str = "\t"


class ParquetWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"
    engine: Literal["auto", "pyarrow", "fastparquet"] = "auto"


# Start Here
class ExcelWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"
    sheet: str = "Sheet1"
    engine: Literal["openpyxl", "xlsxwriter"] = None


class FeatherWriteOption(BaseModel):
    index: bool | Literal["auto"] = "auto"


def write_parquet(
    data: pd.DataFrame | Table,
    to_file: Path | str,
    index: bool | Literal["auto"] = "auto",
    engine: Literal["auto", "pyarrow", "fastparquet"] = "auto",
):
    if index == "auto":
        index = False if is_default_index(data.index) else True
    if isinstance(data, Table):
        data.data.to_parquet(to_file, index=index, engine=engine)
    else:
        data.to_parquet(to_file, index=index, engine=engine)


def write_csv(
    data: pd.DataFrame | Table,
    to_file: Path | str,
    index: bool | Literal["auto"] = "auto",
    sep: str = ",",
):
    if index == "auto":
        index = False if is_default_index(data.index) else True

    if isinstance(data, Table):
        data.data.to_csv(to_file, index=index, sep=sep)
    else:
        data.to_csv(to_file, index=index, sep=sep)


def write_excel(
    data: pd.DataFrame | Table,
    to_file: Path | str,
    index: bool | Literal["auto"] = "auto",
    sheet: str = "Sheet1",
    engine: Literal["openpyxl", "xlsxwriter"] = None,
):
    if index == "auto":
        index = False if is_default_index(data.index) else True

    if isinstance(data, Table):
        data.data.to_excel(to_file, index=index, sheet_name=sheet, engine=engine)
    else:
        data.to_excel(to_file, index=index, sheet_name=sheet, engine=engine)


def write_feather(
    data: pd.DataFrame | Table,
    to_file: Path | str,
    index: bool | Literal["auto"] = "auto",
):
    if index == "auto":
        index = False if is_default_index(data.index) else True

    if isinstance(data, Table):
        data.data.to_feather(to_file, index=index)
    else:
        data.to_feather(to_file, index=index)


def write_dta(
    data: pd.DataFrame | Table,
    to_file: Path | str,
    index: bool | Literal["auto"] = "auto",
    var_labels: Optional[Dict[str,str]] = None,
):
    if index == "auto":
        index = False if is_default_index(data.index) else True

    if isinstance(data, Table):
        df = data.data
        data_label = data.description[:80]
        column_labels = data.column_labels.to_dict()
        if var_labels is not None:
            column_labels.update(var_labels)
  
    else:
        df = data
        data_label = None
        column_labels = var_labels

    try:
        df.to_stata(
            to_file,
            data_label=data_label,
            version=118,
            write_index=index,
            variable_labels=column_labels
        )
    except:
        convert_dtype_backend(df, backend="numpy").to_stata(
            to_file,
            data_label=data_label,
            version=118,
            write_index=index,
            variable_labels=column_labels,
        )


SUFFIX_TO_WRITERS = {
    ".parquet": (write_parquet, ParquetWriteOption),
    ".pq": (write_parquet, ParquetWriteOption),
    ".csv": (write_csv, CSVWriteOption),
    ".tsv": (write_csv, TSVWriteOption),
    ".dta": (write_dta, StataWriteOption),
    ".xlsx": (write_excel, ExcelWriteOption),
    ".xls": (write_excel, ExcelWriteOption),
    ".feather": (write_feather, FeatherWriteOption),
    ".fea": (write_feather, FeatherWriteOption),
}


def write_file(data: pd.DataFrame | Table, to_file: str | Path, **options):
    write_func, option_schema = SUFFIX_TO_WRITERS.get(Path(to_file).suffix)

    if write_func is None:
        logger.error(
            f"Unsupported File Type: file's suffix in '{to_file}' is not in {list(SUFFIX_TO_WRITERS.keys())}"
        )

    option = option_schema(**options).model_dump()

    return write_func(data=data, to_file=to_file, **option)


def scan_dir(directory: Path | str, suffies: Optional[Iterable[FileSuffixStr]] = None):
    source_dir = Path(directory)
    if not source_dir.is_dir():
        logger.error(f"Invalid directory: {directory}")

    if suffies is not None:
        return (f for suffix in suffies for f in source_dir.rglob(f"*{suffix}"))
    else:
        return (f for f in source_dir.rglob("*"))


class FileConverter(object):
    """文件转换器"""

    def __init__(
        self,
        source: Path | str | Dict[str, Path | str],
        suffies: List[FileSuffixStr] = None,
        to_dir: str | Path = Path.cwd(),
        quietly: bool = False,
        **options,
    ) -> None:
        self.suffies = FILE_SUFFIES if suffies is None else suffies
        self.source = source
        self.to_dir = Path(to_dir)
        self.options = {} if options is None else options
        self.quietly = quietly

        if isinstance(self.source, dict):
            for key, path in source.items():
                if not Path(path).is_file() or Path(path).suffix not in set(
                    self.suffies
                ):
                    logger.error(
                        f"Invalid file path in key '{key}': {path} does not exists or not with suffies in {self.suffies}"
                    )

        else:
            self.source = {
                f.stem: f
                for suffix in self.suffies
                for f in Path(self.source).rglob(f"*{suffix}")
            }

        if self.to_dir.exists() and not self.to_dir.is_dir():
            logger.error(f"Not a directory in 'to_dir': {to_dir}")

        Path(self.to_dir).mkdir(exist_ok=True)

        if not self.quietly:
            logger.info(
                f"==> Created a FileConverter from source {self.source} to Directory {self.to_dir}"
            )

    def to_parquet(
        self,
        keys: Optional[Dict[str, str] | List[str]] = None,
        to_dir: Optional[Path | str] = None,
        quietly: bool = False,
    ):
        keys = list(self.source.keys()) if keys is None else keys
        parquet_mappings = dict(zip(keys, keys)) if isinstance(keys, list) else keys

        to_dir = Path(to_dir) if to_dir is not None else self.to_dir
        Path(to_dir).mkdir(exist_ok=True)
        for from_key, to_key in parquet_mappings.items():
            to_file = to_dir / f"{to_key}.parquet"
            read_file(self.source[from_key], **self.options).to_parquet(to_file)

            if not quietly:
                logger.info(
                    f"==> Converted '{from_key}' to Parquet file {to_file} in Directory {to_dir}"
                )
