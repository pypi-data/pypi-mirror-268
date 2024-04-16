from _typeshed import Incomplete

DEBUG: Incomplete
VERBOSE: Incomplete
__REGISTERED_INTERACTIONS__: Incomplete


def register_interaction(self) -> None:
    ...


def unregister_interaction(self) -> None:
    ...


class AbstractInteraction:
    LEFT_BUTTON: int
    MIDDLE_BUTTON: int
    RIGHT_BUTTON: int
    MOUSE_BUTTONS: Incomplete
    debug: Incomplete
    fnum: Incomplete
    interaction_name: Incomplete
    scope: Incomplete
    is_down: Incomplete
    is_drag: Incomplete
    is_running: bool
    pan_event_list: Incomplete
    zoom_event_list: Incomplete
    fig: Incomplete

    def __init__(self, **kwargs) -> None:
        ...

    def reset_mouse_state(self) -> None:
        ...

    def enable_pan_and_zoom(self, ax) -> None:
        ...

    def enable_pan(self, ax) -> None:
        ...

    def enable_zoom(self, ax) -> None:
        ...

    def start(self) -> None:
        ...

    def print_status(self) -> None:
        ...

    def show_page(self, *args) -> None:
        ...

    def connect_callbacks(self) -> None:
        ...

    def bring_to_front(self) -> None:
        ...

    def draw(self) -> None:
        ...

    def on_draw(self, event: Incomplete | None = ...) -> None:
        ...

    def show(self) -> None:
        ...

    def update(self) -> None:
        ...

    def on_scroll(self, event) -> None:
        ...

    def close(self) -> None:
        ...

    def on_close(self, event: Incomplete | None = ...) -> None:
        ...

    def on_motion(self, event) -> None:
        ...

    def on_drag(self, event: Incomplete | None = ...) -> None:
        ...

    def on_drag_inside(self, event: Incomplete | None = ...) -> None:
        ...

    def on_drag_stop(self, event: Incomplete | None = ...) -> None:
        ...

    def on_drag_start(self, event: Incomplete | None = ...) -> None:
        ...

    def on_key_press(self, event) -> None:
        ...

    def on_click(self, event) -> None:
        ...

    def on_click_release(self, event) -> None:
        ...

    def on_click_inside(self, event, ax) -> None:
        ...

    def on_click_outside(self, event) -> None:
        ...

    def show_popup_menu(self, options, event) -> None:
        ...

    def clear_parent_axes(self, ax) -> None:
        ...

    def clean_scope(self) -> None:
        ...

    def append_button(self,
                      text,
                      divider: Incomplete | None = ...,
                      rect: Incomplete | None = ...,
                      callback: Incomplete | None = ...,
                      size: str = ...,
                      location: str = ...,
                      ax: Incomplete | None = ...,
                      **kwargs):
        ...


class AbstractPagedInteraction(AbstractInteraction):
    current_pagenum: int
    nPages: Incomplete
    draw_hud: Incomplete
    NEXT_PAGE_HOTKEYS: Incomplete
    PREV_PAGE_HOTKEYS: Incomplete

    def __init__(self,
                 nPages: Incomplete | None = ...,
                 draw_hud: bool = ...,
                 **kwargs) -> None:
        ...

    def next_page(self, event) -> None:
        ...

    def prev_page(self, event) -> None:
        ...

    def make_hud(self) -> None:
        ...

    fig: Incomplete

    def prepare_page(self, fulldraw: bool = ...) -> None:
        ...

    def on_key_press(self, event) -> None:
        ...


def pretty_hotkey_map(hotkeys):
    ...


def matches_hotkey(key, hotkeys):
    ...
