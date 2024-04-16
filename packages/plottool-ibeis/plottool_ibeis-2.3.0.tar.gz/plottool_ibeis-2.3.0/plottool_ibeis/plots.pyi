from numpy import ndarray
from typing import List
from typing import Any
import matplotlib as mpl
from _typeshed import Incomplete

print: Incomplete
rrr: Incomplete
profile: Incomplete
__docstubs__: str


def is_default_dark_bg():
    ...


def multi_plot(xdata: ndarray | None = None,
               ydata_list: List[ndarray] = ...,
               **kwargs):
    ...


def demo_fonts() -> None:
    ...


def plot_multiple_scores(known_nd_data,
                         known_target_points,
                         nd_labels,
                         target_label,
                         title: Incomplete | None = ...,
                         use_legend: bool = ...,
                         color_list: Incomplete | None = ...,
                         marker_list: Incomplete | None = ...,
                         report_max: bool = ...,
                         **kwargs):
    ...


def plot_rank_cumhist(cdf_list,
                      label_list,
                      color_list: Incomplete | None = ...,
                      marker_list: Incomplete | None = ...,
                      edges: Incomplete | None = ...,
                      xlabel: str = ...,
                      ylabel: str = ...,
                      use_legend: bool = ...,
                      num_xticks: Incomplete | None = ...,
                      kind: str = ...,
                      **kwargs):
    ...


def draw_hist_subbin_maxima(hist: ndarray,
                            centers: Any | None = None,
                            bin_colors: Incomplete | None = ...,
                            maxima_thresh: Incomplete | None = ...,
                            remove_endpoints: bool = ...,
                            **kwargs) -> None:
    ...


def draw_subextrema(ydata: ndarray,
                    xdata: Any | None = None,
                    op: str = ...,
                    bin_colors: Incomplete | None = ...,
                    thresh_factor: Incomplete | None = ...,
                    normalize_x: bool = ...,
                    flat: bool = ...) -> None:
    ...


def zoom_effect01(ax1: mpl.axes.Axes, ax2: mpl.axes.Axes, xmin: float,
                  xmax: float, **kwargs) -> tuple:
    ...


def colorline(x,
              y,
              z: Incomplete | None = ...,
              cmap=...,
              norm=...,
              linewidth: int = ...,
              alpha: float = ...):
    ...


def plot_stems(x_data,
               y_data,
               fnum: Incomplete | None = ...,
               pnum=...,
               **kwargs) -> None:
    ...


def plot_score_histograms(scores_list,
                          score_lbls: Incomplete | None = ...,
                          score_markers: Incomplete | None = ...,
                          score_colors: Incomplete | None = ...,
                          markersizes: Incomplete | None = ...,
                          fnum: Incomplete | None = ...,
                          pnum=...,
                          title: Incomplete | None = ...,
                          score_label: str = ...,
                          score_thresh: Incomplete | None = ...,
                          overlay_prob_given_list: Incomplete | None = ...,
                          overlay_score_domain: Incomplete | None = ...,
                          logscale: bool = ...,
                          histnorm: bool = ...,
                          **kwargs):
    ...


def plot_probabilities(prob_list: list,
                       prob_lbls: Any | None = None,
                       prob_colors: Any | None = None,
                       xdata: Any | None = None,
                       prob_thresh: Any | None = None,
                       score_thresh: Incomplete | None = ...,
                       figtitle: str = 'plot_probabilities',
                       fnum: int | None = None,
                       pnum: tuple | str | None = ...,
                       fill: bool = False,
                       **kwargs) -> None:
    ...


plot_probs = plot_probabilities
plot_densities = plot_probabilities


def plot_sorted_scores(scores_list: list,
                       score_lbls: Any | None = None,
                       score_markers: Any | None = None,
                       score_colors: Any | None = None,
                       markersizes: Any | None = None,
                       fnum: int | None = None,
                       pnum: tuple = ...,
                       logscale: bool = True,
                       figtitle: str | None = None,
                       score_label: str = ...,
                       thresh: Incomplete | None = ...,
                       use_stems: Incomplete | None = ...,
                       **kwargs) -> None:
    ...


def set_logyscale_from_data(y_data) -> None:
    ...


def get_good_logyscale_kwargs(y_data, adaptive_knee_scaling: bool = ...):
    ...


def plot_pdf(data,
             draw_support: bool = ...,
             scale_to: Incomplete | None = ...,
             label: Incomplete | None = ...,
             color: int = ...,
             nYTicks: int = ...) -> None:
    ...


def estimate_pdf(data, bw_factor):
    ...


def interval_stats_plot(param2_stat_dict,
                        fnum: int | None = None,
                        pnum: tuple = ...,
                        x_label: str = ...,
                        y_label: str = ...,
                        title: str = ...):
    ...


def interval_line_plot(xdata: ndarray,
                       ydata_mean: ndarray,
                       y_data_std: ndarray,
                       color=...,
                       label: Incomplete | None = ...,
                       marker: str = ...,
                       linestyle: str = ...) -> None:
    ...


def plot_search_surface(known_nd_data: Any,
                        known_target_points: Any,
                        nd_labels: Any,
                        target_label: Any,
                        fnum: int | None = None,
                        pnum: Incomplete | None = ...,
                        title: Incomplete | None = ...) -> mpl.axes.Axes:
    ...


def draw_timedelta_pie(timedeltas: list,
                       bins: None = None,
                       fnum: Incomplete | None = ...,
                       pnum=...,
                       label: str = ...) -> None:
    ...


def word_histogram2(text_list: list,
                    weight_list: Incomplete | None = ...,
                    **kwargs) -> None:
    ...


def draw_time_histogram(unixtime_list, **kwargs) -> None:
    ...


def draw_histogram(bin_labels: Any,
                   bin_values: Any,
                   xlabel: str = '',
                   ylabel: str = 'Freq',
                   xtick_rotation: int = 0,
                   transpose: bool = False,
                   **kwargs) -> None:
    ...


def draw_time_distribution(unixtime_list, bw: Incomplete | None = ...) -> None:
    ...


def wordcloud(text: str | dict,
              size: Incomplete | None = ...,
              fnum: int | None = None,
              pnum: tuple | None = None,
              ax: Incomplete | None = ...) -> None:
    ...
