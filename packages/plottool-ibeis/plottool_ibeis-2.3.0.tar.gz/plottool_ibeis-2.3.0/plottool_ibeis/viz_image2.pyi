from _typeshed import Incomplete


def draw_chip_overlay(ax, bbox, theta, text, is_sel) -> None:
    ...


def draw_image_overlay(ax,
                       bbox_list=...,
                       theta_list: Incomplete | None = ...,
                       text_list: Incomplete | None = ...,
                       sel_list: Incomplete | None = ...,
                       draw_lbls: bool = ...) -> None:
    ...


def show_image(img,
               bbox_list=...,
               title: str = ...,
               theta_list: Incomplete | None = ...,
               text_list: Incomplete | None = ...,
               sel_list: Incomplete | None = ...,
               draw_lbls: bool = ...,
               fnum: Incomplete | None = ...,
               annote: bool = ...,
               **kwargs):
    ...
