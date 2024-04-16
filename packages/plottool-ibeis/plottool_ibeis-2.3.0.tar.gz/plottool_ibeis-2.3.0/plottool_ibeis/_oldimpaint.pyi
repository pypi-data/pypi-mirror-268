from _typeshed import Incomplete


class _OldPainter:
    button_pressed: bool
    mask: Incomplete
    brush_size: int
    ax: Incomplete
    fig: Incomplete
    color: int
    background: Incomplete

    def __init__(self, fig, ax, mask) -> None:
        ...

    def draw(self) -> None:
        ...

    def do_blit(self) -> None:
        ...

    def draw_callback(self, event) -> None:
        ...

    def button_press_callback(self, event) -> None:
        ...

    def update_image(self) -> None:
        ...

    def button_release_callback(self, event) -> None:
        ...

    def on_move(self, event) -> None:
        ...
