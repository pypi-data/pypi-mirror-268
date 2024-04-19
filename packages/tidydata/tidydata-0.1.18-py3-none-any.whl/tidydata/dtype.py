from typing import Literal

DtypeStr = Literal[
    "Int",
    "UInt",
    "Float",
    "Bool",
    "Str",
    "Cat",
    "Date",
    "Time",
    "Duration",
    "Obj",
    "Null",
    "Bin",
]

DtypeMappings = {
    "Int": "int64[pyarrow]",
    "UInt": "uint64[pyarrow]",
    "Float": "float64[pyarrow]",
    "Bool": "bool[pyarrow]",
    "Str": "string[pyarrow]",
    "Cat": "category",
    "Datetime": "datetime64[ns]",
    "Duration": "timedelta64[ns]",
    "Obj": "object",
    "Null": "null[pyarrow]",
    "Bin": "binary[pyarrow]",
}

PANDASDTYPE_TO_ALIAS = {
    "int64[pyarrow]": "Int",
    "int64": "Int",
    "Int64": "Int",
    "uint64[pyarrow]": "UInt",
    "float64[pyarrow]": "Float",
    "double[pyarrow]": "Float",
    "float64": "Float",
    "Float64": "Float",
    "bool[pyarrow]": "Bool",
    "string[pyarrow]": "Str",
    "category": "Cat",
    "datetime64[ns]": "Datetime",
    "timedelta64[ns]": "Duration",
    "object": "Obj",
    "null[pyarrow]": "Null",
    "binary[pyarrow]": "Bin",
}
