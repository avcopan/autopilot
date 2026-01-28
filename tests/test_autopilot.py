"""autopilot tests."""

from collections.abc import Iterator

import numpy as np
import pytest
from automol import Geometry
from autostore import Database

import autopilot


@pytest.fixture
def database() -> Iterator[Database]:
    """In-memory database fixture."""
    db = Database(":memory:")
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def water() -> Geometry:
    """Water geometry fixture."""
    return Geometry(
        symbols=["O", "H", "H"], coordinates=[[0, 0, 0], [1, 0, 0], [0, 1, 0]]
    )


def test_energy(water: Geometry, database: Database) -> None:
    """Test single-point energy calculation."""
    energy = autopilot.energy(
        water, prog="crest", args={"model": {"method": "gfn2"}}, db=database
    )
    assert np.isclose(energy, -5.062316802835694)
