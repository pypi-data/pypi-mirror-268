from typing import Callable
from _typeshed import Incomplete
from plottool_ibeis import abstract_interaction

__docstubs__: str


def check_if_subinteract(func):
    ...


class ExpandableInteraction(abstract_interaction.AbstractInteraction):
    nRows: Incomplete
    nCols: Incomplete
    pnum_list: Incomplete
    interactive: Incomplete
    ishow_func_list: Incomplete
    func_list: Incomplete
    fnum: Incomplete
    fig: Incomplete

    def __init__(self,
                 fnum: Incomplete | None = ...,
                 _pnumiter: Incomplete | None = ...,
                 interactive: Incomplete | None = ...,
                 **kwargs) -> None:
        ...

    def __iadd__(self, func):
        ...

    def append_plot(self,
                    func: Callable,
                    pnum: tuple | None = None,
                    ishow_func: Callable | None = None,
                    px: int | None = None) -> None:
        ...

    def append_partial(self, func: Callable, *args, **kwargs) -> None:
        ...

    def show_page(self):
        ...

    def on_click(self, event) -> None:
        ...


def zoom_factory(ax: Incomplete | None = ...,
                 zoomable_list=...,
                 base_scale: float = ...):
    ...


def pan_factory(ax: Incomplete | None = ...):
    ...


class PanEvents:
    press: Incomplete
    cur_xlim: Incomplete
    cur_ylim: Incomplete
    x0: Incomplete
    y0: Incomplete
    x1: Incomplete
    y1: Incomplete
    xpress: Incomplete
    ypress: Incomplete
    xzoom: bool
    yzoom: bool
    cidBP: Incomplete
    cidBR: Incomplete
    cidBM: Incomplete
    cidKeyP: Incomplete
    cidKeyR: Incomplete
    cidScroll: Incomplete
    ax: Incomplete

    def __init__(self, ax: Incomplete | None = ...) -> None:
        ...

    def pan_on_press(self, event) -> None:
        ...

    def pan_on_release(self, event) -> None:
        ...

    def pan_on_motion(self, event) -> None:
        ...
