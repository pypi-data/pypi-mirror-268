import matplotlib as mpl
from _typeshed import Incomplete


def pass_props(dict1, dict2, *args) -> None:
    ...


def draw_keypoints(ax: mpl.Axes,
                   kpts_,
                   scale_factor: float = 1.0,
                   offset: tuple = ...,
                   rotation: float = 0.0,
                   ell: bool = True,
                   pts: bool = False,
                   rect: bool = False,
                   eig: bool = False,
                   ori: bool = False,
                   sifts: None = None,
                   siftkw=...,
                   H: Incomplete | None = ...,
                   **kwargs) -> None:
    ...


class HomographyTransform(mpl.transforms.Transform):
    input_dims: int
    output_dims: int
    is_separable: bool
    H: Incomplete

    def __init__(self,
                 H,
                 axis: Incomplete | None = ...,
                 use_rmin: bool = ...) -> None:
        ...

    def transform_non_affine(self, input_xy):
        ...

    def transform_path_non_affine(self, path):
        ...


def get_invVR_aff2Ds(kpts, H: Incomplete | None = ...):
    ...


def ellipse_actors(invVR_aff2Ds):
    ...


def rectangle_actors(invVR_aff2Ds):
    ...


def eigenvector_actors(invVR_aff2Ds):
    ...


def orientation_actors(kpts, H: Incomplete | None = ...):
    ...
