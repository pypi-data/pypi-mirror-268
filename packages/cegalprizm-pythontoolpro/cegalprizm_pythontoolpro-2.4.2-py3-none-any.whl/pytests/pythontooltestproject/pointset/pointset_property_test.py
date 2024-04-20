import pytest
import sys
import os
from datetime import datetime
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSetProperty:
    

    def test_pointset_property_complete(self, pointset):

        def is_almost(val, target):
            return True if abs(val - target) < 0.001 else False
        
        var = pointset
        old_df = var.as_dataframe()

        assert len(var.points) == 1
        assert len(list(var.as_dataframe())) == 15

        assert is_almost(var.as_dataframe()["x"][0], 1.0) == True
        assert is_almost(var.as_dataframe()["y"][0], 2.0) == True
        assert is_almost(var.as_dataframe()["z"][0], 914.40) == True
        assert is_almost(var.as_dataframe()["TWT auto"][0], -914.40) == True

        with var.values() as df:
            df["TWT auto"][0] = 42.0
        assert is_almost(var.as_dataframe()["TWT auto"][0], 42.0) == True
        with var.values() as df:
            df["TWT auto"][0] = old_df["TWT auto"][0]

        with var.values() as df:
            df["TWT auto"][0] = 13.37
        assert is_almost(var.as_dataframe()["TWT auto"][0], 13.37) == True
        with var.values() as df:
            df["TWT auto"][0] = old_df["TWT auto"][0]

        with var.values() as df:
            assert is_almost(df["Dip angle"][0], 45.00) == True
            df["Dip angle"][0] = 42.00
        with var.values() as df:
            assert is_almost(df["Dip angle"][0], 42.00) == True
            df["Dip angle"][0] = old_df["Dip angle"][0]

        with var.values() as df:
            assert is_almost(df["Continuous"][0], 4.20) == True
            df["Continuous"][0] = 42.00
        with var.values() as df:
            assert is_almost(df["Continuous"][0], 42.00) == True
            df["Continuous"][0] = old_df["Continuous"][0]

        with var.values() as df:
            assert str(df["Date"][0]) == "2020-01-28 00:00:00"
            df["Date"][0] = datetime.now()
        with var.values() as df:
            assert str(df["Date"][0]) != "2020-01-28 00:00:00"
            df["Date"][0] = old_df["Date"][0]

        with var.values() as df:
            assert df["TestBoolean"][0] == False
            df["TestBoolean"][0] = True
        with var.values() as df:
            assert df["TestBoolean"][0] == True
            df["TestBoolean"][0] = old_df["TestBoolean"][0]

        with var.values() as df:
            assert df["TestString"][0] == "Hello Pointset"
            df["TestString"][0] = "a"
        with var.values() as df:
            assert df["TestString"][0] == "a"
            df["TestString"][0] = old_df["TestString"][0]

        with var.values() as df:
            assert df["Discrete (1)"][0] == 42
            df["Discrete (1)"][0] = 2
        with var.values() as df:
            assert df["Discrete (1)"][0] == 2
            df["Discrete (1)"][0] = 42
