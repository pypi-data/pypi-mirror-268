import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetCache:
    def test_pointset_cache(self, seismic_pointset):
        indices = [0, 103, 104, 105, 1000, 1103, 1104, 1105, 2000, 2103, 2104, 2105]
        x_values = [487882.6, 487882.6, 487882.6, 487882.6, 487707.3, 487803.7, 487803.7, 487803.7, 487628.5, 487724.9, 487724.9, 487724.9]
        y_values = [6225728.0, 6225728.0, 6225728.0, 6225728.0, 6225824.4, 6225999.7, 6225999.7, 6225999.7, 6226096.1, 6226271.4, 6226271.4, 6226271.4]
        z_values = [-2400.0, -3224.0, -3232.0, -3240.0, -3344.0, -3160.0, -3168.0, -3176.0, -3280.0, -3096.0, -3104.0, -3112.0]
        for i in [0, 103, 104, 105, 1000, 1000+103, 1000+104, 1000+105, 2000, 2000+103, 2000+104, 2000+105]:
            point = seismic_pointset.points[i]
            x = point.x
            y = point.y
            z = point.z
            assert i == indices.pop(0)
            assert x, 1 == pytest.approx(x_values.pop(0))
            assert y, 1 == pytest.approx(y_values.pop(0))
            assert z, 1 == pytest.approx(z_values.pop(0))