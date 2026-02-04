"""Calculations.

These functions perform quantum chemistry calculations and return QCIO Results objects.
They do not interact with the database.
"""

import qcop
from automol import Geometry
from autostore import Calculation
from qcio import CalcType, ProgramInput, Results, SinglePointData


def energy(geo: Geometry, calc: Calculation) -> Results[ProgramInput, SinglePointData]:
    """
    Compute single-point energy.

    Parameters
    ----------
    geo
        Geometry.
    calc
        Calculation metadata.

    Returns
    -------
        Energy in Hartree.

    Raises
    ------
    RuntimeError
        If the calculation fails.
    """
    inp = calc.to_qcio_program_input(geo, CalcType.energy)
    return qcop.compute(calc.program, inp)


def stationary_point(
    geo: Geometry, calc: Calculation
) -> Results[ProgramInput, SinglePointData]:
    """
    Compute optimized structure.

    Parameters
    ----------
    geo
        Geometry.
    calc
        Calculation metadata.

    Returns
    -------
        Energy in Hartree.

    Raises
    ------
    RuntimeError
        If the calculation fails.
    """
    inp = calc.to_qcio_program_input(geo, CalcType.optimization)
    return qcop.compute(calc.program, inp)
