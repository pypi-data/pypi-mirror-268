import math
import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionDataframe:
    def test_markercollection_dataframe_petrel_index(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['Petrel index'][0] == 1
        assert dataframe['Petrel index'][9] == 10
        assert dataframe['Petrel index'][99] == 100
        assert dataframe['Petrel index'][101] == 102
        assert dataframe['Petrel index'][104] == 105

    def test_markercollection_dataframe_no_petrel_index(self, welltops):
        dataframe = welltops.as_dataframe(include_petrel_index=False)
        with pytest.raises(KeyError) as an_error:
            dataframe["Petrel index"]
        assert an_error.type is KeyError

    def test_markercollection_dataframe_md(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['MD'][2] == 1805.45
        assert dataframe['MD'][8] == 1998.97
        assert dataframe['MD'][99] == 2111.52
        assert dataframe['MD'][104] == 1858.57

    def test_markercollection_dataframe_fluvial_facies(self, welltops):
        dataframe = welltops.as_dataframe()
        assert dataframe['Fluvial facies'][8] == 99.0
        assert dataframe['Fluvial facies'][99] == 40.0
        assert math.isnan(dataframe['Fluvial facies'][1])

    def test_markercollection_dataframe_uc_markers_false_petrel_index(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['Petrel index'][0] == 4

    def test_markercollection_dataframe_uc_markers_false_well_id(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['Well identifier (Well name)'][4] == 'B1'

    def test_markercollection_dataframe_uc_markers_false_md(self, welltops):
        dataframe = welltops.as_dataframe(False)
        assert dataframe['MD'][0] == 2012.93

    def test_markercollection_dataframe_uc_markers_true_md(self, welltops):
        dataframe = welltops.as_dataframe(True)
        assert dataframe['MD'][2] == 1805.45

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_strat_filter_md(self, welltops):
        stratigraphy = welltops.stratigraphies["Base Cretaceous"]
        dataframe = welltops.as_dataframe(True, stratigraphy)
        assert dataframe['MD'][0] == 1858.55
        assert dataframe['MD'][1] == 1879.35
        assert dataframe['Petrel index'][0] == 1
        assert dataframe['Petrel index'][17] == 82

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_well_filter_bad_input_raises_value_error(self, welltops):
        with pytest.raises(ValueError) as raised_error:
            welltops.as_dataframe(True, None, "NotOk")
        assert raised_error.type is ValueError
        assert raised_error.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_well_filter(self, welltops, wellb1):
        dataframe = welltops.as_dataframe(True, None, wellb1)
        assert dataframe['MD'][0] == 1831.03
        assert dataframe['MD'][1] == 1864.8
        assert dataframe['Petrel index'][0] == 15
        assert dataframe['Petrel index'][7] == 97

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_strat_and_well_filter(self, welltops, wellb1):
        stratigraphy = welltops.stratigraphies["Top Ness"]
        dataframe = welltops.as_dataframe(True, stratigraphy, wellb1)
        assert dataframe['MD'][0] == 1949.68
        assert dataframe['MD'][1] == 1949.68
        assert dataframe['Petrel index'][0] == 28
        assert dataframe['Petrel index'][1] == 95

    def test_markercollection_dataframe_attribute_filter_bad_input(self, welltops):
        with pytest.raises(TypeError) as raised_error:
            welltops.as_dataframe(marker_attributes_filter=["NotOk", 123, None])
        assert raised_error.type is TypeError
        assert raised_error.value.args[0] == "All entries in marker_attributes_filter must be a MarkerAttribute object as returned from markercollection.attributes"

    def test_markercollection_dataframe_attribute_filter_mixed_input(self, welltops):
        md_att = welltops.attributes["MD"]
        att_list = [md_att, 123]
        with pytest.raises(TypeError) as raised_error:
            welltops.as_dataframe(marker_attributes_filter=att_list)
        assert raised_error.type is TypeError
        assert raised_error.value.args[0] == "All entries in marker_attributes_filter must be a MarkerAttribute object as returned from markercollection.attributes"

    def test_markercollection_dataframe_attribute_filter_three_attributes(self, welltops):
        md_att = welltops.attributes["MD"]
        interp_att = welltops.attributes["Interpreter"]
        obs_att = welltops.attributes["Observation number"]
        att_list = [md_att, interp_att, obs_att]
        df = welltops.as_dataframe(marker_attributes_filter=att_list)
        assert df is not None
        assert len(df) >= 105
        assert len(df.columns) == 9

    def test_markercollection_dataframe_attribute_filter_one_continous_attribute(self, welltops):
        md_att = welltops.attributes["MD"]
        att_list = [md_att]
        df = welltops.as_dataframe(marker_attributes_filter=att_list)
        assert df is not None
        assert len(df) >= 105
        assert len(df.columns) == 7
        assert len(df["MD"]) >= 105

    def test_markercollection_dataframe_attribute_filter_two_discrete_attributes(self, welltops):
        interp_att = welltops.attributes["Interpreter"]
        obs_att = welltops.attributes["Observation number"]
        att_list = [interp_att, obs_att]
        df = welltops.as_dataframe(marker_attributes_filter=att_list)
        assert df is not None
        assert len(df) >= 105
        assert len(df.columns) == 8
        with pytest.raises(KeyError) as raised_error:
            df["MD"]
        assert raised_error.type is KeyError
        assert len(df["Interpreter"]) >= 105

    def test_markercollection_dataframe_attribute_filter_suffix(self, welltops, delete_workflow):
        try:
            welltops.readonly = False
            import numpy as np
            empty = np.array([])
            welltops.add_attribute(empty, "StringSuffix", "string")
            welltops.add_attribute(empty, "StringSuffix", "string")
            welltops.add_attribute(empty, "StringSuffix", "string")
            a1 = welltops.attributes["StringSuffix (1)"]
            a2 = welltops.attributes["StringSuffix (2)"]
            a3 = welltops.attributes["StringSuffix (3)"]
            df23 = welltops.as_dataframe(marker_attributes_filter=[a2,a3])
            with pytest.raises(KeyError) as raised_error:
                df23["StringSuffix"]
            with pytest.raises(KeyError) as raised_error:
                df23["StringSuffix (1)"]
            assert len(df23["StringSuffix (2)"]) >= 105
            assert len(df23["StringSuffix (3)"]) >= 105
            df1 = welltops.as_dataframe(marker_attributes_filter=[a1])
            assert len(df1["StringSuffix (1)"]) >= 105
            with pytest.raises(KeyError) as raised_error:
                df1["StringSuffix"]
            with pytest.raises(KeyError) as raised_error:
                df1["StringSuffix (2)"]
            with pytest.raises(KeyError) as raised_error:
                df1["StringSuffix (3)"]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: a1})
            delete_workflow.run({obj: a2})
            delete_workflow.run({obj: a3})
        
    def test_markercollection_dataframe_attribute_filter_no_attributes(self, welltops):
        df = welltops.as_dataframe(marker_attributes_filter=[])
        assert df is not None
        assert len(df) >= 105
        assert len(df.columns) == 6
        with pytest.raises(KeyError) as raised_error:
            df["MD"]
        assert raised_error.type is KeyError
        assert len(df["Surface"]) >= 105

    def test_markercollection_dataframe_attribute_filter_no_filter(self, welltops):
        df = welltops.as_dataframe()
        assert df is not None
        assert len(df) >= 105
        assert len(df.columns) >= 35
        assert len(df["Surface"]) >= 105
        assert len(df["MD"]) >= 105

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_one_new_attribute(self, welltops, wellb2, delete_workflow):
        try:
            welltops.readonly = False
            import numpy as np
            strings = np.array(["1","2","3","4","5","6"])
            uniqueName = "Attribute_One"
            welltops.add_attribute(strings, uniqueName, "string", False, None, wellb2)
            dataframe = welltops.as_dataframe(False, None, wellb2)
            assert dataframe[uniqueName][0] == "1"
            assert dataframe[uniqueName][5] == "6"
            att = welltops.attributes["Attribute_One"]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: att})

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_two_new_attributes(self, welltops, wellb2, delete_workflow):
        try:
            welltops.readonly = False
            import numpy as np
            strings = np.array(["1","2","3","4","5","6"])
            otherStrings = np.array(["21","22","23","24","25","26"])
            notUniqueName = "Attribute_Two"
            welltops.add_attribute(strings, notUniqueName, "string", False, None, wellb2)
            welltops.add_attribute(otherStrings, notUniqueName, "string", False, None, wellb2)
            dataframe = welltops.as_dataframe(False, None, wellb2)
            with pytest.raises(KeyError) as keyError:
                doesnotwork = dataframe[notUniqueName]
            assert keyError.type is KeyError
            assert dataframe[notUniqueName + " (1)"][1] == "2"
            assert dataframe[notUniqueName + " (1)"][5] == "6"
            assert dataframe[notUniqueName + " (2)"][1] == "22"
            assert dataframe[notUniqueName + " (2)"][5] == "26"
            a1 = welltops.attributes["Attribute_Two (1)"]
            a2 = welltops.attributes["Attribute_Two (2)"]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: a1})
            delete_workflow.run({obj: a2})

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_wells_filter_and_well_raises_value_error(self, welltops, wellb2):
        with pytest.raises(ValueError) as raised_error:
            welltops.as_dataframe(well=wellb2, wells_filter=[wellb2])
        assert raised_error.value.args[0] == "The well and wells_filter arguments cannot be used at the same time"

    def test_markercollection_dataframe_wells_filter_not_a_list_raises_type_error(self, welltops):
        with pytest.raises(TypeError) as raised_error:
            welltops.as_dataframe(wells_filter="bad input")
        assert raised_error.value.args[0] == "wells_filter must be a list of Well objects as returned from petrelconnection.wells"

    def test_markercollection_dataframe_wells_filter_mixed_list_raises_value_error(self, welltops, wellb2):
        with pytest.raises(ValueError) as raised_error:
            welltops.as_dataframe(wells_filter=[wellb2, "bad input"])
        assert raised_error.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    def test_markercollection_dataframe_wells_filter_empty_gives_all_wells(self, welltops):
        df = welltops.as_dataframe(wells_filter=[])
        assert df is not None
        assert len(df) == 105
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 105

    def test_markercollection_dataframe_wells_filter_one_well(self, welltops, wellb2):
        df = welltops.as_dataframe(wells_filter=[wellb2])
        assert df is not None
        assert len(df) == 6
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 6

    def test_markercollection_dataframe_wells_filter_two_wells(self, welltops, wellb2, wellb1):
        df = welltops.as_dataframe(wells_filter=[wellb2, wellb1])
        assert df is not None
        assert len(df) == 14
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 14

    def test_markercollection_dataframe_wells_filter_two_wells_one_none(self, welltops, wellb2, wellb1):
        df = welltops.as_dataframe(wells_filter=[None, wellb2, wellb1])
        assert df is not None
        assert len(df) == 14
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 14

    def test_markercollection_dataframe_wells_filter_three_wells(self, welltops, wellb1, wellb2, wellb8):
        df = welltops.as_dataframe(wells_filter=[wellb1, wellb2, wellb8])
        assert df is not None
        assert len(df) == 21
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 21

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_stratigraphies_filter_and_stratigrapy_raises_value_error(self, welltops):
        t1 = welltops.stratigraphies["Tarbert1"]
        with pytest.raises(ValueError) as raised_error:
            welltops.as_dataframe(marker_stratigraphy=t1, marker_stratigraphies_filter=[t1])
        assert raised_error.value.args[0] == "The marker_stratigraphy and marker_stratigraphies_filter arguments cannot be used at the same time"

    def test_markercollection_dataframe_stratigraphies_filter_not_a_list_raises_type_error(self, welltops):
        with pytest.raises(TypeError) as raised_error:
            welltops.as_dataframe(marker_stratigraphies_filter="bad input")
        assert raised_error.value.args[0] == "marker_stratigraphies_filter must be a list of MarkerStratigraphy objects as returned from markercollection.stratigraphies"

    def test_markercollection_dataframe_stratigraphies_filter_mixed_list_raises_value_error(self, welltops):
        t1 = welltops.stratigraphies["Tarbert1"]
        with pytest.raises(ValueError) as raised_error:
            welltops.as_dataframe(marker_stratigraphies_filter=[t1, "bad input"])
        assert raised_error.value.args[0] == "Each marker_stratigraphy must be a MarkerStratigraphy object as returned from markercollection.stratigraphies"

    def test_markercollection_dataframe_stratigraphies_filter_empty_gives_all_stratigraphies(self, welltops):
        df = welltops.as_dataframe(marker_stratigraphies_filter=[])
        assert df is not None
        assert len(df) == 105
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 105

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_stratigraphies_filter_one_stratigraphy(self, welltops):
        t1 = welltops.stratigraphies["Tarbert1"]
        df = welltops.as_dataframe(marker_stratigraphy=t1)
        assert df is not None
        assert len(df) == 14
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 14

    def test_markercollection_dataframe_stratigraphies_filter_two_stratigraphies(self, welltops):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        df = welltops.as_dataframe(marker_stratigraphies_filter=[t1, t2])
        assert df is not None
        assert len(df) == 27
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 27

    def test_markercollection_dataframe_stratigraphies_filter_three_stratigraphies(self, welltops):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        df = welltops.as_dataframe(marker_stratigraphies_filter=[t1, t2, bc])
        assert df is not None
        assert len(df) == 45
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 45

    def test_markercollection_dataframe_wells_and_stratigraphies_filter(self, welltops, wellb1, wellb2):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        df = welltops.as_dataframe(wells_filter=[wellb1, wellb2], marker_stratigraphies_filter=[t1, t2, bc])
        assert df is not None
        assert len(df) == 5
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 5

    def test_markercollection_dataframe_wells_stratigraphies_attributes_filter(self, welltops, wellb1, wellb2, wellb8):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        z = welltops.attributes["Z"]
        md = welltops.attributes["MD"]
        df = welltops.as_dataframe(wells_filter=[wellb1, wellb2, wellb8], 
                                   marker_stratigraphies_filter=[t1, t2, bc], 
                                   marker_attributes_filter=[z, md])
        assert df is not None
        assert len(df) == 8
        assert len(df.columns) == 8
        assert len(df["MD"]) == 8

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_one_stratigraphy_multiple_wells(self, welltops, wellb1, wellb2, wellb8):
        t1 = welltops.stratigraphies["Tarbert1"]
        df = welltops.as_dataframe(marker_stratigraphy = t1, wells_filter=[wellb1, wellb2, wellb8])
        assert df is not None
        assert len(df) == 2
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 2

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_dataframe_one_well_multiple_stratigraphies(self, welltops, wellb1):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        df = welltops.as_dataframe(well = wellb1, marker_stratigraphies_filter=[t1, t2, bc])
        assert df is not None
        assert len(df) == 2
        assert len(df.columns) >= 35
        assert len(df["MD"]) == 2

    def test_markercollection_dataframe_everything_filter(self, welltops, wellb1, wellb2, wellb8):
        t1 = welltops.stratigraphies["Tarbert1"]
        t2 = welltops.stratigraphies["Tarbert2"]
        bc = welltops.stratigraphies["Base Cretaceous"]
        porosity = welltops.attributes["Porosity"]
        df = welltops.as_dataframe(include_unconnected_markers = False,
                                   include_petrel_index = False,
                                   wells_filter=[wellb1, wellb2, wellb8],
                                   marker_stratigraphies_filter=[t1, t2, bc],
                                   marker_attributes_filter=[porosity])
        assert df is not None
        assert len(df) == 8
        assert len(df.columns) == 6
        assert len(df["Porosity"]) == 8
        with pytest.raises(KeyError):
            df["MD"]

    def test_markercollection_dataframe_well_argument_raises_warning(self, welltops, wellb1):
        with pytest.warns(DeprecationWarning) as raised_warning:
            welltops.as_dataframe(well=wellb1)
        assert raised_warning.pop(DeprecationWarning).message.args[0] == "The 'well' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'wells_filter' instead."

    def test_markercollection_dataframe_marker_stratigraphy_argument_raises_warning(self, welltops):
        strat = welltops.stratigraphies["Tarbert1"]
        with pytest.warns(DeprecationWarning) as raised_warning:
            welltops.as_dataframe(marker_stratigraphy=strat)
        assert raised_warning.pop(DeprecationWarning).message.args[0] == "The 'marker_stratigraphy' argument is deprecated and will be removed in Python Tool Pro version 3.0. Use 'marker_stratigraphies_filter' instead."