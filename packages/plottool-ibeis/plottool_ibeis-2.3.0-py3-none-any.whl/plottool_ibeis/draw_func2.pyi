from numpy import ndarray
import matplotlib as mpl
from typing import Callable
from typing import Any
from typing import List
from _typeshed import Incomplete
from collections.abc import Generator

DEBUG: bool
print: Incomplete
rrr: Incomplete
profile: Incomplete


def __getattr__(key):
    ...


def is_texmode():
    ...


TAU: Incomplete
distinct_colors: Incomplete
lighten_rgb: Incomplete
to_base255: Incomplete
DARKEN: Incomplete
all_figures_bring_to_front: Incomplete
all_figures_tile: Incomplete
close_all_figures: Incomplete
close_figure: Incomplete
iup: Incomplete
iupdate: Incomplete
present: Incomplete
reset: Incomplete
update: Incomplete
ORANGE: Incomplete
RED: Incomplete
GREEN: Incomplete
BLUE: Incomplete
YELLOW: Incomplete
BLACK: Incomplete
WHITE: Incomplete
GRAY: Incomplete
LIGHTGRAY: Incomplete
DEEP_PINK: Incomplete
PINK: Incomplete
FALSE_RED: Incomplete
TRUE_GREEN: Incomplete
TRUE_BLUE: Incomplete
DARK_GREEN: Incomplete
DARK_BLUE: Incomplete
DARK_RED: Incomplete
DARK_ORANGE: Incomplete
DARK_YELLOW: Incomplete
PURPLE: Incomplete
LIGHT_BLUE: Incomplete
UNKNOWN_PURP: Incomplete
TRUE = TRUE_BLUE
FALSE = FALSE_RED
figure: Incomplete
gca: Incomplete
gcf: Incomplete
get_fig: Incomplete
save_figure: Incomplete
set_figtitle: Incomplete
set_title: Incomplete
set_xlabel: Incomplete
set_xticks: Incomplete
set_ylabel: Incomplete
set_yticks: Incomplete
VERBOSE: Incomplete
TMP_mevent: Incomplete
plotWidget: Incomplete


def show_was_requested():
    ...


class OffsetImage2(mpl.offsetbox.OffsetBox):
    image: Incomplete

    def __init__(self,
                 arr,
                 zoom: int = ...,
                 cmap: Incomplete | None = ...,
                 norm: Incomplete | None = ...,
                 interpolation: Incomplete | None = ...,
                 origin: Incomplete | None = ...,
                 filternorm: int = ...,
                 filterrad: float = ...,
                 resample: bool = ...,
                 dpi_cor: bool = ...,
                 **kwargs) -> None:
        ...

    stale: bool

    def set_data(self, arr) -> None:
        ...

    def get_data(self):
        ...

    def set_zoom(self, zoom) -> None:
        ...

    def get_zoom(self):
        ...

    def get_offset(self):
        ...

    def get_children(self):
        ...

    def get_window_extent(self, renderer):
        ...

    def get_extent(self, renderer):
        ...

    def draw(self, renderer) -> None:
        ...


def overlay_icon(icon: ndarray | str,
                 coords: tuple = ...,
                 coord_type: str = 'axes',
                 bbox_alignment: tuple = ...,
                 max_asize: Incomplete | None = ...,
                 max_dsize: None = None,
                 as_artist: bool = ...) -> None:
    ...


def update_figsize() -> None:
    ...


def udpate_adjust_subplots() -> None:
    ...


def render_figure_to_image(fig, **savekw):
    ...


class RenderingContext:
    image: Incomplete
    fig: Incomplete
    was_interactive: Incomplete
    savekw: Incomplete

    def __init__(self, **savekw) -> None:
        ...

    def __enter__(self):
        ...

    def __exit__(self, type_, value, trace):
        ...


def extract_axes_extents(fig, combine: bool = ..., pad: float = ...):
    ...


def axes_extent(axs, pad: float = ...):
    ...


def save_parts(fig: mpl.figure.Figure,
               fpath: str,
               grouped_axes: Incomplete | None = ...,
               dpi: None = None) -> list:
    ...


def quit_if_noshow() -> None:
    ...


def show_if_requested(N: int = ...):
    ...


def distinct_markers(num: int,
                     style: str = ...,
                     total: Incomplete | None = ...,
                     offset: int = ...):
    ...


def get_all_markers():
    ...


def get_pnum_func(nRows: int = ..., nCols: int = ..., base: int = ...):
    ...


def pnum_generator(nRows: int = 1,
                   nCols: int = 1,
                   base: int = 0,
                   nSubplots: None = None,
                   start: int = ...) -> Generator[tuple, None, None]:
    ...


def make_pnum_nextgen(nRows: None = None,
                      nCols: None = None,
                      base: int = 0,
                      nSubplots: None = None,
                      start: int = 0) -> Callable:
    ...


def get_num_rc(nSubplots: None = None,
               nRows: None = None,
               nCols: None = None) -> tuple:
    ...


def fnum_generator(base: int = ...) -> Generator[Any, None, None]:
    ...


def make_fnum_nextgen(base: int = ...):
    ...


BASE_FNUM: int


def next_fnum(new_base: Incomplete | None = ...):
    ...


def ensure_fnum(fnum):
    ...


def execstr_global():
    ...


def label_to_colors(labels_):
    ...


def add_alpha(colors):
    ...


def get_axis_xy_width_height(ax: Incomplete | None = ...,
                             xaug: int = ...,
                             yaug: int = ...,
                             waug: int = ...,
                             haug: int = ...):
    ...


def get_axis_bbox(ax: Incomplete | None = ..., **kwargs):
    ...


def draw_border(ax,
                color=...,
                lw: int = ...,
                offset: Incomplete | None = ...,
                adjust: bool = ...):
    ...


def rotate_plot(theta: Any = ..., ax: None = None) -> None:
    ...


def cartoon_stacked_rects(xy,
                          width,
                          height,
                          num: int = ...,
                          shift: Incomplete | None = ...,
                          **kwargs):
    ...


def make_bbox(bbox,
              theta: int = ...,
              bbox_color: Incomplete | None = ...,
              ax: Incomplete | None = ...,
              lw: int = ...,
              alpha: float = ...,
              align: str = ...,
              fill: Incomplete | None = ...,
              **kwargs):
    ...


def draw_bbox(bbox,
              lbl: Incomplete | None = ...,
              bbox_color=...,
              lbl_bgcolor=...,
              lbl_txtcolor=...,
              draw_arrow: bool = ...,
              theta: int = ...,
              ax: Incomplete | None = ...,
              lw: int = ...) -> None:
    ...


def plot(*args, **kwargs):
    ...


def plot2(x_data,
          y_data,
          marker: str = ...,
          title_pref: str = ...,
          x_label: str = ...,
          y_label: str = ...,
          unitbox: bool = ...,
          flipx: bool = ...,
          flipy: bool = ...,
          title: Incomplete | None = ...,
          dark: Incomplete | None = ...,
          equal_aspect: bool = ...,
          pad: int = ...,
          label: str = ...,
          fnum: Incomplete | None = ...,
          pnum: Incomplete | None = ...,
          *args,
          **kwargs) -> None:
    ...


def pad_axes(pad,
             xlim: Incomplete | None = ...,
             ylim: Incomplete | None = ...) -> None:
    ...


def presetup_axes(x_label: str = ...,
                  y_label: str = ...,
                  title_pref: str = ...,
                  title: Incomplete | None = ...,
                  equal_aspect: bool = ...,
                  ax: Incomplete | None = ...,
                  **kwargs) -> None:
    ...


def postsetup_axes(use_legend: bool = ...,
                   bg: Incomplete | None = ...) -> None:
    ...


def adjust_subplots(left: Incomplete | None = ...,
                    right: Incomplete | None = ...,
                    bottom: Incomplete | None = ...,
                    top: Incomplete | None = ...,
                    wspace: Incomplete | None = ...,
                    hspace: Incomplete | None = ...,
                    use_argv: bool = ...,
                    fig: Incomplete | None = ...) -> None:
    ...


def upperleft_text(txt,
                   alpha: float = ...,
                   color: Incomplete | None = ...) -> None:
    ...


def upperright_text(txt,
                    offset: Incomplete | None = ...,
                    alpha: float = ...) -> None:
    ...


def lowerright_text(txt) -> None:
    ...


def absolute_lbl(x_,
                 y_,
                 txt,
                 roffset=...,
                 alpha: float = ...,
                 **kwargs) -> None:
    ...


def absolute_text(pos, text, ax: Incomplete | None = ..., **kwargs) -> None:
    ...


def relative_text(pos: tuple,
                  text: str,
                  ax: None = None,
                  offset: None = None,
                  **kwargs) -> None:
    ...


def parse_fontkw(**kwargs):
    ...


def ax_absolute_text(x_,
                     y_,
                     txt,
                     ax: Incomplete | None = ...,
                     roffset: Incomplete | None = ...,
                     **kwargs):
    ...


def fig_relative_text(x, y, txt, **kwargs) -> None:
    ...


def draw_text(text_str, rgb_textFG=..., rgb_textBG=...) -> None:
    ...


def show_histogram(data, bins: Incomplete | None = ..., **kwargs):
    ...


def show_signature(sig, **kwargs) -> None:
    ...


def draw_stems(x_data: None = None,
               y_data: None = None,
               setlims: bool = True,
               color: None = None,
               markersize: None = None,
               bottom: None = None,
               marker: Incomplete | None = ...,
               linestyle: str = ...) -> None:
    ...


def plot_sift_signature(
        sift: ndarray,
        title: str = '',
        fnum: int | None = None,
        pnum: tuple | str | int | None = None) -> mpl.axes.AxesSubplot:
    ...


def plot_descriptor_signature(
        vec: ndarray,
        title: str = '',
        fnum: int | None = None,
        pnum: tuple | None = None) -> mpl.axes.AxesSubplot:
    ...


def dark_background(ax: None = None,
                    doubleit: bool = False,
                    force: bool = ...):
    ...


def space_xticks(nTicks: int = ...,
                 spacing: int = ...,
                 ax: Incomplete | None = ...) -> None:
    ...


def space_yticks(nTicks: int = ...,
                 spacing: int = ...,
                 ax: Incomplete | None = ...) -> None:
    ...


def small_xticks(ax: Incomplete | None = ...) -> None:
    ...


def small_yticks(ax: Incomplete | None = ...) -> None:
    ...


def plot_bars(y_data, nColorSplits: int = ...) -> None:
    ...


def append_phantom_legend_label(label: Any,
                                color: Any,
                                type_: str = ...,
                                alpha: float = ...,
                                ax: Incomplete | None = ...) -> None:
    ...


def show_phantom_legend_labels(ax: Incomplete | None = ..., **kwargs) -> None:
    ...


LEGEND_LOCATION: Incomplete


def legend(loc: str = 'best',
           fontproperties: None = None,
           size: None = None,
           fc: str = ...,
           alpha: int = ...,
           ax: Incomplete | None = ...,
           handles: Incomplete | None = ...) -> None:
    ...


def plot_histpdf(data,
                 label: Incomplete | None = ...,
                 draw_support: bool = ...,
                 nbins: int = ...) -> None:
    ...


def plot_hist(data,
              bins: Incomplete | None = ...,
              nbins: int = ...,
              weights: Incomplete | None = ...):
    ...


def variation_trunctate(data) -> None:
    ...


def scores_to_color(score_list: list,
                    cmap_: str = 'hot',
                    logscale: bool = False,
                    reverse_cmap: bool = ...,
                    custom: bool = ...,
                    val2_customcolor: Incomplete | None = ...,
                    score_range: Incomplete | None = ...,
                    cmap_range: tuple = ...) -> list:
    ...


def customize_colormap(data, base_colormap):
    ...


def unique_rows(arr):
    ...


def scores_to_cmap(scores, colors: Incomplete | None = ..., cmap_: str = ...):
    ...


DF2_DIVIDER_KEY: str


def ensure_divider(ax):
    ...


def get_binary_svm_cmap():
    ...


def reverse_colormap(cmap):
    ...


def interpolated_colormap(color_frac_list,
                          resolution: int = ...,
                          space: str = ...):
    ...


def print_valid_cmaps() -> None:
    ...


def colorbar(scalars: ndarray,
             colors: ndarray,
             custom: bool = False,
             lbl: Incomplete | None = ...,
             ticklabels: Incomplete | None = ...,
             float_format: str = ...,
             **kwargs) -> mpl.colorbar.Colorbar:
    ...


def draw_lines2(kpts1,
                kpts2,
                fm: Incomplete | None = ...,
                fs: Incomplete | None = ...,
                kpts2_offset=...,
                color_list: Incomplete | None = ...,
                scale_factor: int = ...,
                lw: float = ...,
                line_alpha: float = ...,
                H1: Incomplete | None = ...,
                H2: Incomplete | None = ...,
                scale_factor1: Incomplete | None = ...,
                scale_factor2: Incomplete | None = ...,
                ax: Incomplete | None = ...,
                **kwargs) -> None:
    ...


def draw_line_segments2(pts1: ndarray,
                        pts2: ndarray,
                        ax: None = None,
                        **kwargs) -> None:
    ...


def draw_line_segments(segments_list, **kwargs) -> None:
    ...


def draw_patches_and_sifts(patch_list,
                           sift_list,
                           fnum: Incomplete | None = ...,
                           pnum=...):
    ...


def show_kpts(kpts: ndarray,
              fnum: Incomplete | None = ...,
              pnum: Incomplete | None = ...,
              **kwargs) -> None:
    ...


def set_axis_extent(extents, ax: Incomplete | None = ...) -> None:
    ...


def set_axis_limit(xmin, xmax, ymin, ymax, ax: Incomplete | None = ...):
    ...


def draw_kpts2(kpts: ndarray,
               offset: tuple = ...,
               scale_factor: int = 1,
               ell: bool = True,
               pts: bool = False,
               rect: bool = False,
               eig: bool = False,
               ori: bool = False,
               pts_size: int = 2,
               ell_alpha: float = 0.6,
               ell_linewidth: float = 1.5,
               ell_color: None = None,
               pts_color: ndarray = ORANGE,
               color_list: list | None = None,
               pts_alpha: float = ...,
               siftkw=...,
               H: Incomplete | None = ...,
               weights: Incomplete | None = ...,
               cmap_: str = ...,
               ax: Incomplete | None = ...,
               **kwargs):
    ...


def draw_keypoint_gradient_orientations(rchip,
                                        kpt,
                                        sift: Incomplete | None = ...,
                                        mode: str = ...,
                                        kptkw=...,
                                        siftkw=...,
                                        **kwargs):
    ...


def draw_keypoint_patch(rchip: ndarray,
                        kp: ndarray,
                        sift: Any | None = None,
                        warped: bool = False,
                        patch_dict: dict = ...,
                        **kwargs) -> mpl.axes.Axes:
    ...


def imshow(img: ndarray,
           fnum: int | None = None,
           title: str | None = None,
           figtitle: None = None,
           pnum: tuple | str | int | None = None,
           interpolation: str = 'nearest',
           cmap: None = None,
           heatmap: bool = False,
           data_colorbar: bool = False,
           darken: None = DARKEN,
           update: bool = False,
           xlabel: Incomplete | None = ...,
           redraw_image: bool = True,
           ax: Incomplete | None = ...,
           alpha: Incomplete | None = ...,
           norm: Incomplete | None = ...,
           **kwargs) -> tuple:
    ...


def draw_vector_field(gx,
                      gy,
                      fnum: Incomplete | None = ...,
                      pnum: Incomplete | None = ...,
                      title: Incomplete | None = ...,
                      invert: bool = ...,
                      stride: int = ...):
    ...


def show_chipmatch2(rchip1: ndarray,
                    rchip2: ndarray,
                    kpts1: ndarray | None = None,
                    kpts2: ndarray | None = None,
                    fm: list | None = None,
                    fs: list | None = None,
                    fm_norm: None = None,
                    title: str | None = None,
                    vert: None = None,
                    fnum: int | None = None,
                    pnum: tuple | str | int | None = None,
                    heatmap: bool = False,
                    modifysize: bool = False,
                    new_return: bool = False,
                    draw_fmatch: bool = True,
                    darken: float | None = DARKEN,
                    H1: ndarray | None = None,
                    H2: ndarray | None = None,
                    sel_fm: list = ...,
                    ax: mpl.axes.Axes | None = None,
                    heatmask: bool = False,
                    white_background: bool = ...,
                    **kwargs) -> tuple:
    ...


def plot_fmatch(xywh1: tuple,
                xywh2: tuple,
                kpts1: ndarray,
                kpts2: ndarray,
                fm: list,
                fs: list | None = None,
                fm_norm: None = None,
                lbl1: None = None,
                lbl2: None = None,
                fnum: None = None,
                pnum: None | tuple | str | int = None,
                rect: bool = False,
                colorbar_: bool = True,
                draw_border: bool = False,
                cmap: None = None,
                H1: None = None,
                H2: None = None,
                scale_factor1: None = None,
                scale_factor2: None = None,
                ax: Incomplete | None = ...,
                **kwargs) -> None:
    ...


def draw_boxedX(xywh: Incomplete | None = ...,
                color=...,
                lw: int = ...,
                alpha: float = ...,
                theta: int = ...,
                ax: Incomplete | None = ...) -> None:
    ...


def color_orimag(gori: ndarray,
                 gmag: ndarray | None = None,
                 gmag_is_01: bool | None = None,
                 encoding: str = ...,
                 p: float = 0.5) -> ndarray:
    ...


def get_orientation_color(radians_list: list):
    ...


def color_orimag_colorbar(gori) -> None:
    ...


def make_ori_legend_img():
    ...


def remove_patches(ax: Incomplete | None = ...) -> None:
    ...


def imshow_null(msg: None = None, ax: None = None, **kwargs) -> None:
    ...


def axes_bottom_button_bar(ax, text_list=...):
    ...


def make_bbox_positioners(y: float = ...,
                          w: float = ...,
                          h: float = ...,
                          xpad: float = ...,
                          startx: int = ...,
                          stopx: int = ...):
    ...


def width_from(num, pad: float = ..., start: int = ..., stop: int = ...):
    ...


def param_plot_iterator(
        param_list,
        fnum: Incomplete | None = ...,
        projection: Incomplete | None = ...) -> Generator[Any, None, None]:
    ...


def plot_surface3d(xgrid,
                   ygrid,
                   zdata,
                   xlabel: Incomplete | None = ...,
                   ylabel: Incomplete | None = ...,
                   zlabel: Incomplete | None = ...,
                   wire: bool = ...,
                   mode: Incomplete | None = ...,
                   contour: bool = ...,
                   dark: bool = ...,
                   rstride: int = ...,
                   cstride: int = ...,
                   pnum: Incomplete | None = ...,
                   labelkw: Incomplete | None = ...,
                   xlabelkw: Incomplete | None = ...,
                   ylabelkw: Incomplete | None = ...,
                   zlabelkw: Incomplete | None = ...,
                   titlekw: Incomplete | None = ...,
                   *args,
                   **kwargs):
    ...


def draw_text_annotations(text_list,
                          pos_list,
                          bbox_offset_list=...,
                          pos_offset_list=...,
                          bbox_align_list=...,
                          color_list: Incomplete | None = ...,
                          textprops=...):
    ...


def set_figsize(w, h, dpi) -> None:
    ...


def plot_func(funcs: List[Callable],
              start: int = 0,
              stop: int = 1,
              num: int = 100,
              setup: Incomplete | None = ...,
              fnum: Incomplete | None = ...,
              pnum: Incomplete | None = ...) -> None:
    ...


def test_save():
    ...
