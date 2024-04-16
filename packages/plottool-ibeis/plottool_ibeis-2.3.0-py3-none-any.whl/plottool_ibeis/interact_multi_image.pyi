from _typeshed import Incomplete

BASE_CLASS: Incomplete


class MultiImageInteraction(BASE_CLASS):
    context_option_funcs: Incomplete
    thetas_list: Incomplete
    bboxes_list: Incomplete
    xlabel_list: Incomplete
    gid_list: Incomplete
    vizkw: Incomplete
    nImgs: Incomplete
    nPerPage: Incomplete
    current_index: int
    page_number: int
    gpath_list: Incomplete
    first_load: bool
    scope: Incomplete
    current_pagenum: int
    nPages: Incomplete

    def __init__(self,
                 gpath_list,
                 nPerPage: int = ...,
                 bboxes_list: Incomplete | None = ...,
                 thetas_list: Incomplete | None = ...,
                 verts_list: Incomplete | None = ...,
                 gid_list: Incomplete | None = ...,
                 nImgs: Incomplete | None = ...,
                 fnum: Incomplete | None = ...,
                 context_option_funcs: Incomplete | None = ...,
                 xlabel_list: Incomplete | None = ...,
                 vizkw: Incomplete | None = ...,
                 **kwargs) -> None:
        ...

    def dump_to_disk(self,
                     dpath,
                     num: Incomplete | None = ...,
                     prefix: str = ...) -> None:
        ...

    def make_hud(self) -> None:
        ...

    def next_page(self, event) -> None:
        ...

    def prev_page(self, event) -> None:
        ...

    start_index: Incomplete
    nDisplay: Incomplete
    pnum_: Incomplete
    stop_index: Incomplete
    fig: Incomplete

    def prepare_page(self, pagenum) -> None:
        ...

    def show_page(self, pagenum: Incomplete | None = ...) -> None:
        ...

    def plot_image(self, index) -> None:
        ...

    def update_images(self, img_ind, updated_bbox_list, updated_theta_list,
                      changed_annottups, new_annottups) -> None:
        ...

    mc: Incomplete

    def on_click_inside(self, event, ax) -> None:
        ...

    def on_key_press(self, event) -> None:
        ...
