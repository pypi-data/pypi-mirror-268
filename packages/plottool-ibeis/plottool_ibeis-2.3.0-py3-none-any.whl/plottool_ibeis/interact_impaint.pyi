from _typeshed import Incomplete

PAINTER_BASE: Incomplete


class PaintInteraction(PAINTER_BASE):
    mask: Incomplete
    img: Incomplete
    brush_size: int
    valid_colors1: Incomplete
    valid_colors2: Incomplete
    color1_idx: int
    color1: Incomplete
    color2: Incomplete
    background: Incomplete
    last_stroke: Incomplete
    finished_callback: Incomplete

    def __init__(self, img, **kwargs) -> None:
        ...

    def update_title(self) -> None:
        ...

    ax: Incomplete

    def static_plot(self, fnum: Incomplete | None = ..., pnum=...) -> None:
        ...

    def update_image(self) -> None:
        ...

    def on_close(self, event: Incomplete | None = ...) -> None:
        ...

    def do_blit(self) -> None:
        ...

    def on_draw(self, event) -> None:
        ...

    def apply_stroke(self, x, y, color) -> None:
        ...

    def on_click_inside(self, event, ax) -> None:
        ...

    def on_scroll(self, event) -> None:
        ...

    def on_key_press(self, event) -> None:
        ...

    def on_drag_stop(self, event) -> None:
        ...

    def on_drag_inside(self, event) -> None:
        ...


def impaint_mask2(img, init_mask: Incomplete | None = ...):
    ...


def draw_demo() -> None:
    ...
