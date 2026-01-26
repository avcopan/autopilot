"""autopilot tests."""

import numpy as np
import pytest
from automol import Geometry

from autopilot import calc


@pytest.fixture
def water() -> Geometry:
    """Water geometry fixture."""
    return Geometry(
        symbols=["O", "H", "H"], coordinates=[[0, 0, 0], [1, 0, 0], [0, 1, 0]]
    )


def test_energy(water: Geometry) -> None:
    """Test single-point energy calculation."""
    energy = calc.single.energy(water, prog="crest", args={"model": {"method": "gfn2"}})
    assert np.isclose(energy, -5.062316802835694)
