"""Single-point calculations."""

import qcop
from automol import Geometry
from qcio import CalcType, ProgramArgs, ProgramInput

from .. import qc


def energy(geo: Geometry, prog: str, args: ProgramArgs | dict[str, object]) -> float:
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
    res = qcop.compute(prog, inp)

    if not res.success:
        msg = f"Calculation failed: {res.traceback}"
        raise RuntimeError(msg)

    return res.data.energy
