import polars as pl
from typing import Any, Optional, Dict, Tuple, List


@pl.api.register_dataframe_namespace("tidy")
class TidyFrame:
    def __init__(self, df: pl.DataFrame):
        self._df = df

    def where(
        self,
        mapping: Optional[Dict[str, Tuple | List | Dict[int, str]]] = None,
    ) -> pl.DataFrame:
        pass


@pl.api.register_expr_namespace("tidy")
class TidyExpr:
    def __init__(self, expr: pl.Expr):
        self._expr = expr

    def trunc(self, range: Tuple[Any, Any] | List[Any]) -> pl.Expr:
        if isinstance(range, tuple):
            return (
                pl.when(self._expr.is_between(range[0], range[1], closed="both"))
                .then(self._expr)
                .otherwise(None)
            )
        else:
            return pl.when(self._expr.is_in(range)).then(self._expr).otherwise(None)

    def winsor(self, lower: Any, upper: Any) -> pl.Expr:
        return self._expr.clip(lower, upper)


@pl.api.register_series_namespace("tidy")
class TidySeries:
    def __init__(self, s: pl.Series):
        self._s = s

    def winsor(self) -> pl.Series:
        return self._s.cut()
