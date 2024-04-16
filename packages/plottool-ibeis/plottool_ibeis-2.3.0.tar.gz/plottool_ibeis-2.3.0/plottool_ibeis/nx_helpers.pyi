import networkx
import dtool as dt
from _typeshed import Incomplete

print: Incomplete
rrr: Incomplete
profile: Incomplete
__docstubs__: str
LARGE_GRAPH: int


def dump_nx_ondisk(graph, fpath) -> None:
    ...


def ensure_nonhex_color(orig_color):
    ...


def show_nx(graph: networkx.Graph,
            with_labels: bool = True,
            fnum: int | None = None,
            pnum: tuple | None = None,
            layout: str = 'agraph',
            ax: None = None,
            pos: None = None,
            img_dict: dict | None = None,
            title: str | None = None,
            layoutkw: None = None,
            verbose: bool | None = None,
            **kwargs):
    ...


def netx_draw_images_at_positions(img_list, pos_list, size_list, color_list,
                                  framewidth_list) -> None:
    ...


def parse_html_graphviz_attrs():
    ...


class GRAPHVIZ_KEYS:
    N: Incomplete
    E: Incomplete
    G: Incomplete


class GraphVizLayoutConfig(dt.Config):

    @staticmethod
    def get_param_info_list():
        ...


def get_explicit_graph(graph):
    ...


def get_nx_layout(graph,
                  layout,
                  layoutkw: Incomplete | None = ...,
                  verbose: Incomplete | None = ...):
    ...


def apply_graph_layout_attrs(graph, layout_info):
    ...


def patch_pygraphviz():
    ...


def make_agraph(graph_):
    ...


def nx_agraph_layout(orig_graph,
                     inplace: bool = ...,
                     verbose: Incomplete | None = ...,
                     return_agraph: bool = ...,
                     groupby: str | None = None,
                     **layoutkw):
    ...


def parse_point(ptstr):
    ...


def parse_anode_layout_attrs(anode):
    ...


def parse_aedge_layout_attrs(aedge, translation: Incomplete | None = ...):
    ...


def format_anode_pos(xy, pin: bool = ...):
    ...


def draw_network2(graph,
                  layout_info,
                  ax,
                  as_directed: Incomplete | None = ...,
                  hacknoedge: bool = ...,
                  hacknode: bool = ...,
                  verbose: Incomplete | None = ...,
                  **kwargs):
    ...
