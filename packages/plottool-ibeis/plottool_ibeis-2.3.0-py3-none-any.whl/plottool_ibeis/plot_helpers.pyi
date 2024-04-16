from typing import Any
from _typeshed import Incomplete

SIFT_OR_VECFIELD: Incomplete


def draw() -> None:
    ...


def get_square_row_cols(nSubplots: Any,
                        max_cols: None = None,
                        fix: bool = ...,
                        inclusive: bool = ...) -> tuple:
    ...


def get_plotdat(ax, key, default: Incomplete | None = ...):
    ...


def set_plotdat(ax, key, val) -> None:
    ...


def del_plotdat(ax, key) -> None:
    ...


def get_plotdat_dict(ax):
    ...


def get_bbox_centers(bbox_list):
    ...


def qt4ensure() -> None:
    ...


def qtensure() -> None:
    ...


ensureqt = qt4ensure


def kp_info(kp):
    ...
