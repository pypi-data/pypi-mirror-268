import scipy.spatial as sptl
import scipy.sparse as sprs
import numpy as np
from pnmlib.tools import tri_to_am


def bcc(
    shape,
    spacing=1,
    method='kdtree',
):
    r"""
    Generate a body-centered cubic lattice

    Parameters
    ----------
    shape : array_like
        The number of corner sites in each direction.  A cubic lattice of
        this size is created and then 'body-centered' nodes are added
        afterward.
    spacing : array_like or float
        The size of a unit cell in each direction. If an scalar is given it is
        applied in all 3 directions.
    method : str
        Dictate how neighbors are found.  Options are:

        ===============  ======================================================
        mode             meaning
        ===============  ======================================================
        'kdtree'         Uses ``scipy.spatial.KDTree`` to find all neighbors
                         within the unit cell
        'triangulation'  Uses ``scipy.spatial.Delaunay`` to find all neighbors
        ===============  ======================================================

    Returns
    -------
    network : dict
        A dictionary containing 'coords', 'conns' and various boolean labels
        (i.e. 'node.center')

    Notes
    -----
    It is not clear whether KDTree or Delaunay are faster. In fact it is
    surely possible to find the neighbors formulaically but this is not
    implemented yet.

    """
    from pnmlib.generators import cubic
    shape = np.array(shape)
    spacing = np.array(spacing)
    net1 = cubic(shape=shape, spacing=1)
    net2 = cubic(shape=shape-1, spacing=1)
    net2['pore.coords'] += 0.5
    crds = np.concatenate(
        (net1['pore.coords'],
         net2['pore.coords']))
    corner_label = np.concatenate(
        (np.ones(net1['pore.coords'].shape[0], dtype=bool),
         np.zeros(net2['pore.coords'].shape[0], dtype=bool)))
    body_label = np.concatenate(
        (np.zeros(net1['pore.coords'].shape[0], dtype=bool),
         np.ones(net2['pore.coords'].shape[0], dtype=bool)))
    if method.startswith('tri'):
        tri = sptl.Delaunay(points=crds)
        am = tri_to_am(tri)
        conns = np.vstack((am.row, am.col)).T
        # Trim diagonal connections between cubic pores
        L = np.sqrt(np.sum(np.diff(crds[conns], axis=1)**2, axis=2)).flatten()
        conns = conns[L <= 1]
    elif method.startswith('kd'):
        tree1 = sptl.KDTree(crds)
        # Method 1
        hits = tree1.query_ball_point(crds, r=1)
        # Method 2: Not sure which is faster
        # tree2 = sptl.KDTree(crds)
        # hits = tree1.query_ball_tree(tree1, r=1)
        indices = np.hstack(hits)
        # Convert to CSR matrix
        indptr = [len(i) for i in hits]
        indptr.insert(0, 0)
        indptr = np.cumsum(indptr)
        am = sprs.csr_matrix((np.ones_like(indices), indices, indptr))
        am = sprs.triu(am, k=1)
        am = am.tocoo()
        conns = np.vstack((am.row, am.col)).T

    d = {}
    d['pore.coords'] = crds*spacing
    d['throat.conns'] = conns
    d['pore.corner'] = corner_label
    d['pore.body'] = body_label
    return d


if __name__ == '__main__':
    import openpnm as op
    import matplotlib.pyplot as plt
    pn = op.network.Network()
    net = bcc([3, 3, 3], 1, mode='tri')
    net['pore.coords'] = net.pop('pore.coords')
    net['throat.conns'] = net.pop('throat.conns')
    net['pore.corner'] = net.pop('pore.corner')
    net['pore.body'] = net.pop('pore.body')
    pn.update(net)
    pn['pore.all'] = np.ones((np.shape(pn.coords)[0]), dtype=bool)
    pn['throat.all'] = np.ones((np.shape(pn.conns)[0]), dtype=bool)
    fig, ax = plt.subplots()
    op.visualization.plot_connections(pn, ax=ax)
    op.visualization.plot_coordinates(pn, ax=ax)
