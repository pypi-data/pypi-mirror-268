"""
Utility functions for quicfire-tools.
"""

from __future__ import annotations

import numpy as np
from pathlib import Path
from numpy import ndarray
from scipy.io import FortranFile


def compute_parabolic_stretched_grid(
    dz_surf: float, n_surf_cell: int, n_tot_cells: int, domain_height: float
) -> np.ndarray:
    """
    Generate a vertical grid spacing array with parabolic stretching.

    Parameters
    ----------
    dz_surf : float
        Vertical cell spacing at the surface, typically about 1 m.
    n_surf_cell : int
        Number of cells with constant vertical cell spacing (dz_surf) at the
        surface.
    n_tot_cells : int
        Total number of vertical cells in the grid. Typically ranges between
        20 and 30.
    domain_height : float
        Total height of the grid. For flat terrain without smoke transport
        concerns, it is usually around 100 m. For terrain with features, it
        should be approximately 3 times the height of the tallest feature.

    Returns
    -------
    np.ndarray
        Array representing the vertical grid spacing (dz) values for the
        simulation.

    Notes
    -----
    The function computes a parabolic stretching of the vertical grid spacings.
    The grid consists of a specified number of cells with uniform spacing at
    the surface, followed by cells with spacings determined by a parabolic
    formula until the total domain height is achieved.
    """
    dzmax_high = domain_height - dz_surf * n_surf_cell
    dzmax_low = 0

    dz = np.ones(n_tot_cells) * dz_surf

    while True:
        dzmax = 0.5 * (dzmax_low + dzmax_high)

        c1 = (dzmax - dz_surf) / ((n_tot_cells - n_surf_cell) ** 2)
        c2 = -2.0 * c1 * n_surf_cell
        c3 = dz_surf + c1 * n_surf_cell**2

        # Apply parabolic formula for cells beyond the surface cells
        kreal = np.arange(n_surf_cell, n_tot_cells, dtype=float)
        dz[n_surf_cell:] = (c1 * kreal**2) + (c2 * kreal) + c3

        zmax_temp = np.sum(dz)

        if abs(domain_height - zmax_temp) < 0.001:
            break
        elif zmax_temp > domain_height:
            dzmax_high = dzmax
        else:
            dzmax_low = dzmax

    dz[-1] += domain_height - np.sum(dz)

    return dz


def read_dat_file(
    filename: Path | str, nz: int, ny: int, nx: int, order: str = "C"
) -> ndarray:
    """
    Read in a .dat file as a numpy array.

    Parameters
    ----------
    filename : Path or str
        The path to the .dat file to read.
    nz : int
        The number of cells in the z-direction.
    ny : int
        The number of cells in the y-direction.
    nx : int
        The number of cells in the x-direction.
    order : str, optional
        The order of the array. Default is "C".

    Returns
    -------
    ndarray
        A 3D numpy array representing the data in the .dat file. The array
        has dimensions (nz, ny, nx).
    """
    if isinstance(filename, str):
        filename = Path(filename)

    with open(filename, "rb") as fin:
        arr = (
            FortranFile(fin)
            .read_reals(dtype="float32")
            .reshape((nz, ny, nx), order=order)
        )

    return arr
