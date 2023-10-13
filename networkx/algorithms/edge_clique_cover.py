"""Find minimum edge clique cover."""

import networkx as nx
from networkx.utils import not_implemented_for

__all__ = ["minimum_edge_clique_cover", "intersection_number"]


def minimum_edge_clique_cover(G):
    """
    Find exact clique-minimum edge clique cover of simple undirected graph G.

    An *edge clique cover* (ECC) of a graph G is a collection of its cliques
    (fully connected subgraphs) whose union contains all edges in G. A
    *clique-minimum ECC* is and ECC with the minimum possible cliques. The
    cardinality of such an ECC is known as the *intersection number* of G.
    This implemenatation is based on [1]_, which has complexity
    :math:`O(f(2^k) + n^4)`, where :math:`k` is the number of cliques in the
    solution and :math:`n` is the number of nodes in G.

    Parameters
    ----------
    G : NetworkX graph
        G must be simple and undirected

    Returns
    -------
    the_cover: set of sets


    See Also
    --------
    intersection_number

    References
    ----------
    .. [1] Gramm, Jens, Jiong Guo, Falk Hüffner, and Rolf Niedermeier.
       "Data reduction and exact algorithms for clique cover."
       Journal of Experimental Algorithmics (JEA) 13 (2009): 2-2.
       https://doi.org/10.1145/1412228.1412236
    """
    return None


def intersection_number(G):
    """Compute intersection number of simple undirected graph G.

    See Also
    --------
    minimum_edge_clique_cover

    Returns
    -------
    int
    """
    return len(minimum_edge_clique_cover(G))
