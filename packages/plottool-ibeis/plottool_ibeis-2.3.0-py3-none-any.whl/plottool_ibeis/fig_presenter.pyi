from _typeshed import Incomplete

SLEEP_TIME: float
__QT4_WINDOW_LIST__: Incomplete
VERBOSE: Incomplete


def unregister_qt4_win(win) -> None:
    ...


def register_qt4_win(win) -> None:
    ...


def set_geometry(fnum, x, y, w, h) -> None:
    ...


def get_geometry(fnum):
    ...


def get_all_figures():
    ...


def get_all_qt4_wins():
    ...


def all_figures_show() -> None:
    ...


def show_figure(fig) -> None:
    ...


def all_figures_tight_layout() -> None:
    ...


def get_main_win_base():
    ...


def get_all_windows():
    ...


def all_figures_tile(max_rows: Incomplete | None = ...,
                     row_first: bool = ...,
                     no_tile: bool = ...,
                     monitor_num: Incomplete | None = ...,
                     percent_w: Incomplete | None = ...,
                     percent_h: Incomplete | None = ...,
                     hide_toolbar: bool = ...) -> None:
    ...


def all_figures_bring_to_front() -> None:
    ...


def close_all_figures() -> None:
    ...


def close_figure(fig) -> None:
    ...


def get_figure_window(fig):
    ...


def bring_to_front(fig) -> None:
    ...


def show() -> None:
    ...


def reset() -> None:
    ...


def draw() -> None:
    ...


def update() -> None:
    ...


def iupdate() -> None:
    ...


iup = iupdate


def present(*args, **kwargs) -> None:
    ...
