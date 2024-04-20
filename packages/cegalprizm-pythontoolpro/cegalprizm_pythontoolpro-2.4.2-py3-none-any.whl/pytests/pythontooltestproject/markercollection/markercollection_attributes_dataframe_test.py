import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAttributeDataframe:
    def test_markerattribute_dataframe_no_filter(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        df = dipAngle.as_dataframe()
        assert len(df) == 105
        with pytest.raises(KeyError):
            df["Dip angle"]
        assert len(df["Value"]) == 105
        assert len(df.columns) == 5
        assert df["Petrel index"][6] == 7
        assert df["Value"][6] == 8.93
        assert df["Well identifier (Well name)"][6] == "B9"
        assert df["Surface"][6] == "Base Cretaceous"
        assert df["Petrel index"][68] == 69
        assert df["Value"][68] == 14.95
        assert df["Well identifier (Well name)"][68] == "" # Unconnected marker
        assert df["Surface"][68] == "Ness1"

    def test_markerattribute_dataframe_skip_unconnected(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        df = dipAngle.as_dataframe(include_unconnected_markers=False)
        assert len(df) == 29
        assert len(df.columns) == 5
        assert df["Petrel index"][1] == 5
        assert df["Value"][1] == 3.38
        assert df["Well identifier (Well name)"][1] == "B4"
        assert df["Surface"][1] == "Base Cretaceous"
        assert df["Petrel index"][28] == 104
        assert df["Value"][28] == 2.46
        assert df["Well identifier (Well name)"][28] == "B2"
        assert df["Surface"][28] == "Ness1"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_well_filter(self, welltops, wellb1):
        dipAngle = welltops.attributes["Dip angle"]
        df = dipAngle.as_dataframe(well=wellb1)
        assert len(df) == 8

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_well_filter_bad_input(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(well="B1")
        assert raised_error.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_stratigraphy_filter(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        strat = welltops.stratigraphies["Base Cretaceous"]
        df = dipAngle.as_dataframe(marker_stratigraphy=strat)
        assert len(df) == 18

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_stratigraphy_filter_skip_unconnected(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        strat = welltops.stratigraphies["Base Cretaceous"]
        df = dipAngle.as_dataframe(include_unconnected_markers=False, marker_stratigraphy=strat)
        assert len(df) == 7

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_stratigraphy_filter_bad_input(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(marker_stratigraphy="Base Cretaceous")
        assert raised_error.value.args[0] == "Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_wells_filter_and_well_raises_value_error(self, welltops, wellb1):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(well=wellb1, wells_filter=[wellb1])
        assert raised_error.value.args[0] == "The well and wells_filter arguments cannot be used at the same time"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_stratigraphies_filter_and_stratigraphy_raises_value_error(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        strat = welltops.stratigraphies["Base Cretaceous"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(marker_stratigraphy=strat, marker_stratigraphies_filter=[strat])
        assert raised_error.value.args[0] == "The marker_stratigraphy and marker_stratigraphies_filter arguments cannot be used at the same time"

    def test_markerattribute_dataframe_wells_filter(self, welltops, wellb1, wellb2, wellb8):
        dipAngle = welltops.attributes["Dip angle"]
        df = dipAngle.as_dataframe(wells_filter=[wellb1, wellb2, wellb8])
        assert len(df) == 21

    def test_markerattribute_dataframe_stratigraphies_filter(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        t2 = welltops.stratigraphies["Tarbert2"]
        df = dipAngle.as_dataframe(marker_stratigraphies_filter=[bc, t2])
        assert len(df) == 31

    def test_markerattribute_dataframe_wells_filter_and_stratigraphies_filter(self, welltops, wellb1, wellb2, wellb8):
        dipAngle = welltops.attributes["Dip angle"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        t2 = welltops.stratigraphies["Tarbert2"]
        df = dipAngle.as_dataframe(wells_filter=[wellb1, wellb2, wellb8], marker_stratigraphies_filter=[bc, t2])
        assert len(df) == 6

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_one_stratigraphy_multiple_wells(self, welltops, wellb1, wellb2):
        dipAngle = welltops.attributes["Dip angle"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        df = dipAngle.as_dataframe(marker_stratigraphy=bc, wells_filter=[wellb1, wellb2])
        assert len(df) == 3

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markerattribute_dataframe_one_well_multiple_stratigraphies(self, welltops, wellb8):
        dipAngle = welltops.attributes["Dip angle"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        tn = welltops.stratigraphies["Top Ness"]
        df = dipAngle.as_dataframe(well=wellb8, marker_stratigraphies_filter=[bc, t1, t2, tn])
        assert len(df) == 4

    def test_markerattribute_dataframe_wells_filter_no_list_raises_type_error(self, welltops, wellb8):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(TypeError) as raised_error:
            dipAngle.as_dataframe(wells_filter=wellb8)
        assert raised_error.value.args[0] == "wells_filter must be a list of Well objects as returned from petrelconnection.wells"

    def test_markerattribute_dataframe_wells_filter_bad_list_raises_value_error(self, welltops, wellb1):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(wells_filter=[wellb1, "B2"])
        assert raised_error.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    def test_markerattribute_dataframe_stratigraphies_filter_no_list_raises_type_error(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.raises(TypeError) as raised_error:
            dipAngle.as_dataframe(marker_stratigraphies_filter="Base Cretaceous")
        assert raised_error.value.args[0] == "marker_stratigraphies_filter must be a list of MarkerStratigraphy objects as returned from markercollection.stratigraphies"

    def test_markerattribute_dataframe_stratigraphies_filter_bad_list_raises_value_error(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        with pytest.raises(ValueError) as raised_error:
            dipAngle.as_dataframe(marker_stratigraphies_filter=[bc, "Tarbert2"])
        assert raised_error.value.args[0] == "Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"

    def test_markerattribute_dataframe_well_argument_raises_warning(self, welltops, wellb1):
        dipAngle = welltops.attributes["Dip angle"]
        with pytest.warns(DeprecationWarning) as raised_warning:
            dipAngle.as_dataframe(well=wellb1)
        assert raised_warning.pop(DeprecationWarning).message.args[0] == "The 'well' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'wells_filter' instead."

    def test_markerattribute_dataframe_marker_stratigraphy_argument_raises_warning(self, welltops):
        dipAngle = welltops.attributes["Dip angle"]
        strat = welltops.stratigraphies["Tarbert1"]
        with pytest.warns(DeprecationWarning) as raised_warning:
            dipAngle.as_dataframe(marker_stratigraphy=strat)
        assert raised_warning.pop(DeprecationWarning).message.args[0] == "The 'marker_stratigraphy' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'marker_stratigraphies_filter' instead."