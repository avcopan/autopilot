"""QCIO Structure interface."""

import pint
from automol import Geometry
from qcio import Structure


def from_geometry(geo: Geometry) -> Structure:
    """
    Generate QCIO Structure from Geometry.

    Parameters
    ----------
    geo
        Geometry.

    Returns
    -------
        QCIO Structure.
    """
    return Structure(
        symbols=geo.symbols,
        geometry=geo.coordinates * pint.Quantity("angstrom").m_as("bohr"),
        charge=geo.charge,
        multiplicity=geo.spin + 1,
    )
