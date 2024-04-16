from _typeshed import Incomplete

BASE_CLASS: Incomplete


class MatchInteraction2(BASE_CLASS):
    rchip1: Incomplete
    rchip2: Incomplete
    kpts1: Incomplete
    kpts2: Incomplete
    fm: Incomplete
    fs: Incomplete
    fk: Incomplete
    fsv: Incomplete
    vecs1: Incomplete
    vecs2: Incomplete
    H1: Incomplete
    H2: Incomplete
    warp_homog: bool
    mode: Incomplete
    mx: Incomplete
    vert: Incomplete
    same_fig: Incomplete
    last_fx: int
    xywh2: Incomplete
    fnum2: Incomplete
    title: Incomplete
    truth: Incomplete

    def __init__(self,
                 rchip1,
                 rchip2,
                 kpts1,
                 kpts2,
                 fm,
                 fs,
                 fsv,
                 vecs1,
                 vecs2,
                 H1: Incomplete | None = ...,
                 H2: Incomplete | None = ...,
                 fnum: Incomplete | None = ...,
                 **kwargs) -> None:
        ...

    def plot(self, *args, **kwargs) -> None:
        ...

    def chipmatch_view(self,
                       fnum: Incomplete | None = ...,
                       pnum=...,
                       verbose: Incomplete | None = ...,
                       **kwargs_) -> None:
        ...

    def select_ith_match(self, mx) -> None:
        ...

    def on_click_inside(self, event, ax) -> None:
        ...

    def on_click_outside(self, event) -> None:
        ...

    def get_popup_options(self):
        ...


def show_keypoint_gradient_orientations(
        ibs,
        rchip,
        kp,
        vec,
        fnum: Incomplete | None = ...,
        pnum: Incomplete | None = ...,
        config2_: Incomplete | None = ...) -> None:
    ...
