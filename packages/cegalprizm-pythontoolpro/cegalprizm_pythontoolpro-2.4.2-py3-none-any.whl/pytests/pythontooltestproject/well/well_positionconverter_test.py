import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellPositionConverter:
    def test_well_position_converter_time(self, well_good):
        xytime = well_good.md_to_xytime([5000,5100])
        assert xytime[0][0] == pytest.approx(486744.2, rel=1e-3)
        assert xytime[1][0] == pytest.approx(6226787.9, rel=1e-3)
        assert xytime[2][0] == pytest.approx(-1588.8, rel=1e-3)
        assert xytime[0][1] == pytest.approx(486744.5, rel=1e-3)
        assert xytime[1][1] == pytest.approx(6226787.8, rel=1e-3)
        assert xytime[2][1] == pytest.approx(-1621.1, rel=1e-3)

    def test_well_position_converter_depth(self, well_good):
        xydepth = well_good.md_to_xydepth([5000, 5100])
        assert xydepth[0][0] == pytest.approx(486744.2, rel=1e-3)
        assert xydepth[1][0] == pytest.approx(6226787.9, rel=1e-3)
        assert xydepth[2][0] == pytest.approx(-4917.8, rel=1e-3)
        assert xydepth[0][1] == pytest.approx(486744.5, rel=1e-3)
        assert xydepth[1][1] == pytest.approx(6226787.8, rel=1e-3)
        assert xydepth[2][1] == pytest.approx(-5017.8, rel=1e-3)
