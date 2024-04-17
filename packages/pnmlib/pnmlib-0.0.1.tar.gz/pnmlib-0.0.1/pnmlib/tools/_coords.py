import numpy as np


__all__ = [
    'generate_points_on_sphere',
    'generate_points_in_disk',
    'generate_points_on_circle',
    'cart2sph',
    'sph2cart',
    'cart2cyl',
    'cyl2cart',
]


def generate_points_on_sphere(n=100, r=1):
    r"""
    Generates approximately equispaced points on the surface of a sphere

    Parameters
    ----------
    n : int or [int, int]
        If a single ``int`` is provided then this number of points will be
        generated using the Fibonacci method to make them approximately
        equally spaced.  If a list of 2 ``int``s is given, they are interpreted
        as the number of meridians and parallels to divide the sphere with.
    r : scalar
        The radius of the sphere on which the points should lie

    Returns
    -------
    coords : ndarray
        An array of x, y, z coordinates for the sphere which will be centered
        on [0, 0, 0]

    """
    if isinstance(n, int):
        i = np.arange(n)
        phi = np.pi * (3 - np.sqrt(5))  # golden angle in radians
        y = 1 - (i / float(n - 1))*2  # y goes from 1 to -1
        radius = np.sqrt(1 - y*y)  # radius at y
        theta = phi * i  # golden angle increment
        x = np.cos(theta) * radius
        z = np.sin(theta) * radius
        # Convert to spherical coords
        r_, q, p = cart2sph(x, y, z)
        # Scale the radius then convert back to cartesian
        X, Y, Z = sph2cart(r=r*r_, theta=q, phi=p)
        coords = np.vstack((X, Y, Z)).T
    else:
        nlat = n[0]
        nlon = n[1]
        lat = []
        lon = []
        for i in range(0, 360, max(1, int(360/nlon))):
            for j in range(max(1, int(180/nlat)), 180, max(1, int(180/nlat))):
                lon.append(i)
                lat.append(j)
        lat.extend([0, 180])
        lon.extend([0, 0])
        theta = np.deg2rad(lon) - np.pi
        phi = np.deg2rad(lat) - np.pi/2
        X, Y, Z = sph2cart(phi=phi, theta=theta, r=r)
        coords = np.vstack((X, Y, Z)).T
    return coords


def generate_points_in_disk(n=100, r=1):
    r"""
    Generates approximately equally spaced points inside a disk

    Parameters
    ----------
    n : int
        The number of points to generate
    r : scalar
        The radius of the disk

    Returns
    -------
    coords : ndarray
        An ``n by 2`` array of x, y points (in cartesian coordinates)
    """
    indices = np.arange(0, n, dtype=float) + 0.5
    r = np.sqrt(indices/n)
    theta = np.pi*(1 + 5**0.5)*indices
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return np.vstack((x, y)).T


def generate_points_on_circle(n=100, r=1):
    r"""
    Generates equally spaced points on a circle

    Parameters
    ----------
    n : int
        The number of points to generate
    r : scalar
        The radius of the disk

    Returns
    -------
    coords : ndarray
        An ``n by 2`` array of x, y points (in cartesian coordinates)
    """
    theta = np.linspace(0, 2*np.pi, n, endpoint=False)
    r = np.ones_like(theta)*r
    z = np.zeros_like(theta)
    x, y, z = cyl2cart(r=r, theta=theta, z=z)
    return np.vstack((x, y)).T


def cart2sph(x, y, z):
    r"""
    Converts cartesian to spherical coordinates

    Parameters
    ----------
    x, y, z : array_like
        Arrays containing the x, y and z coordinates to be converted

    Returns
    -------
    r, theta, phi : ndarrays
        Three arrays containing the spherical coordinate of each given point

    Notes
    -----
    Surprizingly (and annoyingly) this is not built into numpy, for reasons
    discussed `here <https://github.com/numpy/numpy/issues/5228>`_.
    """
    hxy = np.hypot(x, y)
    r = np.hypot(hxy, z)
    phi = np.arctan2(z, hxy)
    theta = np.arctan2(y, x)
    return r, theta, phi


def sph2cart(r, theta, phi):
    r"""
    Converts spherical to cartesian coordinates

    Parameters
    ----------
    r, theta, phi : array_like
        Arrays containing the r, theta and phi coordinates to be transformed

    Returns
    -------
    x, y, z : ndarrays
        Three arrays containing the cartesian coordinates of the given points

    Notes
    -----
    Surprizingly (and annoyingly) this is not built into numpy, for reasons
    discussed `here <https://github.com/numpy/numpy/issues/5228>`_.
    """
    rcos_theta = r * np.cos(phi)
    x = rcos_theta * np.cos(theta)
    y = rcos_theta * np.sin(theta)
    z = r * np.sin(phi)
    return x, y, z


def cart2cyl(x, y, z=0):
    r"""
    Converts cartesian to cylindrical coordinates

    Parameters
    ----------
    x, y, z : array_like
        Arrays containing the cartesian coordinates to be transformed. Note
        that ``z`` is optional since it is unchanged during this operation.
        If ``z`` is omitted it is assumed to be 0, or equivalent to polar
        coordinates.

    Returns
    -------
    r, theta, z : ndarrays
        Three arrays containing the cylindrical coordinates of the given points

    Notes
    -----
    Surprizingly (and annoyingly) this is not built into numpy, for reasons
    discussed `here <https://github.com/numpy/numpy/issues/5228>`_.
    """
    theta = np.arctan2(y, x)
    r = np.hypot(x, y)
    if isinstance(z, (int, float)):
        z = np.ones_like(r)*z
    return r, theta, z


def cyl2cart(r, theta, z=0):
    r"""
    Converts cylindrical to cartesian coordinates

    Parameters
    ----------
    r, theta, z : array_like
        Arrays containing the cylindrical coordinates to be transformed. Note
        that ``z`` is optional since it is unchanged during this operation.
        If ``z`` is omitted it is assumed to be 0, or equivalent to polar
        coordinates.

    Returns
    -------
    x, y, z : ndarrays
        Three arrays containing the cartesian coordinates of the given points

    Notes
    -----
    Surprizingly (and annoyingly) this is not built into numpy, for reasons
    discussed `here <https://github.com/numpy/numpy/issues/5228>`_.
    """
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    if isinstance(z, (int, float)):
        z = np.ones_like(x)*z
    return x, y, z
