"""Single-point calculations."""

from automol import Geometry
from autostore import Database, write
from qcio import ProgramArgs

from . import calc


def energy(
    geo: Geometry, prog: str, args: ProgramArgs | dict[str, object], db: Database
) -> float:
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
    res = calc.energy(geo, prog, args)
    if not res.success or res.data.energy is None:
        msg = f"Calculation failed: {res.traceback}"
        raise RuntimeError(msg)

    write.energy(res, db)
    return res.data.energy
