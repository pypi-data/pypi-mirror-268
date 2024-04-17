import numpy as np
import scipy.sparse as sprs


# Once a function has been stripped of all its OpenPNM dependent code it
# can be added to this list of functions to import
__all__ = [
    'get_edge_prefix',
    'get_node_prefix',
    'change_prefix',
    'tri_to_am',
    'vor_to_am',
    'conns_to_am',
    'dict_to_am',
    'dict_to_im',
    'istriu',
    'istril',
    'isgtriu',
    'istriangular',
    'issymmetric',
]


def get_edge_prefix(network):
    r"""
    Determines the prefix used for edge arrays from ``<edge_prefix>.conns``

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    edge_prefix : str
        The value of ``<edge_prefix>`` used in ``g``.  This is found by
        scanning ``g.keys()`` until an array ending in ``'.conns'`` is found,
        then returning the prefix.

    Notes
    -----
    This process is surprizingly fast, on the order of nano seconds, so this
    overhead is worth it for the flexibility it provides in array naming.
    However, since all ``dict`` are now sorted in Python, it may be helpful
    to ensure the ``'conns'`` array is near the beginning of the list.
    """
    for item in network.keys():
        if item.endswith('.conns'):
            return item.split('.')[0]
    for group in network.keys():
        if 'conns' in network[group].keys():
            return group


def get_node_prefix(network):
    r"""
    Determines the prefix used for node arrays from ``<edge_prefix>.coords``

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    node_prefix : str
        The value of ``<node_prefix>`` used in ``g``.  This is found by
        scanning ``g.keys()`` until an array ending in ``'.coords'`` is found,
        then returning the prefix.

    Notes
    -----
    This process is surprizingly fast, on the order of nano seconds, so this
    overhead is worth it for the flexibility it provides in array naming.
    However, since all ``dict`` are now sorted in Python, it may be helpful
    to ensure the ``'conns'`` array is near the beginning of the list.
    """
    for item in network.keys():
        if item.endswith('.coords'):
            return item.split('.')[0]
    for group in network.keys():
        if 'coords' in network[group].keys():
            return group


def change_prefix(network, old_prefix, new_prefix):
    r"""
    Changes the prefix used when generating the graph

    Parameters
    ----------
    network : dict
        The network graph
    old_prefix : str
        The current prefix to change, can either be a node or an edge prefix
    new_prefix : str
        The prefix to use instead

    Returns
    -------
    network : dict
        The graph dictionary will arrays assigned to new keys
    """
    for key in list(network.keys()):
        if key.startswith(old_prefix):
            temp = key.split('.', 1)[1]
            network[new_prefix + '.' + temp] = network.pop(key)
    return network


def tri_to_am(tri):
    r"""
    Given a Delaunay triangulation object from Scipy's ``spatial`` module,
    converts to a sparse adjacency matrix network representation.

    Parameters
    ----------
    tri : Delaunay Triangulation Object
        This object is produced by ``scipy.spatial.Delaunay``

    Returns
    -------
    A sparse adjacency matrix in COO format.  The network is undirected
    and unweighted, so the adjacency matrix is upper-triangular and all the
    weights are set to 1.

    """
    # Create an empty list-of-list matrix
    lil = sprs.lil_matrix((tri.npoints, tri.npoints))
    # Scan through Delaunay triangulation object to retrieve pairs
    indices, indptr = tri.vertex_neighbor_vertices
    for k in range(tri.npoints):
        lil.rows[k] = indptr[indices[k]:indices[k + 1]].tolist()
    # Convert to coo format
    lil.data = lil.rows  # Just a dummy array to make things work properly
    coo = lil.tocoo()
    # Set weights to 1's
    coo.data = np.ones_like(coo.data)
    # Remove diagonal, and convert to csr remove duplicates
    am = sprs.triu(A=coo, k=1, format='csr')
    # The convert back to COO and return
    am = am.tocoo()
    return am


def vor_to_am(vor):
    r"""
    Given a Voronoi tessellation object from Scipy's ``spatial`` module,
    converts to a sparse adjacency matrix network representation in COO format.

    Parameters
    ----------
    vor : Voronoi Tessellation object
        This object is produced by ``scipy.spatial.Voronoi``

    Returns
    -------
    A sparse adjacency matrix in COO format.  The network is undirected
    and unweighted, so the adjacency matrix is upper-triangular and all the
    weights are set to 1.

    """
    # Create adjacency matrix in lil format for quick matrix construction
    N = vor.vertices.shape[0]
    rc = [[], []]
    for ij in vor.ridge_dict.keys():
        row = vor.ridge_dict[ij].copy()
        # Make sure voronoi cell closes upon itself
        row.append(row[0])
        # Add connections to rc list
        rc[0].extend(row[:-1])
        rc[1].extend(row[1:])
    rc = np.vstack(rc).T
    # Make adj mat upper triangular
    rc = np.sort(rc, axis=1)
    # Remove any pairs with ends at infinity (-1)
    keep = ~np.any(rc == -1, axis=1)
    rc = rc[keep]
    data = np.ones_like(rc[:, 0])
    # Build adj mat in COO format
    M = N = np.amax(rc) + 1
    am = sprs.coo_matrix((data, (rc[:, 0], rc[:, 1])), shape=(M, N))
    # Remove diagonal, and convert to csr remove duplicates
    am = sprs.triu(A=am, k=1, format='csr')
    # The convert back to COO and return
    am = am.tocoo()
    return am


def dict_to_am(network, weights=None):
    r"""
    Convert a graph dictionary into a ``scipy.sparse`` adjacency matrix in
    COO format

    Parameters
    ----------
    network : dict
        A network dictionary
    weights : ndarray, optional
        The weight values to use for the connections. If not provided
        then 1's are assumed.

    Returns
    -------
    am : sparse matrix
        The sparse adjacency matrix in COO format

    Notes
    -----
    If the edge connections in ``g`` are in upper-triangular form, then the
    graph is assumed to be undirected and the returned adjacency matrix is
    symmetrical (i.e. the triu entries are reflected in tril). If any edges
    are found in the lower triangle, then the returned adjacency matrix is
    unsymmetrical.

    Multigraphs (i.e. duplicate connections between nodes) are not suported,
    but this is not checked for here to avoid overhead since this function is
    called frequently.

    """
    edge_prefix = get_edge_prefix(network)
    node_prefix = get_node_prefix(network)
    conns = np.copy(network[edge_prefix+'.conns'])
    shape = [network[node_prefix+'.coords'].shape[0]]*2
    if weights is None:
        weights = np.ones_like(conns[:, 0], dtype=int)
    if isgtriu(network):  # If graph is triu, then it is assumed to be undirected
        conns = np.vstack((conns, np.fliplr(conns)))  # Reflect to tril
        data = np.ones_like(conns[:, 0], dtype=int)  # Generate fake data
        am = sprs.coo_matrix((data, (conns[:, 0], conns[:, 1])), shape=shape)
        am.data = np.hstack((weights, weights))
    else:
        am = sprs.coo_matrix((weights, (conns[:, 0], conns[:, 1])), shape=shape)
    return am


def dict_to_im(network):
    r"""
    Convert a graph dictionary into a ``scipy.sparse`` incidence matrix in COO
    format

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    im : sparse matrix
        The sparse incidence matrix in COO format

    Notes
    -----
    Rows correspond to nodes and columns correspond to edges. Each column
    has 2 nonzero values indicating which 2 nodes are connected by the
    corresponding edge. Each row contains an arbitrary number of nonzeros
    whose locations indicate which edges are directly connected to the
    corresponding node.
    """
    edge_prefix = get_edge_prefix(network)
    node_prefix = get_node_prefix(network)
    conns = network[edge_prefix+'.conns']
    coords = network[node_prefix+'.coords']
    if isgtriu(network):
        data = np.ones(2*conns.shape[0], dtype=int)
        shape = (coords.shape[0], conns.shape[0])
        temp = np.arange(conns.shape[0])
        cols = np.vstack((temp, temp)).T.flatten()
        rows = conns.flatten()
        im = sprs.coo_matrix((data, (rows, cols)), shape=shape)
    else:
        raise Exception('This function is not implemented for directed graphs')
    return im


def ismultigraph(network):
    r"""
    Checks if graph contains multiple connections between any pair of nodes

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    flag : bool
        Returns ``True`` if any pair of nodes is connected by more than one
        edge.
    """
    edge_prefix = get_edge_prefix(network)
    node_prefix = get_node_prefix(network)
    conns = network[edge_prefix+'.conns']
    coords = network[node_prefix+'.coords']
    data = np.ones_like(conns[:, 0], dtype=int)
    shape = 2*[coords.shape[0]]
    am = sprs.coo_matrix((data, (conns[:, 0], conns[:, 1])), shape=shape)
    am.sum_duplicates()
    return np.any(am.data > 1)


def isgtriu(network):
    r"""
    Determines if graph connections are in upper triangular format

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    flag : bool
        Returns ``True`` if *all* rows in "conns" are ordered as [lo, hi]
    """
    edge_prefix = get_edge_prefix(network)
    conns = network[edge_prefix+'.conns']
    return np.all(conns[:, 0] < conns[:, 1])


def to_triu(network):
    r"""
    Adjusts conns array to force into upper triangular form

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    network : dict
        The graph dictionary with edge connections updated

    Notes
    -----
    This does not check for the creation of duplicate connections
    """
    edge_prefix = get_edge_prefix(network)
    conns = network[edge_prefix+'.conns']
    network[edge_prefix+'.conns'] = np.sort(conns, axis=1)
    return network


def conns_to_am(conns, shape=None, force_triu=True, drop_diag=True,
                drop_dupes=True, drop_negs=True):
    r"""
    Converts a list of connections into a Scipy sparse adjacency matrix

    Parameters
    ----------
    conns : array_like, N x 2
        The list of site-to-site connections
    shape : list, optional
        The shape of the array.  If none is given then it is taken as 1 + the
        maximum value in ``conns``.
    force_triu : bool
        If True (default), then all connections are assumed undirected, and
        moved to the upper triangular portion of the array
    drop_diag : bool
        If True (default), then connections from a site and itself are removed.
    drop_dupes : bool
        If True (default), then all pairs of sites sharing multiple connections
        are reduced to a single connection.
    drop_negs : bool
        If True (default), then all connections with one or both ends pointing
        to a negative number are removed.

    Returns
    -------
    am : ndarray
        A sparse adjacency matrix in COO format

    """
    if force_triu:  # Sort connections to [low, high]
        conns = np.sort(conns, axis=1)
    if drop_negs:  # Remove connections to -1
        keep = ~np.any(conns < 0, axis=1)
        conns = conns[keep]
    if drop_diag:  # Remove connections of [self, self]
        keep = np.where(conns[:, 0] != conns[:, 1])[0]
        conns = conns[keep]
    # Now convert to actual sparse array in COO format
    data = np.ones_like(conns[:, 0], dtype=int)
    if shape is None:
        N = conns.max() + 1
        shape = (N, N)
    am = sprs.coo_matrix((data, (conns[:, 0], conns[:, 1])), shape=shape)
    if drop_dupes:  # Convert to csr and back too coo
        am = am.tocsr()
        am = am.tocoo()
    # Perform one last check on adjacency matrix
    missing = np.where(np.bincount(conns.flatten()) == 0)[0]
    if np.size(missing) or np.any(am.col.max() < (shape[0] - 1)):
        print('Some nodes are not connected to any bonds')
    return am


def istriu(am):
    r"""
    Returns ``True`` if the sparse adjacency matrix is upper triangular
    """
    if am.shape[0] != am.shape[1]:
        print('Matrix is not square, triangularity is irrelevant')
        return False
    if am.format != 'coo':
        am = am.tocoo(copy=False)
    return np.all(am.row <= am.col)


def istril(am):
    r"""
    Returns ``True`` if the sparse adjacency matrix is lower triangular
    """
    if am.shape[0] != am.shape[1]:
        print('Matrix is not square, triangularity is irrelevant')
        return False
    if am.format != 'coo':
        am = am.tocoo(copy=False)
    return np.all(am.row >= am.col)


def istriangular(am):
    r"""
    Returns ``True`` if the sparse adjacency matrix is either upper or lower
    triangular
    """
    if am.format != 'coo':
        am = am.tocoo(copy=False)
    return istril(am) or istriu(am)


def issymmetric(am):
    r"""
    A method to check if a square matrix is symmetric
    Returns ``True`` if the sparse adjacency matrix is symmetric
    """
    if am.shape[0] != am.shape[1]:
        print('Matrix is not square, symmetrical is irrelevant')
        return False
    if am.format != 'coo':
        am = am.tocoo(copy=False)
    if istril(am) or istriu(am):
        return False
    # Compare am with its transpose, element wise
    sym = ((am != am.T).size) == 0
    return sym
