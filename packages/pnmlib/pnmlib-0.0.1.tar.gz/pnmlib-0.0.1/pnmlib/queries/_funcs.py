import numpy as np
import scipy.spatial as sptl
import scipy.sparse as sprs
from scipy.sparse import csgraph
from scipy.spatial import Delaunay
from pnmlib.tools import conns_to_am, dict_to_am, dict_to_im
from pnmlib.tools import istriu, isgtriu
from pnmlib.tools import get_node_prefix, get_edge_prefix
from pnmlib.tools import generate_points_on_sphere
from pnmlib.tools import generate_points_on_circle
from pnmlib.tools import cart2sph, sph2cart, cart2cyl, cyl2cart
from pnmlib.core import _parse_indices
from scipy.spatial import KDTree, distance_matrix


__all__ = [
    # Topological
    'find_connecting_edges',
    'find_neighbor_nodes',
    'find_neighbor_edges',
    'find_connected_nodes',
    'find_complementary_nodes',
    'find_complementary_edges',
    'find_path',
    'filter_by_z',
    'find_coordination',
    'find_common_edges',
    'is_fully_connected',
    # Geometric
    'find_nearby_nodes',
    'find_surface_nodes',
    'find_surface_nodes_cubic',
    'find_coincident_nodes',
    'internode_distance',
    'dimensionality',
    'isoutside',
    'iscoplanar',
    'get_cubic_shape',
    'get_cubic_spacing',
    'get_domain_length',
    'get_domain_area',
]


def iscoplanar(network):
    r"""
    Determines if specified nodes are coplanar with each other

    Parameters
    ----------
    network : dict
        The graph dictionary

    Returns
    -------
    flag : bool
        A boolean value of whether given nodes are coplanar (``True``) or
        not (``False``)

    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix + '.coords']
    if np.shape(coords)[0] < 3:
        raise Exception('At least 3 input pores are required')

    Px = coords[:, 0]
    Py = coords[:, 1]
    Pz = coords[:, 2]

    # Do easy check first, for common coordinate
    if np.shape(np.unique(Px))[0] == 1:
        return True
    if np.shape(np.unique(Py))[0] == 1:
        return True
    if np.shape(np.unique(Pz))[0] == 1:
        return True

    # Perform rigorous check using vector algebra
    # Grab first basis vector from list of coords
    n1 = np.array((Px[1] - Px[0], Py[1] - Py[0], Pz[1] - Pz[0])).T
    n = np.array([0.0, 0.0, 0.0])
    i = 1
    while n.sum() == 0:
        if i >= (np.size(Px) - 1):
            return False
        # Chose a secon basis vector
        n2 = np.array((Px[i+1] - Px[i], Py[i+1] - Py[i], Pz[i+1] - Pz[i])).T
        # Find their cross product
        n = np.cross(n1, n2)
        i += 1
    # Create vectors between all other pairs of points
    r = np.array((Px[1:-1] - Px[0], Py[1:-1] - Py[0], Pz[1:-1] - Pz[0]))
    # Ensure they all lie on the same plane
    n_dot = np.dot(n, r)

    return bool(np.sum(np.absolute(n_dot)) == 0)


def find_coincident_nodes(network):
    r"""
    Finds nodes with identical coordinates

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    duplicates : list of ndarrays
        A list with each sublist indicating the indices of nodes that share
        a common set of coordinates

    Notes
    -----
    This function works by computing a ``hash`` of the coordinates then finding
    all nodes with equivalent hash values. Hashes are supposed to be unique
    but they occassionally "collide", meaning nodes may be identified as
    coincident that are not.
    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    hashed = [hash(row.tobytes()) for row in coords]
    uniq, counts = np.unique(hashed, return_counts=True)
    hits = np.where(counts > 1)[0]
    dupes = []
    for item in hits:
        dupes.append(np.where(hashed == uniq[item])[0])
    return dupes


def internode_distance(network, inds_1=None, inds_2=None):
    r"""
    Find the distance between all nodes on set 1 to each node in set 2

    Parameters
    ----------
    network : dict
        The network dictionary
    inds_1 : array_like
        A list containing the indices of the first set of nodes
    inds_2 : array_Like
        A list containing the indices of the first set of nodes.  It's OK if
        these indices are partially or completely duplicating ``nodes1``.

    Returns
    -------
    dist : array_like
        A distance matrix with ``len(site1)`` rows and ``len(sites2)`` columns.
        The distance between site *i* in ``site1`` and *j* in ``sites2`` is
        located at *(i, j)* and *(j, i)* in the distance matrix.

    Notes
    -----
    This function computes and returns a distance matrix, so can get large.
    For distances between larger sets a KD-tree approach would be better,
    which is available in ``scipy.spatial``.

    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    p1 = np.array(inds_1, ndmin=1)
    p2 = np.array(inds_2, ndmin=1)
    return distance_matrix(coords[p1], coords[p2])


def is_fully_connected(network, inds=None):
    r"""
    Checks whether graph is fully connected, i.e. not clustered

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like (optional)
        The indices of boundary nodes (i.e. inlets/outlets). If this is given
        the multiple sample spanning clusters will count as fully connected.

    Returns
    -------
    flag : bool
        If ``inds`` is not specified, then returns ``True`` only if
        the entire network is connected to the same cluster. If
        ``inds`` is given, then returns ``True`` only if all clusters
        are connected to the given boundary nodes.
    """
    am = dict_to_am(network)
    am = am.tolil()
    inds = np.array(inds)
    temp = csgraph.connected_components(am, directed=False)[1]
    is_connected = np.unique(temp).size == 1
    Np = am.shape[0]
    Nt = int(am.nnz/2)
    # Ensure all clusters are part of inds, if given
    if not is_connected and inds is not None:
        am.resize(Np + 1, Np + 1)
        am.rows[-1] = inds.tolist()
        am.data[-1] = np.arange(Nt, Nt + len(inds)).tolist()
        temp = csgraph.connected_components(am, directed=False)[1]
        is_connected = np.unique(temp).size == 1
    return is_connected


def get_cubic_spacing(network):
    r"""
    Determine spacing of a cubic network

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    spacing : ndarray
        An array containing the spacing between nodes in each direction

    """
    node_prefix = get_node_prefix(network)
    edge_prefix = get_edge_prefix(network)
    coords = network[node_prefix+'.coords']
    conns = network[edge_prefix+'.conns']
    # Find Network spacing
    C12 = coords[conns]
    mag = np.linalg.norm(np.diff(C12, axis=1), axis=2)
    unit_vec = np.around(np.squeeze(np.diff(C12, axis=1)) / mag, decimals=14)
    spacing = [0, 0, 0]
    dims = dimensionality(network)
    # Ensure vectors point in n-dims unique directions
    c = {tuple(row): 1 for row in unit_vec}
    mag = np.atleast_1d(mag.squeeze()).astype(float)
    if len(c.keys()) > sum(dims):
        raise Exception(
            "Spacing is undefined when throats point in more directions"
            " than network has dimensions."
        )
    for ax in [0, 1, 2]:
        if dims[ax]:
            inds = np.where(unit_vec[:, ax] == unit_vec[:, ax].max())[0]
            temp = np.unique(mag[inds])
            if not np.allclose(temp, temp[0]):
                raise Exception("A unique value of spacing could not be found.")
            spacing[ax] = temp[0]
    return np.array(spacing)


def get_cubic_shape(network):
    r"""
    Determine shape of a cubic network

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    shape : ndarray
        An array containing the shape of the network each direction

    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    L = np.ptp(coords, axis=0)
    mask = L.astype(bool)
    S = get_cubic_spacing(network)
    shape = np.array([1, 1, 1], int)
    shape[mask] = L[mask] / S[mask] + 1
    return shape


def get_domain_area(network, inlets=None, outlets=None):
    r"""
    Determine the cross sectional area relative to the inlets/outlets.

    Parameters
    ----------
    network : dict
        The network dictionary
    inlets : array_like
        The indices of the inlets
    outlets : array_Like
        The indices of the outlets

    Returns
    -------
    area : scalar
        The cross sectional area relative to the inlets/outlets.

    """
    if dimensionality(network).sum() != 3:
        raise Exception('The network is not 3D, specify area manually')
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    inlets = coords[inlets]
    outlets = coords[outlets]
    if not iscoplanar(inlets):
        print('Detected inlet pores are not coplanar')
    if not iscoplanar(outlets):
        print('Detected outlet pores are not coplanar')
    Nin = np.ptp(inlets, axis=0) > 0
    if Nin.all():
        print('Detected inlets are not oriented along a principle axis')
    Nout = np.ptp(outlets, axis=0) > 0
    if Nout.all():
        print('Detected outlets are not oriented along a principle axis')
    hull_in = ConvexHull(points=inlets[:, Nin])
    hull_out = ConvexHull(points=outlets[:, Nout])
    if hull_in.volume != hull_out.volume:
        print('Inlet and outlet faces are different area')
    area = hull_in.volume  # In 2D: volume=area, area=perimeter
    return area


def get_domain_length(network, inlets=None, outlets=None):
    r"""
    Determine the domain length relative to the inlets/outlets.

    Parameters
    ----------
    network : dict
        The network dictionary
    inlets : array_like
        The pore indices of the inlets.
    outlets : array_Like
        The pore indices of the outlets.

    Returns
    -------
    area : scalar
        The domain length relative to the inlets/outlets.

    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    inlets = coords[inlets]
    outlets = coords[outlets]
    if not iscoplanar(inlets):
        print('Detected inlet pores are not coplanar')
    if not iscoplanar(outlets):
        print('Detected inlet pores are not coplanar')
    tree = KDTree(data=inlets)
    Ls = np.unique(np.float64(tree.query(x=outlets)[0]))
    if not np.allclose(Ls, Ls[0]):
        print('A unique value of length could not be found')
    length = Ls[0]
    return length


def isoutside(network, shape, rtol=0.0):
    r"""
    Identifies sites that lie outside the specified shape

    Parameters
    ----------
    network : dict
        The network dictionary. For convenience it is also permissible to just
        supply an N-by-D array of coordinates.
    shape : array_like
        The shape of the domain beyond which points are considered "outside".
        The argument is treated as follows:

        ========== ============================================================
        shape      Interpretation
        ========== ============================================================
        [x, y, z]  A 3D cubic domain of dimension x, y and z with the origin at
                   [0, 0, 0].
        [x, y, 0]  A 2D square domain of size x by y with the origin at
                   [0, 0]
        [r, z]     A 3D cylindrical domain of radius r and height z whose
                   central axis starts at [0, 0, 0]
        [r, 0]     A 2D circular domain of radius r centered on [0, 0] and
                   extending upwards
        [r]        A 3D spherical domain of radius r centered on [0, 0, 0]
        ========== ============================================================

    rtol : scalar or array_like, optional
        Controls how far a node must be from the domain boundary to be
        considered outside. It is applied as a fraction of the domain size as
        ``x[i] > (shape[0] + shape[0]*threshold)`` or
        ``y[i] < (0 - shape[1]*threshold)``.  Discrete threshold values
        can be given for each axis by supplying a list the same size as
        ``shape``.

    Returns
    -------
    mask : boolean ndarray
        A boolean array with ``True`` values indicating nodes that lie outside
        the domain.

    Notes
    -----
    If the domain is 2D, either a circle or a square, then the z-dimension
    of ``shape`` should be set to 0.

    """
    try:
        node_prefix = get_node_prefix(network)
        coords = network[node_prefix+'.coords']
    except AttributeError:
        coords = network
    shape = np.array(shape, dtype=float)
    if np.isscalar(rtol):
        tolerance = np.array([rtol]*len(shape))
    else:
        tolerance = np.array(rtol)
    # Label external pores for trimming below
    if len(shape) == 1:  # Spherical
        # Find external points
        R, Q, P = cart2sph(*coords.T)
        thresh = tolerance[0]*shape[0]
        Ps = R > (shape[0] + thresh)
    elif len(shape) == 2:  # Cylindrical
        # Find external pores outside radius
        R, Q, Z = cart2cyl(*coords.T)
        thresh = tolerance[0]*shape[0]
        Ps = R > shape[0]*(1 + thresh)
        # Find external pores above and below cylinder
        if shape[1] > 0:
            thresh = tolerance[1]*shape[1]
            Ps = Ps + (coords[:, 2] > (shape[1] + thresh))
            Ps = Ps + (coords[:, 2] < (0 - thresh))
        else:
            pass
    elif len(shape) == 3:  # Rectilinear
        thresh = tolerance*shape
        Ps1 = np.any(coords > (shape + thresh), axis=1)
        Ps2 = np.any(coords < (0 - thresh), axis=1)
        Ps = Ps1 + Ps2
    return Ps


def dimensionality(network):
    r"""
    Checks the dimensionality of the network

    Parameters
    ----------
    network : dict
        The network dictionary
    cache : boolean, optional (default is True)
        If ``False`` then the dimensionality is recalculated even if it has
        already been calculated and stored in the graph dictionary.

    Returns
    -------
    dims : list
        A  3-by-1 array containing ``True`` for each axis that contains
        multiple values, indicating that the pores are spatially distributed
        in that dimension.

    """
    n = get_node_prefix(network)
    coords = network[n+'.coords']
    eps = np.finfo(float).resolution
    dims_unique = [not np.allclose(k, k.mean(), atol=0, rtol=eps) for k in coords.T]
    return np.array(dims_unique)


def find_surface_nodes(network):
    r"""
    Identifies nodes on the outer surface of the domain using a Delaunay
    tessellation

    Parameters
    ----------
    network : dict
        The network dictionary

    Returns
    -------
    mask : ndarray
        A boolean array of ``True`` values indicating which nodes were found
        on the surfaces.

    Notes
    -----
    This function generates points around the domain the performs a Delaunay
    tesselation between these points and the network nodes.  Any network
    nodes which are connected to a generated points is considered a surface
    node.

    """
    node_prefix = get_node_prefix(network)
    coords = np.copy(network[node_prefix+'.coords'])
    shift = np.mean(coords, axis=0)
    coords = coords - shift
    tmp = cart2sph(*coords.T)
    hits = np.zeros(coords.shape[0], dtype=bool)
    r = 2*tmp[0].max()
    dims = dimensionality(network)
    if sum(dims) == 1:
        hi = np.where(coords[:, dims] == coords[:, dims].max())[0]
        lo = np.where(coords[:, dims] == coords[:, dims].min())[0]
        hits[hi] = True
        hits[lo] = True
        return hits
    if sum(dims) == 2:
        markers = generate_points_on_circle(n=max(10, int(coords.shape[0]/10)), r=r)
        pts = np.vstack((coords[:, dims], markers))
    else:
        markers = generate_points_on_sphere(n=max(10, int(coords.shape[0]/10)), r=r)
        pts = np.vstack((coords, markers))
    tri = Delaunay(pts, incremental=False)
    (indices, indptr) = tri.vertex_neighbor_vertices
    for k in range(coords.shape[0], tri.npoints):
        neighbors = indptr[indices[k]:indices[k+1]]
        inds = np.where(neighbors < coords.shape[0])
        hits[neighbors[inds]] = True
    return hits


def find_surface_nodes_cubic(network):
    r"""
    Identifies nodes on the outer surface of the domain assuming a cubic domain
    to save time

    Parameters
    ----------
    network : dict
        The graph dictionary

    Returns
    -------
    mask : ndarray
        A boolean array of ``True`` values indicating which nodes were found
        on the surfaces.
    """
    node_prefix = get_node_prefix(network)
    coords = network[node_prefix+'.coords']
    hits = np.zeros(coords.shape[0], dtype=bool)
    dims = dimensionality(network)
    for d in range(3):
        if dims[d]:
            hi = np.where(coords[:, d] == coords[:, d].max())[0]
            lo = np.where(coords[:, d] == coords[:, d].min())[0]
            hits[hi] = True
            hits[lo] = True
    return hits


def find_nearby_nodes(network, nodes, r, flatten=False, include_input=False):
    r"""
    Find all pores within a given radial distance of the input pore(s)
    regardless of whether or not they are toplogically connected.

    Parameters
    ----------
    nodes : array_like
        The list of nodes for whom nearby neighbors are to be found
    r : scalar
        The maximum radius within which the search should be performed
    include_input : bool
        Controls whether the input pores should be included in the
        list of pores nearby the *other pores* in the input list.
        So if ``pores=[1, 2]`` and 1 and 2 are within ``r`` of each
        other, then 1 will be included in the returned for pores
        near 2, and vice-versa *if* this argument is ``True``.
        The default is ``False``.
    flatten : bool
        If ``True`` returns a single list of all pores that match the
        criteria, otherwise returns an array containing a sub-array for
        each input pore, where each sub-array contains the pores that
        are nearby to each given input pore.  The default is False.

    Returns
    -------
        A list of pores which are within the given spatial distance.
        If a list of N pores is supplied, then a an N-long list of
        such lists is returned.  The returned lists each contain the
        pore for which the neighbors were sought.

    Examples
    --------
    >>> import openpnm as op
    >>> pn = op.network.Cubic(shape=[3, 3, 3])
    >>> Ps = pn.find_nearby_pores(pores=[0, 1], r=1)
    >>> print(Ps[0])
    [3 9]
    >>> print(Ps[1])
    [ 2  4 10]
    >>> Ps = pn.find_nearby_pores(pores=[0, 1], r=0.5)
    >>> print(Ps)
    [array([], dtype=int64), array([], dtype=int64)]
    >>> Ps = pn.find_nearby_pores(pores=[0, 1], r=1, flatten=True)
    >>> print(Ps)
    [ 2  3  4  9 10]

    """
    nodes = _parse_indices(network, nodes)
    # Handle an empty array if given
    if np.size(nodes) == 0:
        return np.array([], dtype=np.int64)
    if r <= 0:
        raise Exception('Provided distances should be greater than 0')
    # Create kdTree objects
    kd = sptl.cKDTree(network['pore.coords'])
    kd_pores = sptl.cKDTree(network['pore.coords'][nodes])
    # Perform search
    Ps_within_r = kd_pores.query_ball_tree(kd, r=r)
    # Remove self from each list
    for i, P in enumerate(Ps_within_r):
        Ps_within_r[i].remove(nodes[i])
    # Convert to flattened list by default
    temp = np.concatenate((Ps_within_r))
    Pn = np.unique(temp).astype(np.int64)
    # Remove inputs if necessary
    if include_input is False:
        Pn = Pn[~np.in1d(Pn, nodes)]
    # Convert list of lists to a list of ndarrays
    if flatten is False:
        if len(Pn) == 0:  # Deal with no nearby neighbors
            Pn = [np.array([], dtype=np.int64) for i in nodes]
        else:
            mask = np.zeros(shape=np.amax((Pn.max(), nodes.max())) + 1, dtype=bool)
            mask[Pn] = True
            temp = []
            for item in Ps_within_r:
                temp.append(np.array(item, dtype=np.int64)[mask[item]])
            Pn = temp
    return Pn


def find_complementary_edges(network, inds, asmask=False):
    r"""
    Finds the complementary edges to a given set of inputs

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like
        A list of edge indices for which the complement is sought
    asmask : bool
        If set to ``True`` the result is returned as a boolean mask of the
        correct length with ``True`` values indicate the complements.  The
        default is ``False`` which returns a list of indices instead.

    Returns
    -------
    An array containing indices of the edges that are not part of the input
    list

    """
    edge_prefix = get_edge_prefix(network)
    inds = np.unique(inds)
    N = network[edge_prefix+'.conns'].shape[0]
    mask = np.ones(shape=N, dtype=bool)
    mask[inds] = False
    if asmask:
        return mask
    else:
        return np.arange(N)[mask]


def find_complementary_nodes(network, inds, asmask=False):
    r"""
    Finds the complementary nodes to a given set of inputs

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like (optional)
        A list of indices for which the complement is sought
    asmask : bool
        If set to ``True`` the result is returned as a boolean mask of the
        correct length with ``True`` values indicate the complements. The
        default is ``False`` which returns a list of indices instead.

    Returns
    -------
    An array containing indices of the nodes that are not part of the input
    list

    """
    node_prefix = get_node_prefix(network)
    inds = np.unique(inds)
    N = network[node_prefix+'.coords'].shape[0]
    mask = np.ones(shape=N, dtype=bool)
    mask[inds] = False
    if asmask:
        return mask
    else:
        return np.arange(N)[mask]


def find_connected_nodes(network, inds, flatten=True, logic='or'):
    r"""
    Finds which nodes are connected to a given set of edges

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like
        A list of edges indices whose connected nodes are sought
    flatten : bool (default is ``True``)
        Indicates whether the returned result is a compressed array of all
        neighbors, or a list of lists with each sub-list containing the
        neighbors for each input edge.  Note that an *unflattened* list might
        be slow to generate since it is a Python ``list`` rather than a Numpy
        array.
    logic : str
        Specifies logic to filter the resulting list.  Options are:

        ======= ===============================================================
        logic   Description
        ======= ===============================================================
        'or'    (default) All neighbors of the inputs.  This is also known as
                the 'union' in set theory or 'any' in boolean logic. Both
                keywords are accepted and treated as 'or'.
        'xor'   Only neighbors of one and only one inputs.  This is useful for
                finding neighbors that are not *shared* by any of the input
                nodes. 'exclusive_or' is also accepted.
        'xnor'  Neighbors that are shared by two or more inputs . This is
                equivalent to finding all neighbors with 'or', minus those
                found with 'xor', and is useful for finding neighbors that the
                inputs have in common.  'nxor' is also accepted.
        'and'   Only neighbors shared by all inputs. This is also known as
                'intersection' in set theory and (sometimes) as 'all' in
                boolean logic.  Both keywords are accepted and treated as
                'and'.
        ======= ===============================================================

    Returns
    -------
    An array containing the connected sites, filtered by the given logic.  If
    ``flatten`` is ``False`` then the result is a list of lists containing the
    neighbors of each given input edge.  In this latter case, nodes that
    have been removed by the given logic are indicated by ``nans``, thus the
    array is of type ``float`` and is not suitable for indexing.

    """
    if not isgtriu(network):
        raise Exception("This function is not implemented for directed networks")
    edges = np.array(inds, ndmin=1)
    if len(edges) == 0:  # Short-circuit this function if edges is empty
        return []
    am = dict_to_am(network)
    neighbors = np.hstack((am.row[edges], am.col[edges]))
    if neighbors.size > 0:
        n_sites = np.amax(neighbors)
    if logic in ['or', 'union', 'any']:
        neighbors = np.unique(neighbors)
    elif logic in ['xor', 'exclusive_or']:
        neighbors = np.unique(np.where(np.bincount(neighbors) == 1)[0])
    elif logic in ['xnor', 'nxor']:
        neighbors = np.unique(np.where(np.bincount(neighbors) > 1)[0])
    elif logic in ['and', 'all', 'intersection']:
        temp = np.vstack((am.row[edges], am.col[edges])).T.tolist()
        temp = [set(pair) for pair in temp]
        neighbors = temp[0]
        [neighbors.intersection_update(pair) for pair in temp[1:]]
        neighbors = np.array(list(neighbors), dtype=np.int64, ndmin=1)
    else:
        raise Exception('Specified logic is not implemented')
    if flatten is False:
        if neighbors.size:
            mask = np.zeros(shape=n_sites + 1, dtype=bool)
            mask[neighbors] = True
            temp = np.hstack((am.row[edges], am.col[edges])).astype(np.int64)
            temp[~mask[temp]] = -1
            inds = np.where(temp == -1)[0]
            if len(inds):
                temp = temp.astype(float)
                temp[inds] = np.nan
            temp = np.reshape(a=temp, newshape=[len(edges), 2], order='F')
            neighbors = temp
        else:
            neighbors = [np.array([], dtype=np.int64) for i in range(len(edges))]
    return neighbors


def find_neighbor_edges(network, inds, flatten=True, logic='or'):
    r"""
    Finds all edges that are connected to the given input nodes

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like (optional)
        A list of node indices whose neighbor edges are sought
    flatten : bool (default is ``True``)
        Indicates whether the returned result is a compressed array of all
        neighbors, or a list of lists with each sub-list containing the
        neighbors for each input node.  Note that an *unflattened* list might
        be slow to generate since it is a Python ``list`` rather than a Numpy
        array.
    logic : str
        Specifies logic to filter the resulting list.  Options are:

        ======= ===============================================================
        logic   Description
        ======= ===============================================================
        'or'    (default) All neighbors of the inputs.  This is also known as
                the 'union' in set theory or 'any' in boolean logic. Both
                keywords are accepted and treated as 'or'.
        'xor'   Only neighbors of one and only one inputs.  This is useful for
                finding neighbors that are not *shared* by any of the input
                nodes. 'exclusive_or' is also accepted.
        'xnor'  Neighbors that are shared by two or more inputs . This is
                equivalent to finding all neighbors with 'or', minus those
                found with 'xor', and is useful for finding neighbors that the
                inputs have in common.  'nxor' is also accepted.
        'and'   Only neighbors shared by all inputs. This is also known as
                'intersection' in set theory and (somtimes) as 'all' in
                boolean logic.  Both keywords are accepted and treated as
                'and'.
        ======= ===============================================================

    Returns
    -------
    An array containing the neighboring edges filtered by the given logic. If
    ``flatten`` is ``False`` then the result is a list of lists containing the
    neighbors of each given input node.

    Notes
    -----
    The ``logic`` options are applied to neighboring edges only, thus it is not
    possible to obtain edges that are part of the global set but not neighbors.
    This is because (a) the list of global edges might be very large, and
    (b) it is not possible to return a list of neighbors for each input site
    if global sites are considered.

    """
    if flatten == False:
        im = dict_to_im(network)
        am = None
    else:
        am = dict_to_am(network)
        im = None
    if im is not None:
        if im.format != 'lil':
            im = im.tolil(copy=False)
        rows = [im.rows[i] for i in np.array(inds, ndmin=1, dtype=np.int64)]
        if len(rows) == 0:
            return []
        neighbors = np.hstack(rows).astype(np.int64)
        n_bonds = int(im.nnz / 2)
        if logic in ['or', 'union', 'any']:
            neighbors = np.unique(neighbors)
        elif logic in ['xor', 'exclusive_or']:
            neighbors = np.unique(np.where(np.bincount(neighbors) == 1)[0])
        elif logic in ['xnor', 'shared']:
            neighbors = np.unique(np.where(np.bincount(neighbors) > 1)[0])
        elif logic in ['and', 'all', 'intersection']:
            neighbors = set(neighbors)
            [neighbors.intersection_update(i) for i in rows]
            neighbors = np.array(list(neighbors), dtype=int, ndmin=1)
        else:
            raise Exception('Specified logic is not implemented')
        if (flatten is False):
            if (neighbors.size > 0):
                mask = np.zeros(shape=n_bonds, dtype=bool)
                mask[neighbors] = True
                for i in range(len(rows)):
                    vals = np.array(rows[i], dtype=np.int64)
                    rows[i] = vals[mask[vals]]
                neighbors = rows
            else:
                neighbors = [np.array([], dtype=np.int64) for i in range(len(inds))]
        return neighbors
    elif am is not None:
        if am.format != 'coo':
            am = am.tocoo(copy=False)
        if flatten is False:
            raise Exception('flatten cannot be used with an adjacency matrix')
        if isgtriu(network):
            am = sprs.triu(am, k=1)
        Ps = np.zeros(am.shape[0], dtype=bool)
        Ps[inds] = True
        conns = np.vstack((am.row, am.col)).T
        if logic in ['or', 'union', 'any']:
            neighbors = np.any(Ps[conns], axis=1)
        elif logic in ['xor', 'exclusive_or']:
            neighbors = np.sum(Ps[conns], axis=1) == 1
        elif logic in ['xnor', 'shared']:
            neighbors = np.all(Ps[conns], axis=1)
        elif logic in ['and', 'all', 'intersection']:
            raise Exception('Specified logic is not implemented')
        else:
            raise Exception('Specified logic is not implemented')
        neighbors = np.where(neighbors)[0]
        return neighbors
    else:
        raise Exception('Either the incidence or the adjacency matrix must be specified')


def find_neighbor_nodes(network, inds, flatten=True, include_input=False,
                        logic='or'):
    r"""
    Finds all nodes that are directly connected to the input nodes

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like
        A list of node indices whose neighbors are sought
    flatten : bool
        If ``True`` (default) the returned result is a compressed array of all
        neighbors, or a list of lists with each sub-list containing the
        neighbors for each input site.  Note that an *unflattened* list might
        be slow to generate since it is a Python ``list`` rather than a Numpy
        array.
    include_input : bool
        If ``False`` (default) the input nodes will be removed from the result.

    logic : str
        Specifies logic to filter the resulting list.  Options are:

        ======= ===============================================================
        logic   Description
        ======= ===============================================================
        'or'    (default) All neighbors of the inputs.  This is also known as
                the 'union' in set theory or 'any' in boolean logic. Both
                keywords are accepted and treated as 'or'.
        'xor'   Only neighbors of one and only one inputs.  This is useful for
                finding neighbors that are not *shared* by any of the input
                nodes. 'exclusive_or' is also accepted.
        'xnor'  Neighbors that are shared by two or more inputs . This is
                equivalent to finding all neighbors with 'or', minus those
                found with 'xor', and is useful for finding neighbors that the
                inputs have in common.  'nxor' is also accepted.
        'and'   Only neighbors shared by all inputs. This is also known as
                'intersection' in set theory and (somtimes) as 'all' in
                boolean logic.  Both keywords are accepted and treated as
                'and'.
        ======= ===============================================================

    Returns
    -------
    nodes : ndarray
        An array containing the neighboring nodes filtered by the given logic.  If
        ``flatten`` is ``False`` then the result is a list of lists containing the
        neighbors of each input site.

    Notes
    -----
    The ``logic`` options are applied to neighboring nodes only, thus it is not
    possible to obtain nodes that are part of the global set but not neighbors.
    This is because the list of global nodes might be very large.

    """
    g = network
    nodes = np.array(inds, ndmin=1)
    # Short-circuit the function if the input list is already empty
    if len(nodes) == 0:
        return []
    am_coo = dict_to_am(g)
    am = am_coo.tolil(copy=False)
    rows = am.rows[nodes].tolist()
    if len(rows) == 0:
        return []
    n_nodes = am.shape[0]
    neighbors = am_coo.col[np.in1d(am_coo.row, nodes)]
    if logic in ['or', 'union', 'any']:
        neighbors = np.unique(neighbors)
    elif logic in ['xor', 'exclusive_or']:
        neighbors = np.unique(np.where(np.bincount(neighbors) == 1)[0])
    elif logic in ['xnor', 'nxor']:
        neighbors = np.unique(np.where(np.bincount(neighbors) > 1)[0])
    elif logic in ['and', 'all', 'intersection']:
        neighbors = set(neighbors)
        [neighbors.intersection_update(i) for i in rows]
        neighbors = np.array(list(neighbors), dtype=np.int64, ndmin=1)
    else:
        raise Exception('Specified logic is not implemented')
    # Deal with removing inputs or not
    mask = np.zeros(shape=n_nodes, dtype=bool)
    mask[neighbors] = True
    if not include_input:
        mask[nodes] = False
    # Finally flatten or not
    if flatten:
        neighbors = np.where(mask)[0]
    else:
        if neighbors.size > 0:
            for i in range(len(rows)):
                vals = np.array(rows[i], dtype=np.int64)
                rows[i] = vals[mask[vals]]
            neighbors = rows
        else:
            neighbors = [np.array([], dtype=int) for i in range(len(nodes))]
    return neighbors


def find_connecting_edges(inds, network=None, am=None):
    r"""
    Finds the edge that connects each pair of given nodes

    Parameters
    ----------
    inds : array_like
        A 2-column vector containing pairs of node indices
    network : dict, optional
        The network dictionary.  Either this or ``am`` must be provided
    am : scipy.sparse matrix, optional
        The adjacency matrix of the network. Must be symmetrical such that if
        nodes *i* and *j* are connected, the matrix contains non-zero values
        at locations (i, j) and (j, i). Either this or ``g`` must be provided.

    Returns
    -------
    edges : ndarray
        An ndarry the same length as P1 (and P2) with each element
        containing the edge number that connects the corresponding nodes,
        or `nan`` if nodes are not connected.

    Notes
    -----
    The adjacency matrix is converted to the ``DOK`` format internally if
    needed, so if this format is already available it should be provided to
    save time.

    """
    nodes = np.array(inds, ndmin=2)
    # Short-circuit function if nodes is an empty list
    if nodes.size == 0:
        return []
    if network is not None:
        edge_prefix = get_edge_prefix(network)
        am = dict_to_am(
            network,
            weights=np.arange(network[edge_prefix+'.conns'].shape[0])
        )
    elif am is not None:
        pass
    else:
        raise Exception('Either g or am must be provided')
    if am.format != 'dok':
        am = am.todok(copy=True)
    z = tuple(zip(nodes[:, 0], nodes[:, 1]))
    neighbors = np.array([am.get(item, np.nan) for item in z])
    return neighbors


def find_common_edges(network, inds_1, inds_2):
    """
    Finds edges shared between two sets of nodes

    Parameters
    ----------
    network : dict
        The network dictionary
    inds_1 : array_like
        A list of indices defining the first set of nodes
    inds_2 : array_like
        A list of indices defining the second set of nodes

    Returns
    -------
    edges : ndarray
        List of edge indices connecting the two given sets of nodes

    """
    if np.intersect1d(inds_1, inds_2).size != 0:
        raise Exception("inds_1 and inds_2 must not share any nodes")
    if not isgtriu(network):
        raise Exception("This function is not implemented for directed graphs")
    edges_1 = find_neighbor_edges(inds=inds_1, network=network, logic="xor")
    edges_2 = find_neighbor_edges(inds=inds_2, network=network, logic="xor")
    return np.intersect1d(edges_1, edges_2)


def filter_by_z(network, inds, z=1):
    r"""
    Filters a list of nodes to those with a given number of neighbors

    Parameters
    ----------
    network : dict
        The network dictionary
    inds : array_like
        A list containing the indices of the nodes to be filtered
    z : int
        The coordination number by which to filter

    Returns
    -------
    inds : array_like
        A list of node indices which satisfy the criteria

    """
    inds = np.array(inds)
    coordination = find_coordination(network)
    hits = coordination == z
    inds = inds[hits[inds]]
    return inds


def find_coordination(network, nodes=None):
    r"""
    Find the coordination number of nodes

    Parameters
    ----------
    network : dict
        The network dictionary
    nodes : array_like, optional
        The nodes for which coordination is sought. If not provided then
        coordination for *all* nodes is returned

    Returns
    -------
    z : ndarray
        An array containing the number of neighbors for each given node

    Notes
    -----
    Supports directed and undirected graphs

    """
    am = dict_to_am(network)
    z = am.getnnz(axis=1)
    if nodes is None:
        return z
    else:
        return z[np.array(nodes)]


def find_path(network, pairs, weights=None):
    r"""
    Find the shortest path between pairs of nodes

    Parameters
    ----------
    network : dict
        The network dictionary
    pairs : array_like
        An N x 2 array containing N pairs of nodes between which the shortest
        path is sought
    weights : ndarray, optional
        The edge weights to use when traversing the path. If not provided
        then 1's will be used.

    Returns
    -------
    paths : dict
        A dictionary containing ``'node_paths'`` and ``'edge_paths'``, each
        containing a list of lists indicating the path between each set of
        nodes given in ``pairs``. An empty list indicates that no path was
        found between a given set of pairs.

    Notes
    -----
    The shortest path is found using Dijkstra's algorithm included in the
    ``scipy.sparse.csgraph`` module

    """
    am = dict_to_am(network)
    if weights is not None:
        am.data = np.ones_like(am.row, dtype=int)
    pairs = np.array(pairs, ndmin=2)
    paths = csgraph.dijkstra(csgraph=am, indices=pairs[:, 0],
                             return_predecessors=True, min_only=False)[1]
    if isgtriu(network):
        am.data = np.hstack(2*[np.arange(am.data.size/2)]).astype(int)
    else:
        am.data = np.arange(am.data.size).astype(int)
    dok = am.todok()
    nodes = []
    edges = []
    for row in range(0, np.shape(pairs)[0]):
        j = pairs[row][1]
        ans = []
        while paths[row][j] > -9999:
            ans.append(j)
            j = paths[row][j]
        if len(ans) > 0:
            ans.append(pairs[row][0])
            ans.reverse()
            nodes.append(np.array(ans, dtype=int))
            keys = [tuple((ans[i], ans[i+1])) for i in range(len(ans)-1)]
            temp = [dok[k] for k in keys]
            edges.append(np.array(temp, dtype=int))
        else:
            nodes.append([])
            edges.append([])
    return {'node_paths': nodes, 'edge_paths': edges}
