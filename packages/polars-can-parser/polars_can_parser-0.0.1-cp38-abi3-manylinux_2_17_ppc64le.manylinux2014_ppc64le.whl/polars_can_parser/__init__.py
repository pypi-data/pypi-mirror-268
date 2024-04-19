from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import polars as pl

from polars_can_parser.utils import parse_into_expr, register_plugin, parse_version

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

if parse_version(pl.__version__) < parse_version("0.20.16"):
    from polars.utils.udfs import _get_shared_lib_location

    lib: str | Path = _get_shared_lib_location(__file__)
else:
    lib = Path(__file__).parent


def decode_can_message(expr: IntoExpr, *, path_to_dbc: str, signal_name: str) -> pl.Expr:
    expr = parse_into_expr(expr)
    return expr.register_plugin(
        symbol="decode_can_message",
        is_elementwise=True,
        lib=lib,
        kwargs={"path_to_dbc": path_to_dbc, "signal_name": signal_name},
    )