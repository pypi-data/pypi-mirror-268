import matplotlib as mpl
import utool as ut
from _typeshed import Incomplete
from plottool_ibeis import abstract_interaction

print: Incomplete
rrr: Incomplete
profile: Incomplete
DEFAULT_SPECIES_TAG: str
ACCEPT_SAVE_HOTKEY: Incomplete
ADD_RECTANGLE_HOTKEY: str
ADD_RECTANGLE_FULL_HOTKEY: str
DEL_RECTANGLE_HOTKEY: str
TOGGLE_LABEL_HOTKEY: str
HACK_OFF_SPECIES_TYPING: bool
NEXT_IMAGE_HOTKEYS: Incomplete
PREV_IMAGE_HOTKEYS: Incomplete
TAU: Incomplete


class AnnotPoly(mpl.patches.Polygon, ut.NiceRepr):

    def __init__(poly,
                 ax,
                 num,
                 verts,
                 theta,
                 species,
                 fc=...,
                 line_color=...,
                 line_width: int = ...,
                 is_orig: bool = ...,
                 metadata: Incomplete | None = ...,
                 valid_species: Incomplete | None = ...,
                 manager: Incomplete | None = ...) -> None:
        ...

    def axes_init(poly, ax) -> None:
        ...

    def move_to_back(poly) -> None:
        ...

    def __nice__(poly):
        ...

    def add_to_axis(poly, ax) -> None:
        ...

    def remove_from_axis(poly, ax) -> None:
        ...

    def draw_self(poly,
                  ax,
                  show_species_tags: bool = ...,
                  editable: bool = ...) -> None:
        ...

    def calc_tag_position(poly):
        ...

    def calc_handle_display_coords(poly):
        ...

    def update_color(poly,
                     selected: bool = ...,
                     editing_parts: bool = ...) -> None:
        ...

    def update_lines(poly) -> None:
        ...

    def set_species(poly, text) -> None:
        ...

    def increment_species(poly, amount: int = ...) -> None:
        ...

    def resize_poly(poly, x, y, idx, ax) -> None:
        ...

    def rotate_poly(poly, dtheta, ax) -> None:
        ...

    def move_poly(poly, dx, dy, ax) -> None:
        ...

    def update_display_coords(poly) -> None:
        ...

    def print_info(poly) -> None:
        ...

    def get_poly_mask(poly, shape):
        ...

    def is_near_handle(poly, xy_pt, max_dist):
        ...

    @property
    def size(poly):
        ...


class AnnotationInteraction(abstract_interaction.AbstractInteraction):
    valid_species: Incomplete
    commit_callback: Incomplete
    but_width: float
    next_prev_but_height: float
    but_height: Incomplete
    callback_funcs: Incomplete
    mpl_callback_ids: Incomplete
    img: Incomplete
    show_species_tags: bool
    max_dist: int
    do_mask: Incomplete
    img_ind: Incomplete
    species_tag: Incomplete
    showverts: bool
    fc_default: Incomplete
    mouseX: Incomplete
    mouseY: Incomplete
    ind_xy: Incomplete
    parent_poly: Incomplete
    background: Incomplete
    reinitialize_variables: Incomplete
    fig: Incomplete

    def __init__(self,
                 img,
                 img_ind: Incomplete | None = ...,
                 commit_callback: Incomplete | None = ...,
                 verts_list: Incomplete | None = ...,
                 bbox_list: Incomplete | None = ...,
                 theta_list: Incomplete | None = ...,
                 species_list: Incomplete | None = ...,
                 metadata_list: Incomplete | None = ...,
                 line_width: int = ...,
                 line_color=...,
                 face_color=...,
                 fnum: Incomplete | None = ...,
                 default_species=...,
                 next_callback: Incomplete | None = ...,
                 prev_callback: Incomplete | None = ...,
                 do_mask: bool = ...,
                 valid_species=...,
                 **kwargs) -> None:
        ...

    fnum: Incomplete
    ax: Incomplete

    def reinitialize_figure(self, fnum: Incomplete | None = ...) -> None:
        ...

    def add_action_buttons(self) -> None:
        ...

    def disconnect_mpl_callbacks(self, canvas) -> None:
        ...

    def connect_mpl_callbacks(self, canvas) -> None:
        ...

    prev_callback: Incomplete
    next_callback: Incomplete

    def update_callbacks(self, next_callback, prev_callback) -> None:
        ...

    polys: Incomplete

    def update_image_and_callbacks(self, img, bbox_list, theta_list,
                                   species_list, metadata_list, next_callback,
                                   prev_callback) -> None:
        ...

    def update_UI(self) -> None:
        ...

    def draw_artists(self) -> None:
        ...

    @property
    def uneditable_polys(self):
        ...

    @property
    def editable_polys(self):
        ...

    def get_poly_under_cursor(self, x, y):
        ...

    def get_most_recently_added_poly(self):
        ...

    def new_polygon(self,
                    verts,
                    theta,
                    species,
                    fc=...,
                    line_color=...,
                    line_width: int = ...,
                    is_orig: bool = ...,
                    metadata: Incomplete | None = ...):
        ...

    original_indices: Incomplete
    original_bbox_list: Incomplete
    original_theta_list: Incomplete
    original_species_list: Incomplete
    original_metadata_list: Incomplete

    def handle_polygon_creation(self, bbox_list, theta_list, species_list,
                                metadata_list) -> None:
        ...

    def add_new_poly(self,
                     event: Incomplete | None = ...,
                     full: bool = ...) -> None:
        ...

    def delete_current_poly(self, event: Incomplete | None = ...) -> None:
        ...

    def edit_poly_parts(self, poly) -> None:
        ...

    @property
    def in_edit_parts_mode(self):
        ...

    def toggle_species_label(self) -> None:
        ...

    def save_and_exit(self, event, do_close: bool = ...):
        ...

    def next_image(self, event) -> None:
        ...

    def prev_image(self, event) -> None:
        ...

    def start(self) -> None:
        ...

    def show(self) -> None:
        ...

    def draw_callback(self, event) -> None:
        ...

    def is_poly_pickable(self, artist, event):
        ...

    def on_pick(self, event) -> None:
        ...

    def on_click(self, event) -> None:
        ...

    def on_motion(self, event) -> None:
        ...

    def on_click_release(self, event) -> None:
        ...

    def on_figure_leave(self, event) -> None:
        ...

    def on_key_press(self, event):
        ...


def pretty_hotkey_map(hotkeys):
    ...


def apply_mask(img, mask):
    ...


def points_center(pts):
    ...


def rotate_points_around(points, theta, ax, ay):
    ...


def calc_display_coords(oldcoords, theta):
    ...


def polarDelta(p1, p2):
    ...


def apply_polarDelta(poldelt, cart):
    ...


def is_within_distance_from_line(pt, line, max_dist):
    ...


def check_min_wh(coords):
    ...


def default_vertices(img,
                     polys: Incomplete | None = ...,
                     mouseX: Incomplete | None = ...,
                     mouseY: Incomplete | None = ...):
    ...


def check_valid_coords(ax, coords_list):
    ...


def check_dims(ax, xy_pt, margin: float = ...):
    ...


def enforce_dims(ax, xy_pt, margin: float = ...):
    ...


def test_interact_annots():
    ...
