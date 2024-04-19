import pandas as pd
from typing import (
    Optional,
    Tuple,
    List,
    Dict,
    Literal,
    Iterable,
    Any,
    Mapping,
)
from typeguard import typechecked
import platform
from pandas.api.types import is_string_dtype, is_object_dtype, infer_dtype
import polars as pl
import re
from collections import Counter
from loguru import logger


def strflatten_index(idx: pd.Index, sep: str = "_", fillna: str = "NA") -> pd.Index:
    """Normalize to a string, flat, and no-NA (or No space) index"""

    if isinstance(idx, pd.MultiIndex):
        return idx.to_flat_index().fillna(fillna).map(lambda x: sep.join(map(str, x)))
    else:
        return idx.fillna(fillna).astype(str)


def set_range(series: pd.Series, range: Optional[Tuple | List | Dict[int, str]] = None):
    if range is None:
        return series

    if isinstance(range, tuple) and len(range) > 2 or len(range) == 0:
        raise ValueError(
            f"Invalid value in mapping item: the length of tuple range {range} are greater than 2"
        )

    if isinstance(range, tuple):
        if len(range) == 1 and isinstance(range[0], tuple):
            return series.clip(range[0], range[1], inplace=True)
        else:
            return series.where(series.between(range[0], range[1], inclusive="both"))

    if isinstance(range, list):
        return series.where(series.isin(range))

    if isinstance(range, dict):
        if isinstance(series.dtype, pd.CategoricalDtype):
            categories = list(dict(sorted(range.items())).values())

            return series.astype(pd.CategoricalDtype(categories, ordered=True))
        else:
            raise TypeError(
                f"Unsupported Dtype: dict range '{range}' can not apply to non-categorical series"
            )


def free_fillna(series: pd.Series, value: Any):
    if value is None:
        return series

    try:
        return series.fillna(value)
    except:
        return series.astype(object).fillna(value)


def free_astype(series: pd.Series, dtype: Any):
    if dtype is None:
        return series
    try:
        return series.astype(dtype)
    except:
        return series.astype(object).astype(dtype)


def is_default_index(idx: pd.Index) -> bool:
    """Check whether is default index"""
    return isinstance(idx, pd.RangeIndex) and idx.start == 0 and idx.step == 1


def infer_stata_bin(version: int = 18):
    system = platform.system()
    if system == "Linux":
        return rf"/usr/local/stata{version}"
    elif system == "Windows":
        return rf"C:/Program Files/Stata{version}"
    elif system == "Darwin":
        return rf"/Applications/Stata"
    else:
        raise Exception(f"Unsupported System: {system}")


def cast_mix_dtype(
    df: pd.DataFrame, dtype_backend: Literal["numpy_nullable", "pyarrow"] = "pyarrow"
):
    to_string_type = "string[pyarrow]" if dtype_backend == "pyarrow" else "string"

    return df.transform(
        lambda x: x.astype(to_string_type)
        if infer_dtype(x).startswith("mix")
        and is_object_dtype(x)
        and not is_string_dtype(x)
        or (
            isinstance(x.dtype, pd.CategoricalDtype)
            and not is_string_dtype(x.cat.categories)
        )
        else x,
        axis=0,
    ).convert_dtypes(dtype_backend=dtype_backend)


def convert_dtype_backend(
    df: pd.DataFrame, backend: Literal["numpy", "numpy_nullable", "pyarrow"] = "pyarrow"
):
    if backend == "numpy":
        return pl.from_pandas(df).to_pandas()
    else:
        return df.convert_dtypes(dtype_backend=backend)


def lreshape_frame(
    df: pd.DataFrame,
    groups: List[str] | Dict[str, List[str]],
    i: Optional[List[str] | str] = None,
    j: Optional[str] = None,
    sep: str = "@",
    suffix: str = r".*",
    dropna: bool = False
) -> pd.DataFrame:
    """Reshape to long format"""

    if not df.columns.is_unique:
        raise IndexError(f"column names is not unique")

    if j is None:
        long_df = pd.lreshape(df, groups, dropna=True)
    else:
        widecol_pattern = re.compile(f"({'|'.join(set(groups))})({sep})({suffix})")
        i = (
            df.columns.where(~df.columns.str.fullmatch(widecol_pattern)).dropna()
            if i is None
            else i
        )
        long_df = (
            pd.wide_to_long(df, stubnames=groups, i=i, j=j, sep=sep, suffix=suffix)
            .reset_index()
            .astype({j: "string[pyarrow]"})
        )

        if long_df[i].empty:
            raise ValueError(
                f"Can not match wide columns with pattern sep and suffix: {sep}{suffix}"
            )
    if dropna:
        subset = groups.keys() if isinstance(groups,dict) else groups
        return long_df.dropna(how='all', subset=subset)
    else:
        return long_df 


def wreshape_frame(
    df: pd.DataFrame,
    groups: Optional[List[str] | Dict[str, List[str]]] = None,
    i: Optional[List[str] | str] = None,
    j: Optional[str] = None,
    sep: str = "@",
) -> pd.DataFrame:
    """Reshape to wide format"""

    if not isinstance(groups, dict) and j is None:
        raise ValueError(f"'groups' is not a dictionary while 'j' is None")
    if isinstance(groups, dict) and j is not None:
        raise ValueError(f"'groups' and 'j' is conflict, please set one of them")

    columns = list(groups.keys()) if isinstance(groups, dict) else j
    values = list(groups.values()) if isinstance(groups, dict) else groups

    index = i or list(
        set(df.columns)
        - set(values)
        - (
            set(columns)
            if isinstance(columns, list)
            else {columns}
            if isinstance(columns, str)
            else set()
        )
    )

    wide_df = df.pivot(columns=columns, index=index, values=values)

    wide_df.columns = strflatten_index(
        wide_df.columns,
        sep=sep,
        fillna="NA",
    )
    wide_df.reset_index(inplace=True)
    return wide_df


def reshape_frame(
    df: pd.DataFrame,
    to_shape: Literal["long", "wide"],
    groups: Optional[List[str] | Dict[str, List[str]]] = None,
    i: Optional[List[str] | str] = None,
    j: Optional[str] = None,
    sep: str = "@",
    suffix: str = r".*",
    dropna: bool = False
):
    if to_shape == "long":
        return lreshape_frame(df, groups, i, j, sep, suffix, dropna)
    else:
        return wreshape_frame(df, groups, i, j, sep)


def append_frames(
    dfs: Iterable[pd.DataFrame],
    on: Optional[List[str]] = None,
    how: Literal["inner", "outer"] = "outer",
    keycol: Optional[Dict[str, List[str] | List[int]]] = None,
) -> pd.DataFrame:
    """Append dataframes to a dataframe"""

    if on is not None:
        dfs = (df.filter(items=on, axis=1) for df in dfs)

    if keycol is not None:
        key_idx = pd.MultiIndex.from_frame(pd.DataFrame(keycol))
        names = key_idx.names
        concated_df = pd.concat(
            dfs, join=how, copy=False, keys=key_idx.to_list(), names=names
        )
        concated_df.index = concated_df.index.droplevel(
            [name for name in concated_df.index.names if name not in set(names)]
        )
        concated_df.reset_index(inplace=True)

        return concated_df.astype(
            {
                k: "string[pyarrow]" if isinstance(v[0], str) else "int64[pyarrow]"
                for k, v in keycol.items()
            }
        )
    else:
        return pd.concat(dfs, join=how, copy=False, ignore_index=True)


def join_frames(
    dfs: Iterable[pd.DataFrame],
    on: Optional[List[str]] = None,
    how: Literal["left", "inner", "outer"] = "outer"
):
    """Merge dataframes to a dataframe"""

    if on is not None:
        dfs = (df.set_index(on) for df in dfs)
        
    return next(dfs).join(dfs, how=how).reset_index()


def concat_frames(
    dfs: Iterable[pd.DataFrame],
    axis: Literal["column", "row"],
    on: Optional[List[str]] = None,
    how: Literal["left", "inner", "outer"] = "outer",
    keycol: Optional[Dict[str, List[str | int]]] = None,
):
    if axis == "column":
        return join_frames(dfs, on, how)
    else:
        return append_frames(dfs, on, how, keycol)


def merge_dict_in_nest_list(
    list_of_lists: List[List[Dict] | List[str]], allow_duplciate_key: bool = False
) -> List[Dict | str]:
    merged_list = []
    for sublist in list_of_lists:
        merged_dict = {}
        for d in sublist:
            for key in d:
                if not allow_duplciate_key and key in merged_dict:
                    raise ValueError(f"Duplicate key '{key}' found. Merging stopped.")
                merged_dict[key] = d[key]
        merged_list.append(merged_dict)
    return merged_list


def get_duplicate_items(items: Iterable | Mapping):
    counter = Counter(items)
    return [item for item, count in counter.items() if count > 1]


def log_error(message: str, *args, throw: bool = True, **kwargs):
    logger.error(message, *args, **kwargs)
    if throw:
        raise Exception(message)


@typechecked
def split_frame_by_columns(df: pd.DataFrame, by: str | List[str]):
    for k, v in df.groupby(by=by):
        if isinstance(k, tuple):
            yield f"{'_'.join(map(lambda x: 'NA' if x is pd.NA else str(x),k))}", v
        else:
            yield f"{k}", v


@typechecked
def split_frame_by_rows(df: pd.DataFrame, by: int):
    for start in range(0, df.index.size, by):
        end = start + by
        yield f"{start}", df[start:end]


def split_frame(
    df: pd.DataFrame,
    by_columns: Optional[List[str] | str] = None,
    by_rows: Optional[int] = None,
):
    if (by_columns or by_rows) is None:
        raise ValueError(f"'by_columns' and 'by_rows' should not be all None.")

    if by_columns is not None and by_rows is None:
        for k, v in split_frame_by_columns(df, by=by_columns):
            yield k, v

    elif by_columns is None and by_rows is not None:
        for k, v in split_frame_by_rows(df, by=by_rows):
            yield k, v

    else:
        for k, sub_df in split_frame_by_columns(df, by=by_columns):
            for start in range(0, sub_df.index.size, by_rows):
                end = start + by_rows
                yield f"{k}_{start}", sub_df[start:end]


# def gfill(ss: pd.Series, groupby: pd.Series | List[pd.Series], method: Literal['b','f','bf','fb'] = 'fb'):
    
#     df = pd.concat([ss] + groupby) if isinstance(groupby, list) else pd.concat([ss,groupby])
    
#     if method == 'b':
#         return df.groupby([])
#     pass