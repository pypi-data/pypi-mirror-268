from _typeshed import Incomplete

DEFAULT_MAX_ROWS: int
WIN7_SIZES: Incomplete
GNOME3_SIZES: Incomplete


def infer_monitor_specs(res_w, res_h, inches_diag) -> None:
    ...


def get_resolution_info(monitor_num: int = 0) -> dict:
    ...


def get_number_of_monitors():
    ...


def get_monitor_geom(monitor_num: int = 0) -> tuple:
    ...


def get_monitor_geometries():
    ...


def get_stdpxls():
    ...


def get_xywh_pads():
    ...


def get_avail_geom(monitor_num: Incomplete | None = ...,
                   percent_w: float = ...,
                   percent_h: float = ...):
    ...


def get_valid_fig_positions(num_wins,
                            max_rows: Incomplete | None = ...,
                            row_first: bool = ...,
                            monitor_num: Incomplete | None = ...,
                            percent_w: float = ...,
                            percent_h: float = ...):
    ...
