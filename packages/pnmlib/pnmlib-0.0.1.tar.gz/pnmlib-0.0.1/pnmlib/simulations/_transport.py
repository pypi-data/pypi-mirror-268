import numpy as np
import scipy.sparse.csgraph as spgr
from pnmlib.tools import dict_to_am
from pnmlib import core
from sympy import symbols, sympify, lambdify
from scipy.sparse import linalg
import scipy.sparse as sprs


__all__ = [
    "create_algorithm",
    "build_A",
    "build_b",
    "set_value_bc",
    "set_rate_bc",
    "get_rate",
    "solve",
]


def create_algorithm(network):
    alg = {}
    alg['pore.all'] = network['pore.all']
    alg['throat.all'] = network['throat.all']
    return alg


def laplacian(am):
    diag = np.zeros(am.shape[0], dtype=float)
    np.add.at(diag, am.row, -am.data[am.col])
    A = am.copy()
    A.setdiag(diag)
    return A


def build_A(project, conductance):
    gvals = core.get_data(project, conductance)
    am = dict_to_am(project['network'], weights=gvals)
    A = spgr.laplacian(am).astype(float)
    return A


def build_A_from_am(am):
    A = laplacian(am)
    return A


def build_b(network):
    Np = core.num_pores(network)
    b = np.zeros(Np, dtype=float)
    return b


def build_b_from_am(am):
    b = np.zeros(shape=am.shape[0], dtype=float)  # Create vector of 0s
    return b


def set_value_bc(A, b, values, locs):
    b[locs] = values  # Put value in RHS
    # Zero rows and cols for given locs
    rows = np.isin(A.row, locs)
    A.data[rows] = 0
    # Re-add b entries to diagonal of A
    datadiag = A.diagonal()
    datadiag[locs] = np.ones_like(values)
    A.setdiag(datadiag)
    A.eliminate_zeros()  # Remove 0 entries
    return A, b


def set_rate_bc(b, rates, locs, w=0):
    b[locs] = b[locs]*w + rates*(1-2*w)
    return b


def get_rate(network, phase, x, locs):
    P12 = network['throat.conns']
    X12 = x[P12]
    g = phase['throat.hydraulic_conductance']
    Qt = g*(np.diff(X12, axis=1)).squeeze()
    Qp = np.zeros_like(x)
    np.add.at(Qp, P12[:, 0], -Qt)
    # _np.add.at(Qp, P12[:, 1], -Qt)
    R = Qp[locs]
    return R


def solve(A, b, solver='sp', **kwargs):
    f = globals()["solve_" + solver]
    x = f(A, b, **kwargs)
    return x


def solve_sp(A, b, **kwargs):
    x = linalg.spsolve(A=A.tocsr(), b=b, *kwargs)
    return x


# Below here is for reactive transport
def solve_reactive(A, b, x0=0, rxns={}, f=[0, 0], maxiter=100, tol=1e-15, solver='sp'):
    b_cached = b.copy()
    A_cached = A.copy()
    i = 0
    while i < maxiter:
        b = b_cached.copy()
        A = A_cached.copy()
        for locs, rxn in rxns.items():
            S1, S2, R = eval_source_term(x=x0, **rxn)
            A, b = set_source_term(A=A, b=b, locs=np.array(locs),
                                   S1=S1, S2=S2, f=f)
        x = solve(A=A, b=b, solver=solver)
        r = get_residual(A, b, x)
        if isconverged(A=A, b=b, x=x, tol=tol):
            break
        else:
            x0 = x
            i += 1
    if i == maxiter:
        print(f'Solution not converged after {i} iterations \n',
              f' Current residual is {r}')
    return A, b, x


def isconverged(A, b, x, tol=1e-10):
    res = get_residual(A, b, x)
    if not sprs.issparse(b):
        b = sprs.coo_matrix(b).T
    res_tol = sprs.linalg.norm(b) * tol
    flag_converged = True if (res <= res_tol) else False
    return flag_converged


def get_residual(A, b, x):
    if not sprs.issparse(x):
        x = sprs.coo_matrix(x).T
    if not sprs.issparse(b):
        b = sprs.coo_matrix(b).T
    res = sprs.linalg.norm(A * x - b)
    return res


def get_source_term(f, **kwargs):
    eqn = sympify(f)
    args = {'x': symbols('x')}
    for key in kwargs.keys():
        args[key] = symbols(key)
    r, s1, s2 = _build_func(eqn, **args)

    return {**{"S1": s1, "S2": s2, "R": r}, **kwargs}


def _build_func(eq, **args):
    eq_prime = eq.diff(args['x'])
    s1 = eq_prime
    s2 = eq - eq_prime*args['x']
    EQ = lambdify(args.values(), expr=eq, modules='numpy')
    S1 = lambdify(args.values(), expr=s1, modules='numpy')
    S2 = lambdify(args.values(), expr=s2, modules='numpy')
    return EQ, S1, S2


def eval_source_term(x, S1, S2, R, **kwargs):
    x = np.array(x)+1e-50
    S1_val = S1(x, **kwargs)
    S2_val = S2(x, **kwargs)
    R_val = R(x, **kwargs)
    return S1_val, S2_val, R_val


def set_source_term(A, b, locs, S1, S2, R=None, f=[0, 0]):
    # f = [0, 0] for steady-state
    # f = [0, 1] for explicit
    # f = [1, 1] for implicit
    # f = [0, 2] for crank-nicolson explicit
    # f = [1, 2] for crank-nicolson implicit
    diag = A.diagonal()
    diag[locs] += (1-2*f[0])*S1[locs]
    A.setdiag(diag)
    b[locs] -= (1-2*f[0])*S2[locs]
    return A, b
