from pathlib import Path
import shutil
from typing import (
    Optional,
    List,
    Literal,
)
from typeguard import typechecked
from loguru import logger
from IPython.display import display
import pandas as pd
from tidydata.table import Table
from tidydata.schema import SourceSchema
from tidydata.schema import SourceSchema, PipeSchema, ExportSchema, TidyDataSchema
import toml


class TidyData(object):
    """TableManager类"""

    def __getitem__(self, key):
        return self.cache[key]

    @typechecked
    def __setitem__(self, key: str, value: Table):
        self.cache[key] = value

    @typechecked
    def __setitem__(self, key: str, value: Table):
        self.cache[key] = value

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.cache.close()
        shutil.rmtree(self.cache_dir)

    @classmethod
    def from_toml(cls, path: Path | str):
        tidydata = toml.load(path).get("tidydata")
        if tidydata is None:
            raise ValueError(f"Missing key 'tidydata' in file: {path}")
        return cls(**tidydata)

    @typechecked
    def __init__(
        self,
        cache_dir: Path | str = "_cache",
        export_dir: str | Path = "_export",
        log_file: bool = False,
        log_level: Literal[
            "TRACE", "DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"
        ] = "INFO",
        log_format: str = "<green>{time:YYYY-MM-DD HH:mm:ss} {level}</green>: {message}",
        source: Optional[Path | str] = None,
        pipe: Optional[Path | str] = None,
        export: Optional[Path | str] = None,
        keep_cache: bool = True,
        **kwargs,
    ):
        tidydata_schema = TidyDataSchema(
            cache_dir=cache_dir,
            export_dir=export_dir,
            log_file=log_file,
            log_format=log_format,
            log_level=log_level,
            source=source,
            pipe=pipe,
            export=export,
        )

        self.cache_dir = tidydata_schema.cache_dir
        self.export_dir = tidydata_schema.export_dir
        self.log_file = tidydata_schema.log_file
        self.cache = tidydata_schema._cache

        if tidydata_schema.source is not None:
            self.source(tidydata_schema.source)
        if tidydata_schema.pipe is not None:
            self.pipe(tidydata_schema.pipe)
        if tidydata_schema.export is not None:
            self.export(tidydata_schema.export)

        if not keep_cache:
            self.remove()

    @property
    def tags(self):
        return [self.cache.get(key, tag=True)[1] for key in self.keys]

    @property
    def keys(self):
        return list(self.cache.iterkeys())

    def values(self):
        return (self.cache[k] for k in self.keys)

    def key_to_tag(self):
        return pd.DataFrame({"key": self.keys, "tag": self.tags})

    def disk_usage(self):
        return self.cache.volume()

    def close(self):
        logger.debug(f"Closing disk cache in {self.cache_dir}...")
        self.cache.close()
        logger.debug(f"Closed disk cache in {self.cache_dir}...")

    def remove(self):
        self.close()
        logger.debug(f"Removing cache directory: {self.cache_dir}...")
        shutil.rmtree(self.cache_dir)
        logger.info(f"Removed TidyData cache from directory: '{self.cache_dir}'.")

    def pipe(self, toml_file: Path | str):
        PipeSchema.from_toml(toml_file).to_cache(self.cache)
        logger.success(f"All pipe actions took from toml file: '{toml_file}'.")

    def source(self, toml_file: Path | str):
        SourceSchema.from_toml(toml_file).to_cache(self.cache)
        logger.success(f"All sources added from toml file: '{toml_file}'.")

    def export(self, toml_file: Path | str):
        ExportSchema.from_toml(toml_file).export_from_cache(
            self.cache, export_dir=self.export_dir
        )
        logger.success(
            f"All data (metadata or statistics) exported from toml file: '{toml_file}'."
        )

    def get_keys(
        self,
        keys: Optional[str | List[str]] = None,
        tags: Optional[str | List[str]] = None,
    ):
        query_condition = None

        if keys is not None:
            query_condition = f"key.isin({[keys] if isinstance(keys, str) else keys})"

        if tags is not None:
            if query_condition is None:
                query_condition = (
                    f"tag.isin({[tags] if isinstance(tags, str) else tags})"
                )
            else:
                query_condition = (
                    query_condition
                    + "&"
                    + f"tag.isin({[tags] if isinstance(tags, str) else tags})"
                )

        if query_condition is not None:
            queried_keys = self.key_to_tag().query(query_condition)["key"].to_list()

        else:
            queried_keys = self.keys

        return queried_keys

    def describe(
        self,
        keys: Optional[List[str] | str] = None,
        tags: Optional[List[str] | str] = None,
        destype: Literal["metafile", "summary"] = "summary",
    ):
        for i, key in enumerate(self.get_keys(keys=keys, tags=tags), start=1):
            print(f"\033[32m [{i}] Describe Table with name '{key}': ")
            display(self.cache[key].describe(destype=destype))
