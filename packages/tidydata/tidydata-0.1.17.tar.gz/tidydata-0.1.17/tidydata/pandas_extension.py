import pandas as pd
from pandas.api.types import (
    is_any_real_numeric_dtype,
    is_integer_dtype,
    is_string_dtype,
    is_bool_dtype,
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_float_dtype
)
from typeguard import typechecked
from typing import Optional, Literal, Any, List
import re
from pandas._libs.missing import NAType
from numpy import log, log10, log2


@pd.api.extensions.register_series_accessor("bools")
class BooleanAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    def _validate(self, obj):
        if not is_bool_dtype(obj) or obj.dtype.name != "bool[pyarrow]":
            raise TypeError(f"Not a boolean series with dtype name 'bool[pyarrow]'.")

    def to_dummy(self, fill_value: Optional[bool] = None):
        bool_ss = self._obj
        if fill_value is not None:
            bool_ss = bool_ss.fillna(fill_value)

        return (
            bool_ss.astype(object).replace({True: 1, False: 0}).astype("int64[pyarrow]")
        )

    def to_cats(
        self,
        true: str = "Yes",
        false: str = "No",
        fill_value: Optional[bool] = None,
        ordered: bool = True,
    ):
        bool_ss = self._obj
        if fill_value is not None:
            bool_ss = bool_ss.fillna(fill_value)

        return (
            bool_ss.astype(object)
            .replace({True: true, False: false})
            .astype(pd.CategoricalDtype([false, true], ordered=ordered))
        )

    def _or(self, other: pd.Series, skipna: bool = True):
        if not is_bool_dtype(other):
            raise TypeError(f"Not a boolean series in 'other': {other}.")

        xor_ss = (self._obj | other).fillna(False)
        if skipna:
            both_nas = self._obj.isna() & other.isna()
            return xor_ss.mask(both_nas, pd.NA)
        else:
            any_nas = self._obj.isna() | other.isna()
            return xor_ss.mask(any_nas, pd.NA)


@pd.api.extensions.register_series_accessor("cats")
class CategoricalAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    def _validate(self, obj):
        if not isinstance(obj.dtype, pd.CategoricalDtype):
            raise TypeError(f"Not a Categorical series.")

    def to_dummy(
        self, true: List[str] | str | pd.Series, fill_value: Optional[Any] = None
    ):
        cat_ss = self._obj
        cat_codes = cat_ss.cat.categories

        if fill_value is not None:
            if fill_value not in cat_codes:
                raise ValueError(
                    f"Value in 'fill_value' is not in existing categories."
                )
            else:
                cat_ss = cat_ss.fillna(fill_value)

        if isinstance(true, pd.Series) and not is_bool_dtype(true):
            raise TypeError(f"Value in 'true' is not a boolean series: {true}.")

        if isinstance(true, pd.Series):
            fill_true = true.fillna(False)
            return (
                self._obj.astype(object)
                .where(fill_true, 0)
                .mask(fill_true, 1)
                .where(true.notna(), pd.NA)
                .astype("int64[pyarrow]")
            )
        else:
            if isinstance(true, str):
                true = [true]
            repls = {cat: 1 if cat in set(true) else 0 for cat in cat_codes}
            return cat_ss.astype(object).replace(repls).astype("int64[pyarrow]")

    def to_bool(
        self, true: List[str] | str | pd.Series, fill_value: Optional[Any] = None
    ):
        return self._obj.cats.to_dummy(true, fill_value).astype("bool[pyarrow]")



@pd.api.extensions.register_series_accessor("combs")
class CombineAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def _max(self, other: pd.Series, skipna: bool = True):
        return pd.concat((self._obj, other), axis=1).max(axis=1, skipna=skipna)

    def _min(self, other: pd.Series, skipna: bool = True):
        return pd.concat((self._obj, other), axis=1).min(axis=1, skipna=skipna)

    def _mean(self, other: pd.Series, skipna: bool = True):
        return pd.concat((self._obj, other), axis=1).mean(axis=1, skipna=skipna)
    
    def _if(self, other: pd.Series, cond: pd.Series, skipna: bool = False):
        fill_cond = cond.fillna(False)
        mask_cond = (
            fill_cond | self._obj.isna() if skipna else fill_cond & self._obj.notna()
        )
        return self._obj.mask(mask_cond, other)


@pd.api.extensions.register_series_accessor("strs")
class StringAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    def _validate(self, obj):
        if obj.dtype.name != "string":
            raise TypeError(f"Not a string series with dtype name 'string'.")

    def to_numeric(self, coerce: bool = False):
        errors = "coerce" if coerce else "raise"
        return pd.to_numeric(self._obj, errors=errors, dtype_backend="pyarrow")

    def cat(
        self, other: str | pd.Series, sep: str = "", fill_value: Optional[str] = None
    ):
        ss = self._obj.fillna(fill_value) if fill_value is not None else self._obj

        if isinstance(other, str):
            return ss + sep + other
        else:
            return ss.str.cat(other, sep=sep, na_rep=fill_value)

    def lit(
        self, other: str
    ):
        return pd.Series(other,index=self._obj.index,dtype='string[pyarrow]')

@pd.api.extensions.register_series_accessor("ints")
class IntegerAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    def _validate(self, obj):
        if not is_integer_dtype(obj):
            raise TypeError(f"Not a integer series: {obj}.")

    def to_string(self):
        return self._obj.astype("string[pyarrow]")

    def log(self, base: Literal["e"] = "e"):
        log_funcs = {"e": log, "10": log10, "2": log2}
        return (
            self._obj.astype("float64")
            .transform(log_funcs[base])
            .astype("float64[pyarrow]")
        )



@pd.api.extensions.register_series_accessor("floats")
class IntegerAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    def _validate(self, obj):
        if not is_float_dtype(obj):
            raise TypeError(f"Not a float series: {obj}.")
        
    def log(self, base: Literal["e"] = "e"):
        log_funcs = {"e": log, "10": log10, "2": log2}
        return (
            self._obj.astype("float64")
            .transform(log_funcs[base])
            .astype("float64[pyarrow]")
        )

@pd.api.extensions.register_series_accessor("econ")
class EconomicsAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj
        self._educ10_cn = {
            "No formal education illiterate": 1,
            "Did not finish primary school but capable of reading and/or writing": 2,
            "Sishu": 3,
            "Elementary school": 6,
            "Middle school": 9,
            "High school": 12,
            "Vocational school": 12,
            "Two/Three Year College/Associate degree": 15,
            "Four Year College/Bachelor's degree": 16,
            "Post-graduated(Master/PhD)": 19,
        }
        

        
        self._educ_system = {"cn10": self._educ10_cn}

    def to_educ_year(self, system: Optional[Literal["cn10"]] = "cn10"):
        ss = self._obj
        if not isinstance(
            ss.dtype, pd.CategoricalDtype
        ) and not ss.dtype.name.startswith("dictionary"):
            raise TypeError(f"Not a categorical or dictionary series: {ss}.")

        if ss.dtype.name.startswith("dictionary"):
            ss = ss.astype("category")

        if set(ss.cat.categories) != set(self._educ_system[system].keys()):
            raise ValueError(
                f"Categories Mismatch: categories from series can not match the categoeies of 'cn10'."
            )

        return (
            ss.astype(object)
            .replace(self._educ_system[system])
            .astype("int64[pyarrow]")
        )
    def to_educ_level(self, system: Optional[Literal['cn6','isced97-3','cn8','cn2']]="cn6"):
        
        cn10_to_cn8 = {
            "No formal education illiterate": 'Illiterate',
            "Did not finish primary school but capable of reading and/or writing": 'Capable of reading and/or writing',
            "Sishu": 'Capable of reading and/or writing',
            "Elementary school": 'Elementary school',
            "Middle school": "Middle school",
            "High school": "High school/Vocational school",
            "Vocational school": "High school/Vocational school",
            "Two/Three Year College/Associate degree": "Two/Three Year College/Associate degree",
            "Four Year College/Bachelor's degree": "Four Year College/Bachelor's degree",
            "Post-graduated(Master/PhD)":"Post-graduated(Master/PhD)"
        }
        cn10_to_cn6 = {
            "No formal education illiterate": 'Less than middle school',
            "Did not finish primary school but capable of reading and/or writing": 'Less than middle school',
            "Sishu": 'Less than middle school',
            "Elementary school": 'Less than middle school',
            "Middle school": "Middle school",
            "High school": "High school/Vocational school",
            "Vocational school": "High school/Vocational school",
            "Two/Three Year College/Associate degree": "Two/Three Year College/Associate degree",
            "Four Year College/Bachelor's degree": "Four Year College/Bachelor's degree",
            "Post-graduated(Master/PhD)":"Post-graduated(Master/PhD)"
        }
        
        cn10_to_isced3 = {
            "No formal education illiterate": 'Less than higher secondary education',
            "Did not finish primary school but capable of reading and/or writing":'Less than higher secondary education',
            "Sishu": 'Less than higher secondary education',
            "Elementary school": 'Less than higher secondary education',
            "Middle school": 'Less than higher secondary education',
            "High school": "Higher secondary education",
            "Vocational school": "Higher secondary education",
            "Two/Three Year College/Associate degree": "Tertiary eduction",
            "Four Year College/Bachelor's degree": "Tertiary eduction",
            "Post-graduated(Master/PhD)":"Tertiary eduction"
        }
        
        cn10_to_cn2 = {
            "No formal education illiterate": 'Without tertiary education',
            "Did not finish primary school but capable of reading and/or writing":'Without tertiary education',
            "Sishu": 'Without tertiary education',
            "Elementary school": 'Without tertiary education',
            "Middle school": 'Without tertiary education',
            "High school": 'Without tertiary education',
            "Vocational school": 'Without tertiary education',
            "Two/Three Year College/Associate degree": "Tertiary eduction",
            "Four Year College/Bachelor's degree": "Tertiary eduction",
            "Post-graduated(Master/PhD)":"Tertiary eduction"
        }
        
        if system == 'isced97-3':
            cat_dtype = pd.CategoricalDtype(
                ['Less than higher secondary education',
                'Higher secondary education',
                'Tertiary eduction'],ordered=True)
            
            return self._obj.astype('string[pyarrow]').replace(cn10_to_isced3).astype(cat_dtype)

        elif system == 'cn2':
            cat_dtype = pd.CategoricalDtype(
                ['Without tertiary education',
                'Tertiary eduction'],ordered=True)
            
            return self._obj.astype('string[pyarrow]').replace(cn10_to_cn2).astype(cat_dtype)


        elif system == 'cn8':
            cat_dtype = pd.CategoricalDtype(
                ['Illiterate',
                'Capable of reading and/or writing',
                'Elementary school',
                'Middle school',
                'High school/Vocational school',
                'Two/Three Year College/Associate degree',
                "Four Year College/Bachelor's degree",
                "Post-graduated(Master/PhD)"],ordered=True)

            return self._obj.astype('string[pyarrow]').replace(cn10_to_cn8).astype(cat_dtype)
        
        else:
            cat_dtype = pd.CategoricalDtype(
                ['Less than middle school',
                'Middle school',
                'High school/Vocational school',
                'Two/Three Year College/Associate degree',
                "Four Year College/Bachelor's degree",
                "Post-graduated(Master/PhD)"],ordered=True)

            return self._obj.astype('string[pyarrow]').replace(cn10_to_cn6).astype(cat_dtype)
    
    def prov_to_area(self, system: Literal['econ3']='econ3'):
        """转换省份名到大区域名"""
        
        # 国家统计局2011经济分区 
        # http://www.stats.gov.cn/ztjc/zthd/sjtjr/dejtjkfr/tjkp/201106/t20110613_71947.htm
        prov_to_econ3 = {
            "北京":"东部",
            "天津":"东部",
            "河北":"东部",
            "上海":"东部",
            "江苏":"东部",
            "浙江":"东部",
            "福建":"东部",
            "山东":"东部",
            "广东":"东部",
            "海南":"东部",
            "辽宁":"东部",
            "吉林":"东部",
            "黑龙江":"东部",
            "山西":"中部",
            "安徽":"中部",
            "江西":"中部",
            "河南":"中部",
            "湖北":"中部",
            "湖南":"中部",
            "内蒙古":"西部",
            "广西":"西部",
            "重庆":"西部",
            "四川":"西部",
            "贵州":"西部",
            "云南":"西部",
            "西藏":"西部",
            "陕西":"西部",
            "甘肃":"西部",
            "青海":"西部",
            "宁夏":"西部",
            "新疆":"西部"
        }
        
        if system == "econ3":
            cat_dtype = pd.CategoricalDtype(['东部','中部','西部'],ordered=True)
            return self._obj.astype('string[pyarrow]').replace(prov_to_econ3).astype(cat_dtype)
        
