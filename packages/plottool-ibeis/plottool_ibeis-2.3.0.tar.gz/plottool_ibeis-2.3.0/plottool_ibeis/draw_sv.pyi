from _typeshed import Incomplete


def get_blended_chip(chip1, chip2, M):
    ...


def show_sv(chip1,
            chip2,
            kpts1,
            kpts2,
            fm,
            homog_tup: Incomplete | None = ...,
            aff_tup: Incomplete | None = ...,
            mx: Incomplete | None = ...,
            show_assign: bool = ...,
            show_lines: bool = ...,
            show_kpts: bool = ...,
            show_aff: Incomplete | None = ...,
            fnum: int = ...,
            refine_method: Incomplete | None = ...,
            **kwargs):
    ...


def show_sv_simple(chip1,
                   chip2,
                   kpts1,
                   kpts2,
                   fm,
                   inliers,
                   mx: Incomplete | None = ...,
                   fnum: int = ...,
                   vert: Incomplete | None = ...,
                   **kwargs) -> None:
    ...
