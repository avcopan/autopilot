"""Core functions."""

from automol import Geometry
from autostore import Calculation, Database, read, write
from qcio import Structure

from . import compute


def energy(
    geo: Geometry, calc: Calculation, *, db: Database, hash_name: str = "minimal"
) -> float:
    """
    Compute energy.

    Parameters
    ----------
    geo
        Geometry.
    calc
        Calculation metadata.
    db
        Database connection manager.
    hash_name
        Calculation hash type.

    Returns
    -------
        Energy in Hartree.

    Raises
    ------
    RuntimeError
        If the calculation fails.
    """
    ene = read.energy(geo, calc, db=db, hash_name=hash_name)
    if ene is not None:
        return ene

    res = compute.energy(geo, calc)
    if not res.success or res.data.energy is None:
        msg = f"Calculation failed: {res.traceback}"
        raise RuntimeError(msg)

    write.energy(res, db)
    return res.data.energy


def stationary_point(geo: Geometry, calc: Calculation, *, db: Database) -> Structure:
    """
    Compute stationary point structure.

    Parameters
    ----------
    geo
        Geometry.
    calc
        Calculation metadata.
    db
        Database connection manager.
    hash_name
        Calculation hash type.

    Returns
    -------
        Final structure.

    Raises
    ------
    RuntimeError
        If the calculation fails.
    """
    res = compute.stationary_point(geo, calc)

    if not res.success or res.data.final_structure is None:  # ty:ignore[unresolved-attribute]
        msg = f"Calculation failed: {res.traceback}"
        raise RuntimeError(msg)

    write.stationary_point(res, db)

    return res.data.final_structure  # ty:ignore[unresolved-attribute]
