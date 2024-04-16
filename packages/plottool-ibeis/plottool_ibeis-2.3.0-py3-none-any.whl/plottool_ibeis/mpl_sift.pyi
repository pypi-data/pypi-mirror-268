from typing import Any
from numpy import ndarray
from _typeshed import Incomplete

TAU: Incomplete
BLACK: Incomplete
RED: Incomplete


def testdata_sifts():
    ...


def get_sift_collection(sift: Any,
                        aff: None = None,
                        bin_color: ndarray = BLACK,
                        arm1_color: ndarray = RED,
                        arm2_color: ndarray = BLACK,
                        arm_alpha: float = 1.0,
                        arm1_lw: float = 1.0,
                        arm2_lw: float = 2.0,
                        stroke: float = ...,
                        circ_alpha: float = 0.5,
                        fidelity: int = 256,
                        scaling: bool = ...,
                        **kwargs) -> Any:
    ...


def draw_sifts(ax,
               sifts,
               invVR_aff2Ds: Incomplete | None = ...,
               **kwargs) -> None:
    ...


def draw_sift_on_patch(patch, sift, **kwargs):
    ...


def render_sift_on_patch(patch, sift):
    ...
