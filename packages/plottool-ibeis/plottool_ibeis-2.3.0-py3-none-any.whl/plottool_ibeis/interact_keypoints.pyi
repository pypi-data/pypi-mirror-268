from _typeshed import Incomplete
from plottool_ibeis import abstract_interaction

print: Incomplete
rrr: Incomplete
profile: Incomplete


class KeypointInteraction(abstract_interaction.AbstractInteraction):
    chip: Incomplete
    kpts: Incomplete
    vecs: Incomplete
    figtitle: Incomplete
    mode: int

    def __init__(self,
                 chip,
                 kpts,
                 vecs,
                 fnum: int = ...,
                 figtitle: Incomplete | None = ...,
                 **kwargs) -> None:
        ...

    def plot(self, fnum: Incomplete | None = ..., pnum=..., **kwargs) -> None:
        ...

    def on_click_outside(self, event) -> None:
        ...

    def on_click_inside(self, event, ax) -> None:
        ...


def ishow_keypoints(chip,
                    kpts,
                    desc,
                    fnum: int = ...,
                    figtitle: Incomplete | None = ...,
                    nodraw: bool = ...,
                    **kwargs) -> None:
    ...
