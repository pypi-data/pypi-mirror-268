import pytest
import os
import sys
import pandas as pd
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestCheckShotDataFrame:
    def test_checkshot_dataframe_basic(self, checkshot_all):
        df = checkshot_all.as_dataframe()
        assert df is not None
        assert len(df) == 171
        assert len(df.columns) >= 7

        assert df["Petrel Index"][22] == 23
        assert df["MD"][22] == 1908.67
        assert df["TWT"][22] == -1766.0
        assert df["Average Velocity"][22] == 647.23
        assert df["Interval Velocity"][22] == 725.71
        assert df["Z"][22] == 1875.0
        assert df["Well"][22] == "A16"

        assert df["MD"][71] == 1914.18
        assert df["TWT"][71] == -1802.0
        assert df["Average Velocity"][71] == -660.06
        assert df["Interval Velocity"][71] == -729.41
        assert df["Z"][71] == -1951.17     # Z does not match General in this case
        assert df["Well"][71] == "B9"

    def test_checkshot_dataframe_skip_unconnected(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_unconnected_checkshots=False)
        assert df is not None
        assert len(df) == 55
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 28

    def test_checkshot_dataframe_include_unconnected(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_unconnected_checkshots=True)
        assert len(df) == 171
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 1

    def test_checkshot_dataframe_unconnected_bad_input(self, checkshot_all):
        with pytest.raises(TypeError) as excinfo:
            checkshot_all.as_dataframe(include_unconnected_checkshots="No, please skip them")
        assert "bool" in excinfo.value.args[0]
        assert "expected" in excinfo.value.args[0]

    def test_checkshot_dataframe_include_unconnected_skip_user_properties(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_unconnected_checkshots=True, include_user_defined_properties=False)
        assert len(df) >= 171
        assert len(df.columns) < 8

    def test_checkshot_dataframe_skip_unconnected_skip_user_properties(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_unconnected_checkshots=False, include_user_defined_properties=False)
        assert len(df) < 171
        assert len(df.columns) < 8

    def test_checkshot_dataframe_skip_unconnected_include_user_properties(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_unconnected_checkshots=False, include_user_defined_properties=True)
        assert len(df) < 171
        assert len(df.columns) >= 8

    def test_checkshot_dataframe_one_well(self, checkshot_all, wellb1):
        df = checkshot_all.as_dataframe(wells_filter=[wellb1])
        assert df is not None
        assert len(df) == 12
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 28

    def test_checkshot_dataframe_two_wells(self, checkshot_all, wellb1, wellb8):
        df = checkshot_all.as_dataframe(wells_filter=[wellb1, wellb8])
        assert df is not None
        assert len(df) == 19
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 28
        assert df["Well"][0] == "B1"
        assert df["Well"][12] == "B8"

    def test_checkshot_dataframe_two_wells_one_none(self, checkshot_all, wellb1, wellb8):
        df = checkshot_all.as_dataframe(wells_filter=[wellb1, None, wellb8])
        assert df is not None
        assert len(df) == 19
        assert len(df.columns) >= 7
        assert df["Well"][0] == "B1"
        assert df["Well"][12] == "B8"

    def test_checkshot_dataframe_wells_filter_empty_returns_all_wells(self, checkshot_all):
        df = checkshot_all.as_dataframe(wells_filter=[])
        assert df is not None
        assert len(df) == 171
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 1
        assert df["Well"][0] == "A10"

    def test_checkshot_dataframe_wells_filter_none_returns_all_wells(self, checkshot_all):
        df = checkshot_all.as_dataframe(wells_filter=None)
        assert df is not None
        assert len(df) == 171
        assert len(df.columns) >= 7
        assert df["Petrel Index"][0] == 1

    def test_checkshot_dataframe_wells_filter_invalid_type(self, checkshot_all):
        with pytest.raises(TypeError) as excinfo:
            checkshot_all.as_dataframe(wells_filter="Give me a well")
        assert excinfo.value.args[0] == "wells_filter must be a list of Well objects as returned from petrelconnection.wells"

    def test_checkshot_dataframe_wells_filter_invalid_well(self, checkshot_all, wellb1):
        with pytest.raises(ValueError) as excinfo:
            checkshot_all.as_dataframe(wells_filter=[wellb1, "Give me a well"])
        assert excinfo.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    def test_checkshot_dataframe_user_properties_excluded(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_user_defined_properties=False)
        assert df is not None
        assert len(df) == 171
        assert len(df.columns) == 7

    def test_checkshot_dataframe_user_properties_included(self, checkshot_all):
        df = checkshot_all.as_dataframe(include_user_defined_properties=True)
        assert df is not None
        assert len(df) == 171
        assert len(df.columns) == 8

        general = df["General"]
        assert general.dtype == "float64"
        assert general[0] == 0.0
        assert general[170] == -2370.0

    def test_checkshot_dataframe_user_properties_datetime(self, checkshot_user_properties):
        df = checkshot_user_properties.as_dataframe(include_user_defined_properties=True)
        assert df is not None
        assert len(df) == 7
        assert len(df.columns) >= 16
        
        dates = df["DateValues"]
        assert dates.dtype == "datetime64[ns]"
        assert dates[0] == pd.Timestamp("2015-05-05 00:00:00")

    def test_checkshot_dataframe_user_properties_bool(self, checkshot_user_properties):
        df = checkshot_user_properties.as_dataframe()
        bools = df["BoolValues"]
        assert bools.dtype == "bool"
        assert bools[0] == False
        assert bools[5] == True

    def test_checkshot_dataframe_user_properties_int(self, checkshot_user_properties):
        df = checkshot_user_properties.as_dataframe()
        ints = df["IntegerValues"]
        assert ints.dtype == pd.Int64Dtype()
        assert ints[0] == 150
        assert ints[6] == 156

    def test_checkshot_dataframe_user_properties_string(self, checkshot_user_properties):
        df = checkshot_user_properties.as_dataframe()
        strings = df["StringValues"]
        assert strings[0] == "First Line"
        assert strings[6] == "LastLine"

    def test_checkshot_dataframe_user_properties_duplicate_name(self, checkshot_user_properties):
        df = checkshot_user_properties.as_dataframe()
        userProp = df["MD (User Defined)"]
        assert userProp.dtype == "float64"
        assert userProp[3] == 1234.56

    def test_checkshot_dataframe_user_properties_multiple_duplicates(self, checkshot_user_properties):
        ## There are three attributes named "Continuous" in the checkshot 
        df = checkshot_user_properties.as_dataframe()
        with pytest.raises(KeyError):
            df["Continuous"]
        first = df["Continuous (1)"]
        second = df["Continuous (2)"]
        third = df["Continuous (3)"]
        assert first[1] == 1.2
        assert second[1] == 2.2
        assert third[1] == 3.2
