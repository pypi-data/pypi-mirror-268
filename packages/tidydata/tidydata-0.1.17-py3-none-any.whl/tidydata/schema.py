from pydantic import (
    BaseModel,
    model_validator,
    AnyHttpUrl,
)
from typing import (
    Optional,
    Dict,
    List,
    Hashable,
    Tuple,
    Any,
    Literal,
    Callable,
)
from tidydata.dtype import DtypeStr
from pathlib import Path
from tidydata.io import read_file
from loguru import logger
from ast import literal_eval
import toml
import pandas as pd
from tidydata.table import Table
from tidydata.io import SUFFIX_TO_WRITERS
from diskcache import Cache
from tidydata.utils import log_error, get_duplicate_items
from diskcache import Cache
import shutil
import sys


class ColumnMeta(BaseModel):
    columns: Optional[List[str]] = None
    column_labels: Optional[Dict[str, str]] = None
    column_dtypes: Optional[Dict[str, DtypeStr]] = None
    column_aliases: Optional[Dict[str, str]] = None
    value_ranges: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None
    value_repls: Optional[Dict[str, Dict[Hashable, Any]]] = None
    value_nafills: Optional[Dict[str, Any]] = None

    @classmethod
    def from_file(cls, path: Path | str):
        df = (
            pd.read_csv(
                path,
                dtype={
                    "Is_Use": "bool[pyarrow]",
                    "Column": "string[pyarrow]",
                    "Column_Label": "string[pyarrow]",
                    "Column_Dtype": "string[pyarrow]",
                },
            )
            .dropna(subset=["Column"])
            .query("Is_Use==True")
        )

        columns = df["Column"]

        if not columns.is_unique:
            log_error(f"Not unique values in 'Column' from file {path}")
        df.set_index("Column", inplace=True, drop=True)
        columns = columns.to_list()

        # validate column labels
        column_labels = df["Column_Label"]

        if not column_labels.is_unique:
            log_error(f"Not unique values in 'Column_Label' column from file {path}")
        if column_labels.hasnans:
            log_error(f"NA value in 'Column_Label; from file {path}")
        column_labels = column_labels.to_dict()

        # validate column dtypes
        column_dtypes = df["Column_Dtype"]

        if column_dtypes.hasnans:
            logger.error(f"NA value in 'Column_Dtype; from file {path}")
        column_dtypes = column_dtypes.to_dict()

        # validate column aliases
        column_aliases = df.get("Column_Alias")
        if isinstance(column_aliases, pd.Series):
            column_aliases = column_aliases.dropna()
            column_aliases = (
                column_aliases.to_dict() if not column_aliases.empty else None
            )
        # validate value ranges
        value_ranges = df.get("Value_Range")
        if isinstance(value_ranges, pd.Series):
            value_ranges = value_ranges.dropna()
            value_ranges = (
                value_ranges.map(eval).to_dict() if not value_ranges.empty else None
            )

        # validate value prerepls
        value_repls = df.get("Value_PreRepl")
        if isinstance(value_repls, pd.Series):
            value_repls = value_repls.dropna()
            value_repls = (
                value_repls.map(literal_eval).to_dict()
                if not value_repls.empty
                else None
            )

        # validate value prefill
        value_prefills = df.get("Value_PreFill")
        if isinstance(value_prefills, pd.Series):
            value_prefills = value_prefills.dropna()
            value_prefills = (
                value_prefills.to_dict() if not value_prefills.empty else None
            )

        return ColumnMeta(
            columns=columns,
            column_labels=column_labels,
            column_dtypes=column_dtypes,
            column_aliases=column_aliases,
            value_ranges=value_ranges,
            value_repls=value_repls,
            value_nafills=value_prefills,
        )


class SourceData(BaseModel):
    name: str
    description: str
    tag: Optional[str] = None
    datafile: str | Path
    metafile: Optional[str | Path] = None
    docs: Optional[Path | str | AnyHttpUrl] = None
    reader: Dict = {}
    replace: bool = True
    _colmeta: Optional[ColumnMeta] = None

    @model_validator(mode="after")
    def load_colmeta(self):
        self._colmeta = (
            ColumnMeta.from_file(self.metafile)
            if self.metafile is not None
            else ColumnMeta()
        )
        return self

    @model_validator(mode="after")
    def update_tag(self):
        if self.tag is None:
            self.tag = self.name
        return self

    @classmethod
    def from_datafile(cls, source: Path | str):
        return cls(
            name=source.stem,
            datafile=source,
            description=f"Auto-generated table '{source.stem}' from file: {source}",
        )

    def to_cache(self, cache: Cache):
        if not self.replace:
            cached_keys = set(cache.iterkeys())
            if self.name in cached_keys:
                log_error(
                    f"Value in 'name' should not be in cached_keys when 'replace' is False: {self.name}."
                )

        logger.debug(
            f"==> Constructing Table object '{self.name}' with description: {self.description}."
        )

        cache.set(
            key=self.name,
            value=Table.from_file(
                path=self.datafile,
                name=self.name,
                tag=self.tag,
                description=self.description,
                columns=self._colmeta.columns,
                column_labels=self._colmeta.column_labels,
                column_dtypes=self._colmeta.column_dtypes,
                column_aliases=self._colmeta.column_aliases,
                value_repls=self._colmeta.value_repls,
                value_nafills=self._colmeta.value_nafills,
                value_ranges=self._colmeta.value_ranges,
                **self.reader,
            ),
            tag=self.tag,
        )

        logger.debug(
            f"==> Added Table with key '{self.name}' and tag '{self.tag}' to cache {cache.directory}"
        )


class SourceSchema(BaseModel):
    data: List[Dict[str, Any]]

    @model_validator(mode="after")
    def parse_data(self):
        self.data = [SourceData(**dt) for dt in self.data]
        return self

    @model_validator(mode="after")
    def check_duplicate_keys(self):
        logger.debug(f"==> Validating the uniqueness of table names...")
        duplicate_keys = get_duplicate_items((src.name for src in self.data))
        if len(duplicate_keys) > 0:
            log_error(f"Duplicate keys {duplicate_keys} exists in SourceSchema's data")
        logger.debug(f"==> Successfully constructed a SourceSchema object.")
        return self

    @classmethod
    def from_toml(cls, source: Path | str):
        source_path = Path(source)

        if not source_path.is_file() or not source_path.suffix == ".toml":
            log_error(f"Not an existing toml file: {source}")

        logger.debug(f"==>Constructing SourceSchema from toml file: {source}")
        logger.debug(f"==> Getting the key 'source'...")
        source_dict = toml.load(source_path).get("source")
        if source_dict is None:
            log_error(f"Missing key 'source' in toml file: {source}")

        logger.debug(f"==> Getting the the nested key 'data' in 'source'...")
        source_data = source_dict.get("data")
        if source_data is None:
            log_error(f"Missing nest Key 'data' in 'source': {source_data}")
        logger.debug(
            f"==> Checking whether the value of key 'data' in 'source' is a list..."
        )
        if not isinstance(source_data, list):
            log_error(f"Not a List value for 'data': {source_data}")

        return SourceSchema(data=source_data)

    def to_cache(self, cache: Cache):
        for dt in self.data:
            dt.to_cache(cache)
            logger.info(f"Added source: {dt.description} as key '{dt.name}'.")


class ReshapeArgs(BaseModel):
    to_shape: Literal["long", "wide"]
    groups: str | List[str] | Dict[str, List[str]]
    i: Optional[str | List[str]] = None
    j: Optional[str | List[str]] = None
    sep: str = r"@"
    suffix: str = r"\d+"
    dropna: bool = False


class MutateArgs(BaseModel):
    exprs: List[str]
    repl_dict: Optional[Dict[str, str]] = None
    engine: Optional[Literal["numexpr", "python"]] = None


class FormatArgs(BaseModel):
    description: Optional[str] = None
    columns: Optional[List[str] | str] = None
    rows: Optional[Any] = None
    column_labels: Optional[Dict[str, str]] = None
    column_dtypes: Optional[Dict[str, DtypeStr]] = None
    value_repls: Optional[Dict[str, Dict[Hashable, Any]]] = None
    value_nafills: Optional[Dict[str, Any]] = None
    value_ranges: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None
    dtype_backend: Optional[Literal["numpy", "numpy_nullable", "pyarrow"]] = None
    drop_duplicates: Optional[List[str] | Literal["all"]] = None
    column_aliases: Optional[Dict[str, str]] = None


class ConcatArgs(BaseModel):
    others: List[str]
    by_axis: Literal["column", "row"]
    on: Optional[List[str]] = None
    how: Literal["left", "inner", "outer"] = "outer"
    keycol: Optional[Dict[str, List[int | str]]] = None


PIPE_ARG_SCHEMA = {
    "reshape": ReshapeArgs,
    "concat": ConcatArgs,
    "mutate": MutateArgs,
    "format": FormatArgs,
}


class PipeAction(BaseModel):
    description: str
    from_keys: str | List[str]
    to_keys: Optional[str | List[str]] = None
    to_tags: Optional[str | List[str]] = None
    func: Literal["reshape", "concat", "mutate", "format"]
    func_args: Dict = {}
    split_mode: bool = False
    replace: bool = True
    _method: Optional[Callable] = None

    @model_validator(mode="after")
    def validate_keys(self):
        logger.debug(f"Validating pipe action: {self.description} ")
        logger.debug(
            f"==> Validating whether the length of 'from_keys' match with the length of 'to_keys'..."
        )

        if isinstance(self.from_keys, str):
            self.from_keys = [self.from_keys]

        if self.to_keys is None:
            self.to_keys = self.from_keys

        if isinstance(self.to_keys, str):
            self.to_keys = [self.to_keys]

        if len(self.from_keys) != len(self.to_keys):
            log_error(
                f"Length mismatch: 'from_keys' and 'to_keys' should have the same length in a pipe action."
            )

        return self

    @model_validator(mode="after")
    def parse_tags(self):
        logger.debug(f"==> Parsing tags from 'to_tags'...")
        if self.to_tags is None:
            self.to_tags = self.to_keys
        else:
            if isinstance(self.to_tags, str):
                self.to_tags = [self.to_tags] * len(self.to_keys)

            if len(self.to_keys) != len(self.to_tags):
                log_error(
                    f"Length mismatch: 'to_tags' and 'to_keys' should have the same length in a pipe action."
                )
        return self

    @model_validator(mode="after")
    def parse_func_args(self):
        func_schema = PIPE_ARG_SCHEMA[self.func]

        if self.split_mode:
            logger.debug(
                f"==> Parsing 'func_args' as a dict with splited function '{self.func}' schemas..."
            )

            if len(self.func_args) > 0:
                extra_func_arg_keys = set(self.func_args.keys()) - set(self.from_keys)
                if len(extra_func_arg_keys) > 0:
                    log_error(
                        f"Keys in the dict 'func_args' are out of the scope of 'from_keys': {extra_func_arg_keys}."
                    )

            self.func_args = {
                k: func_schema(**v).model_dump() for k, v in self.func_args.items()
            }

        else:
            logger.debug(
                f"==> Parsing 'func_args' as a dict with unified function '{self.func}' schema..."
            )
            self.func_args = {
                k: func_schema(**self.func_args).model_dump() for k in self.from_keys
            }

        logger.debug(
            f"==>Successfully parsed 'func_args' as a dict of function schema: {self.func_args}"
        )

        return self

    @model_validator(mode="after")
    def parse_method(self):
        logger.debug(f"==> Getting method Table from 'func': {self.func}")
        self._method = getattr(Table, self.func)
        return self

    def to_cache(self, cache: Cache):
        cached_keys = set(cache.iterkeys())
        extra_from_keys = set(self.from_keys) - cached_keys

        if len(extra_from_keys) > 0:
            log_error(
                f"values in 'from_keys' are not in cached keys: {extra_from_keys}"
            )

        if not self.replace:
            duplicated_to_keys = set(self.to_keys).intersection(cached_keys)
            if len(duplicated_to_keys) > 0:
                log_error(
                    f"values in 'to_keys' are in cached keys: {duplicated_to_keys}"
                )

        for from_key, to_key, to_tag in zip(self.from_keys, self.to_keys, self.to_tags):
            if self.func == "concat":
                logger.debug(
                    f"==> Updating 'others' in 'func_args' with a Table generator related to its keys..."
                )
                self.func_args[from_key]["others"] = (
                    cache[other_key] for other_key in self.func_args[from_key]["others"]
                )

            logger.debug(
                f"==> Applying pipe action from key '{from_key}' to '{to_key}'..."
            )

            cache.set(
                key=to_key,
                value=self._method(cache[from_key], **self.func_args.get(from_key, {}))
                .reset_table_name(to_key)
                .reset_table_tag(to_tag),
                tag=to_tag,
            )

            logger.debug(f"==> Added piped Table '{to_key}' to cache {cache.directory}")


class PipeSchema(BaseModel):
    actions: List[Dict[str, Any]]

    @model_validator(mode="after")
    def generate_actions(self):
        self.actions = [PipeAction(**ac) for ac in self.actions]
        return self

    @classmethod
    def from_toml(cls, pipe: Path | str):
        pipe_path = Path(pipe)
        if not pipe_path.is_file() or not pipe_path.suffix == ".toml":
            log_error(f"Not an existing toml file: {pipe}")

        logger.debug(f"Constructing PipeSchema from toml file: {pipe}")
        logger.debug(f"==> Getting the key 'pipe'...")
        pipe_dict = toml.load(pipe_path).get("pipe")
        if pipe_dict is None:
            log_error(f"Missing key 'pipe' in toml file: {pipe}")

        logger.debug(f"==> Getting the the nested key 'action' in 'pipe'...")
        pipe_actions = pipe_dict.get("action")
        if pipe_actions is None:
            log_error(f"Missing nest Key 'action' in 'pipe' from file: {pipe}")
        logger.debug(
            f"==> Checking whether the value of key 'action' in 'pipe' is a list..."
        )
        if not isinstance(pipe_actions, list):
            log_error(f"Not a List value for 'action' in 'pipe': {pipe_actions}")

        return PipeSchema(actions=pipe_actions)

    def to_cache(self, cache: Cache):
        for action in self.actions:
            action.to_cache(cache)
            logger.info(
                f"Took pipe action: {action.description} as keys {action.to_keys}."
            )


class ExportData(BaseModel):
    name: str
    description: str
    datafile: bool | Path | str = False
    metafile: bool | Path | str = False
    statfile: bool | Path | str = False
    rows: Optional[str | int | List[str]] = None
    columns: Optional[str | List[str]] = None
    by_columns: Optional[str | List[str]] = None
    by_rows: Optional[int] = None
    writer: Dict[str, Any] = {}
    replace: bool = True

    @model_validator(mode="after")
    def check_file_path(self):
        # Ensure at least one file path
        if (self.datafile, self.metafile, self.statfile) == (False, False, False):
            log_error(
                f"Values of 'datafile', 'metafile' and 'statfile' should not be all False."
            )

        if (self.by_columns or self.by_rows) is not None:
            # Ensure file path is an existing file path when spliting data by columns or by rows
            if isinstance(self.datafile, (str, Path)) and Path(self.datafile).is_file():
                log_error(
                    f"Value in 'datafile' should not be a file path. 'datafile' should be a directory or bool value when 'by_columns' and 'by_rows' are not all None."
                )
            if isinstance(self.metafile, (str, Path)) and Path(self.metafile).is_file():
                log_error(
                    f"Value in 'metafile' should not be a file path. 'metafile' should be a directory or bool value when 'by_columns' and 'by_rows' are not all None."
                )
            if isinstance(self.statfile, (str, Path)) and Path(self.statfile).is_file():
                log_error(
                    f"Value in 'statfile' should not be a file path. 'statfile' should be a directory or bool value when 'by_columns' and 'by_rows' are not all None."
                )

        return self

    def export_from_cache(self, cache: Cache, export_dir: Path | str):
        logger.debug(f"==> Checking main export path: '{export_dir}'...")
        export_dir = Path(export_dir)
        export_dir.mkdir(exist_ok=True)

        logger.debug(f"==> Checking values of 'datafile', 'metafile' and 'statfile'...")

        if self.datafile is True:
            logger.debug(f"==> Setting default datafile path...")
            self.datafile = export_dir / f"datafile-{self.name}.csv"
            logger.debug(f"==> Set default datafile path as '{self.datafile}'.")
        if self.metafile is True:
            logger.debug(f"==> Setting default metafile path...")
            self.metafile = export_dir / f"metafile-{self.name}.csv"
            logger.debug(f"==> Set default metafile path as '{self.metafile}'.")
        if self.statfile is True:
            logger.debug(f"==> Setting default statfile path...")
            self.statfile = export_dir / f"statfile-{self.name}.csv"
            logger.debug(f"==> Set default statfile path as '{self.statfile}'.")

        if not self.replace:
            logger.debug(
                f"==> Checking the conflict whether export file exists when replace is False..."
            )
            if isinstance(self.datafile, Path) and self.datafile.exists():
                log_error(
                    f"Path exists: {self.datafile}. Path of 'datafile' should not exists when 'replace' is False."
                )

            if isinstance(self.metafile, Path) and self.metafile.exists():
                log_error(
                    f"Path exists: {self.metafile}. Path of 'metafile' should not exists when 'replace' is False."
                )
            if isinstance(self.statfile, Path) and self.statfile.exists():
                log_error(
                    f"Path exists: {self.statfile}. Path of 'statfile' should not exists when 'replace' is False."
                )

        logger.debug(
            f"==> Getting Table '{self.name}' from cache and filtering by conditions of columns and rows..."
        )

        table = cache[self.name].select_columns(self.columns).select_rows(self.rows)

        if (self.by_columns or self.by_rows) is not None:
            logger.debug(f"==> Spliting Table '{self.name}' and exporting...")
            for k, tab in table.split(by_columns=self.by_columns, by_rows=self.by_rows):
                if self.datafile is not False:
                    self.datafile.mkdir(exist_ok=True)
                    to_file = self.datafile / f"{k}.parquet"
                    tab.to_datafile(to_file)
                    logger.info(
                        f"Exported splited datafile: {self.description} from key '{self.name}' to '{to_file}'."
                    )

                if self.metafile is not False:
                    self.metafile.mkdir(exist_ok=True)
                    to_file = self.metafile / f"metafile-{k}.csv"
                    tab.to_metafile(to_file)
                    logger.info(
                        f"Exported splited metafile: {self.description} from key '{self.name}' to '{to_file}'."
                    )
                if self.statfile is not False:
                    self.statfile.mkdir(exist_ok=True)
                    to_file = self.statfile / f"statfile-{k}.csv"
                    tab.to_statfile(to_file)
                    logger.info(
                        f"Exported splited statfile: {self.description} from key '{self.name}' to '{to_file}'."
                    )
        else:
            if self.datafile is not False:
                table.to_datafile(self.datafile, **self.writer)
                logger.info(
                    f"Exported datafile: {self.description} from key '{self.name}' to '{self.datafile}'."
                )
            if self.metafile is not False:
                table.to_metafile(self.metafile, **self.writer)
                logger.info(
                    f"Exported metafile: {self.description} from key '{self.name}' to '{self.metafile}'."
                )
            if self.statfile is not False:
                table.to_statfile(self.statfile, **self.writer)
                logger.info(
                    f"Exported statfile: {self.description} from key '{self.name}' to '{self.statfile}'."
                )

        del table


class ExportSchema(BaseModel):
    data: List[Dict]

    @model_validator(mode="after")
    def parse_data(self):
        logger.debug(f"==> Generating the list ExportData objects from 'data'...")
        self.data = [ExportData(**dt) for dt in self.data]

        return self

    def check_duplicate_keys(self):
        logger.debug(f"==> Validating the uniqueness of export file names...")
        duplicate_keys = get_duplicate_items((src.name for src in self.data))
        if len(duplicate_keys) > 0:
            log_error(f"Duplicate keys {duplicate_keys} exists in ExportSchema's data")
        logger.debug(f"==> Successfully constructed a ExportSchema object.")
        return self

    @classmethod
    def from_toml(cls, export: Path | str):
        export_path = Path(export)

        if not export_path.is_file() or not export_path.suffix == ".toml":
            log_error(f"Not an existing toml file: {export}")

        logger.debug(f"==>Constructing ExportSchema from toml file: {export}")
        logger.debug(f"==> Getting the key 'export'...")
        export_dict = toml.load(export_path).get("export")
        if export_dict is None:
            log_error(f"Missing key 'export' in toml file: {export}")

        return ExportSchema(**export_dict)

    def export_from_cache(self, cache: Cache, export_dir: Path | str):
        for dt in self.data:
            dt.export_from_cache(cache=cache, export_dir=export_dir)


class TidyDataSchema(BaseModel):
    cache_dir: Path | str = "_cache"
    export_dir: Path | str = "_export"
    log_file: bool = False
    log_level: Literal[
        "TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"
    ] = "INFO"
    log_format: str = "<green>{time:YYYY-MM-DD HH:mm:ss} {level}</green>: {message}"
    source: Optional[Path | str] = None
    pipe: Optional[Path | str] = None
    export: Optional[Path | str] = None
    keep_cache: bool = True
    _cache: Optional[Cache] = None

    @model_validator(mode="after")
    def parse_dirs(self):
        logger.remove()
        logger.add(
            sys.stdout,
            format=self.log_format,
            level=self.log_level,
            colorize=True,
        )

        self.export_dir = Path(self.export_dir)
        self.export_dir.mkdir(exist_ok=True)
        self.cache_dir = Path(self.cache_dir)

        if self.log_file:
            self.log_file = self.export_dir / f"tidydata-{self.cache_dir.stem}.log"
            logger.add(
                self.log_file,
                format=self.log_format,
                level=self.log_level,
            )

        logger.info(f"Initializing TidyData cache from directory '{self.cache_dir}'...")

        logger.debug(f"==> Validating and connecting cache {self.cache_dir}....")

        if self.cache_dir.exists():
            self._cache = Cache(
                directory=self.cache_dir,
                size_limit=int(shutil.disk_usage(".").free * 0.95),
                cull_limit=0,
                tag_index=True,
            )

            broken_messages = self._cache.check()
            if len(broken_messages) > 0:
                for m in broken_messages:
                    log_error(m.message.__str__())

            for k in self._cache.iterkeys():
                if not isinstance(self._cache[k], Table):
                    log_error(
                        f"Key {k} is not a Table object in cache {self.cache_dir}"
                    )

        else:
            self._cache = Cache(
                directory=self.cache_dir,
                size_limit=int(shutil.disk_usage(".").free * 0.95),
                cull_limit=0,
                tag_index=True,
            )

        logger.info(
            f"Connected cache '{self.cache_dir}' and export directory '{self.export_dir}'."
        )
