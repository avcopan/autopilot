"""Calculations.

These functions perform quantum chemistry calculations and return QCIO Results objects.
They do not interact with the database.
"""

import qcop
from automol import Geometry
from autostore import qc
from qcio import CalcType, ProgramArgs, ProgramInput, Results, SinglePointData


def energy(
    geo: Geometry, prog: str, args: ProgramArgs | dict[str, object]
) -> Results[ProgramInput, SinglePointData]:
    """
    Compute single-point energy.

    Parameters
    ----------
    geo
        Geometry.
    prog
        Program name.
    args
        Program arguments.

    Returns
    -------
        Energy in Hartree.

    Raises
    ------
    RuntimeError
        If the calculation fails.
    """
    args = ProgramArgs.model_validate(args)
    inp = ProgramInput(
        calctype=CalcType.energy,
        structure=qc.structure.from_geometry(geo),
        **args.model_dump(),
    )
    return qcop.compute(prog, inp)
