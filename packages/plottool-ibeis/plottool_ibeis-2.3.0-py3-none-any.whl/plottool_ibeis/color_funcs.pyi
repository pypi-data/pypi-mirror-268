from typing import Any
from _typeshed import Incomplete


def is_base01(channels):
    ...


def is_base255(channels):
    ...


def assert_base01(channels) -> None:
    ...


def assert_base255(channels) -> None:
    ...


def to_base01(color255):
    ...


def to_base255(color01, assume01: bool = ...):
    ...


def ensure_base01(color: Any) -> Any:
    ...


def convert_255_to_hex(color255):
    ...


def convert_hex_to_255(hex_color):
    ...


def ensure_base255(color):
    ...


def brighten_rgb(rgb, amount):
    ...


def testshow_colors(rgb_list, gray=...) -> None:
    ...


def desaturate_rgb(rgb, amount):
    ...


def darken_rgb(rgb, amount):
    ...


def lighten_rgb(rgb, amount):
    ...


def adjust_hsv_of_rgb255(rgb255, *args, **kwargs):
    ...


def adjust_hsv_of_rgb(rgb: tuple,
                      hue_adjust: float = 0.0,
                      sat_adjust: float = 0.0,
                      val_adjust: float = 0.0) -> Any:
    ...


def brighten(*args, **kwargs):
    ...


def distinct_colors(N: int,
                    brightness: float = 0.878,
                    randomize: bool = ...,
                    hue_range=...,
                    cmap_seed: Incomplete | None = ...) -> list:
    ...


def add_alpha(colors):
    ...


CMAP_DICT: Incomplete


def show_all_colormaps() -> None:
    ...
