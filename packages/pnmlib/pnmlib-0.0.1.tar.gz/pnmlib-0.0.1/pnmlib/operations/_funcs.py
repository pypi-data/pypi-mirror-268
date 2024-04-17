import numpy as np


__all__ = [
    "rotate_coords",
    "shear_coords",
]


def rotate_coords(coords, a=0, b=0, c=0, R=None):
    r"""
    Rotates coordinates a given amount about each axis

    Parameters
    ----------
    coords : ndarray
        The site coordinates to be transformed.  ``coords`` must be in 3D,
        but a 2D network can be represented by putting 0's in the missing
        dimension.
    a, b, c : scalar, optional
        The amount in degrees to rotate about the x, y, and z-axis,
        respectively.
    R : array_like, optional
        Rotation matrix.  Must be a 3-by-3 matrix since coordinates are
        always in 3D.  If this is given then `a`, `b`, and `c` are ignored.

    Returns
    -------
    coords : ndarray
        A copy of the given ``coords`` is made and returned to the rotation
        does not occur *in place*.

    See Also
    --------
    shear_coords

    """
    coords = np.copy(coords)
    if R is None:
        if a:
            R = np.array([[1, 0, 0],
                          [0, np.cos(np.deg2rad(a)), -np.sin(np.deg2rad(a))],
                          [0, np.sin(np.deg2rad(a)), np.cos(np.deg2rad(a))]])
            coords = np.tensordot(coords, R, axes=(1, 1))
        if b:
            R = np.array([[np.cos(np.deg2rad(b)), 0, -np.sin(np.deg2rad(b))],
                          [0, 1, 0],
                          [np.sin(np.deg2rad(b)), 0, np.cos(np.deg2rad(b))]])
            coords = np.tensordot(coords, R, axes=(1, 1))
        if c:
            R = np.array([[np.cos(np.deg2rad(c)), -np.sin(np.deg2rad(c)), 0],
                          [np.sin(np.deg2rad(c)), np.cos(np.deg2rad(c)), 0],
                          [0, 0, 1]])
            coords = np.tensordot(coords, R, axes=(1, 1))
    else:
        coords = np.tensordot(coords, R, axes=(1, 1))
    return coords


def shear_coords(coords, ay=0, az=0, bx=0, bz=0, cx=0, cy=0, S=None):
    r"""
    Shears the coordinates a given amount about along axis

    Parameters
    ----------
    coords : ndarray
        The coordinates to be transformed
    ay : scalar
        The factor by which to shear along the x-axis as a function of y
    az : scalar
        The factor by which to shear along the x-axis as a function of z
    bx : scalar
        The factor by which to shear along the y-axis as a function of x
    bz : scalar
        The factor by which to shear along the y-axis as a function of z
    cx : scalar
        The factor by which to shear along the z-axis  as a function of x
    cy : scalar
        The factor by which to shear along the z-axis as a function of y
    S : array_like
        The shear matrix.  Must be a 3-by-3 matrix since pore coordinates are
        always in 3D.  If this is given then the other individual arguments
        are ignored.

    Returns
    -------
    coords : ndarray
        The sheared coordinates.  A copy of the supplied coordinates is made
        so that the operation is not performed *in place*.

    See Also
    --------
    rotate_coords

    Notes
    -----
    The shear along the i *th*-axis is given as i\* = i + aj.  This means
    the new i coordinate is the old one plus some linear factor *a* in the
    j *th* direction.

    The values of ``a``, ``b``, and ``c`` are essentially the inverse of the
    slope to be formed by the neighboring layers of sheared pores.  A value of
    0 means no shear, and neighboring points are stacked directly on top of
    each other; a value of 1 means they form a 45 degree diagonal, and so on.

    If ``S`` is given, then is should be of the form:

    ::

        S = [[1 , ay, az],
             [bx, 1 , bz],
             [cx, cy, 1 ]]

        where any of the off-diagonal components can be 0 meaning no shear

    """
    coords = np.copy(coords)
    if S is None:
        S = np.array([[1, ay, az],
                      [bx, 1, bz],
                      [cx, cy, 1]])
    coords = (S@coords.T).T
    return coords
