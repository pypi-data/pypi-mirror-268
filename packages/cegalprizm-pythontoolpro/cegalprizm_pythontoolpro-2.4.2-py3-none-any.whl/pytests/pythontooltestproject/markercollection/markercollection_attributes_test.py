import math
import numpy as np
import pandas as pd
import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject
from cegalprizm.pythontool.markerattribute import MarkerAttribute

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestMarkerCollectionAttributes:
    def test_markercollection_attributes_repr(self, welltops):
        assert welltops is not None
        assert welltops.attributes is not None
        z = welltops.attributes["Z"]
        assert z is not None
        represent = repr(welltops.attributes["Z"])
        assert represent == "MarkerAttribute(\"Z\")"

    def test_markercollection_attributes_readonly(self, welltops):
        welltops.readonly = True
        from cegalprizm.pythontool.exceptions import PythonToolException
        import numpy as np
        array = np.empty(2)
        with pytest.raises(PythonToolException) as exceptionInfo:
            welltops.attributes["Z"].set_values(array)
        assert exceptionInfo.type is PythonToolException
        assert exceptionInfo.value.args[0] == "MarkerCollection is readonly"
        welltops.readonly = False

    def test_markercollection_attributes_parent(self, welltops):
        z = welltops.attributes["Z"]
        assert z.markercollection == welltops

    def test_markercollection_attributes_len(self, welltops):
        assert len(welltops.attributes) >= 29

    def test_markercollection_attributes_get_none(self, welltops):
        assert welltops.attributes[None] is None

    def test_markercollection_attributes_get_by_name(self, welltops):
        crevasse = welltops.attributes["Crevasse"]
        assert isinstance(crevasse, MarkerAttribute)
        assert crevasse._name == "Crevasse"

    def test_markercollection_attributes_get_by_index(self, welltops):
        md = welltops.attributes[4]
        assert isinstance(md, MarkerAttribute)
        assert md._name == "MD"

    def test_markercollection_attributes_get_by_index_out_of_range(self, welltops):
        with pytest.raises(IndexError) as error:
            welltops.attributes[100]
        assert error.type is IndexError
        assert "index out of range" in error.value.args[0]

    def test_markercollection_attributes_get_by_index_negative(self, welltops):
        from_the_end = welltops.attributes[-1]
        assert isinstance(from_the_end, MarkerAttribute)

    def test_markercollection_attributes_get_by_index_bad_type(self, welltops):
        nothing = welltops.attributes[2.3456]
        assert nothing is None

    def test_markercollection_attribute_as_array(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        assert str(geoAge) == "MarkerAttribute(\"Geological age\")"
        arr = geoAge.as_array(False)
        assert math.isnan(arr[0])
        assert arr[20] == 65.5

    def test_markercollection_attribute_set_values_empty_array(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        emptyData = np.array([])
        with pytest.raises (ValueError) as it_failed:
            geoAge.set_values(emptyData, False)
        assert it_failed.type is ValueError
        assert it_failed.value.args[0] == "Input array does not contain any values"

    def test_markercollection_attribute_set_values_too_short_skip_unconnected(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        tooShortData = np.array([1.1,2.2,3.3])
        with pytest.raises (ValueError) as it_failed:
            geoAge.set_values(tooShortData, False)
        assert it_failed.type is ValueError
        assert it_failed.value.args[0] == "Number of elements in array must match number of markers in markercollection"

    def test_markercollection_attribute_set_values_too_short_include_unconnected(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        tooShortData = np.array([1.1,2.2,3.3])
        with pytest.raises (ValueError) as it_failed:
            geoAge.set_values(tooShortData, True)
        assert it_failed.type is ValueError
        assert it_failed.value.args[0] == "Number of elements in array must match number of markers in markercollection"

    def test_markercollection_attribute_set_values_incorrect_data_type(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        badData = np.array([10,20,30,40,50,60,70,80,90,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9])
        with pytest.raises (ValueError) as it_failed:
            geoAge.set_values(badData, False)
        assert it_failed.type is ValueError
        assert it_failed.value.args[0] == "Input data type does not match expected data type"

    def test_markercollection_attribute_update_float_values(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        newData = np.array([2.1, 3.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10,11,12,13,14,15,16,17,18,19,20.9,21.8,22.7,23.6,24.5,25.4,26.3,27.2,28.1,29.0])
        data_before = geoAge.as_array()
        assert data_before[0] != 2.1
        assert data_before[19] != 20.9
        geoAge.set_values(newData, False)
        arr = geoAge.as_array(False)
        assert arr[0] == 2.1
        assert arr[19] == 20.9
        geoAge.set_values(data_before, True)

    def test_markercollection_attribute_update_string_value(self, welltops):
        interp = welltops.attributes['Interpreter']
        data_before = interp.as_array()
        interpArr = interp.as_array(False)
        assert interpArr[4] == "marit"
        assert interpArr[10] == ""
        interpArr[10] = "ptpUser"
        interp.set_values(interpArr, False)
        newInterpArr = interp.as_array(False)
        assert newInterpArr[10] == "ptpUser"
        interp.set_values(data_before)

    def test_markercollection_attribute_update_bool_value(self, welltops):
        geoMod = welltops.attributes['Used by geo mod']
        data_before = geoMod.as_array()
        geoModArr = geoMod.as_array(False)
        assert geoModArr[0] == True
        assert geoModArr[4] == True
        geoModArr[0] = False
        geoMod.set_values(geoModArr, False)
        newGeoModArr = geoMod.as_array(False)
        assert newGeoModArr[0] == False
        geoMod.set_values(data_before)

    def test_markercollection_attribute_update_discrete_value(self, welltops):
        obsNr = welltops.attributes['Observation number']
        data_before = obsNr.as_array()
        assert isinstance(data_before[1], type(pd.NA))
        newData = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29])
        obsNr.set_values(newData, False)
        obsNrArray = obsNr.as_array(False)
        assert obsNrArray[1] == 2
        obsNr.set_values(data_before)

    def test_markercollection_attribute_update_value_stratigraphy_filter(self, welltops):
        myStrat = welltops.stratigraphies[0]
        geoAge = welltops.attributes["Geological age"]
        data_before = geoAge.as_array()
        # First set some values without filter to have some data to work with
        newData = np.array([2.1, 3.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10,11,12,13,14,15,16,17,18,19,20.9,21.8,22.7,23.6,24.5,25.4,26.3,27.2,28.1,29.0])
        geoAge.set_values(newData, False)

        geoArray = geoAge.as_array(False, myStrat)
        assert geoArray[1] == 3.2
        
        arr = geoAge.as_array(False, myStrat)
        for i in range(len(arr)):
            arr[i] = 12.3 + i
        geoAge.set_values(arr, False, myStrat)
        newGeoArray = geoAge.as_array(False, myStrat)
        assert newGeoArray[1] == 13.3
        geoAge.set_values(data_before)

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_attribute_update_value_well_and_stratigraphy_filter(self, welltops, wellb1):
        myStrat = welltops.stratigraphies[0]
        geoAge = welltops.attributes["Geological age"]
        data_before = geoAge.as_array()
        arr = geoAge.as_array(False, myStrat, wellb1)
        assert math.isnan(arr[0])
        onlyTwoValues = np.array([101.11,202.22])
        geoAge.set_values(onlyTwoValues, False, myStrat, wellb1)
        gdf = geoAge.as_dataframe(False, myStrat, wellb1)
        assert gdf['Value'][0] == 101.11
        assert gdf['Value'][1] == 202.22
        geoAge.set_values(data_before)

    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_markercollection_attribute_filter_on_well(self, welltops, wellb1):
        geoAge = welltops.attributes["Geological age"]
        gdf = geoAge.as_dataframe(False, None, wellb1)
        assert gdf['Value'][5] == 65.5

    def test_markercollection_attribute_filter_on_well_bad_input(self, welltops):
        myStrat = welltops.stratigraphies[0]
        geoAge = welltops.attributes["Geological age"]
        with pytest.raises(ValueError) as raised_error:
            geoAge.as_array(True, myStrat, myStrat)
        assert raised_error.type is ValueError
        assert raised_error.value.args[0] == "Each well input must be a Well object as returned from petrelconnection.wells"

    def test_markercollection_attribute_template(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        assert geoAge.template == 'Geological time scale'

    def test_markercollection_attribute_get_template(self, welltops):
        geoAge = welltops.attributes["Geological age"]
        from cegalprizm.pythontool.template import Template
        template = geoAge.get_template()
        assert isinstance(template, Template)
        assert template.unit_symbol == 'Ma'

    def test_markercollection_attribute_workflow_enabled(self, welltops, return_workflow):
        geoAge = welltops.attributes["Geological age"]
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: geoAge})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(geoAge))
        assert unpacked_object.petrel_name == geoAge.petrel_name
        assert unpacked_object.path == geoAge.path
        assert unpacked_object.droid == geoAge.droid

    def test_markercollection_dictionary_attribute_workflow_enabled(self, welltops, return_workflow):
        depthconv = welltops.attributes["Used by dep.conv."]
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: depthconv})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(depthconv))
        assert unpacked_object.petrel_name == depthconv.petrel_name
        assert unpacked_object.path == depthconv.path
        assert unpacked_object.droid == depthconv.droid

    def test_markercollection_attribute_duplicated_name_workflow_enabled(self, welltops, return_workflow, delete_workflow):
        try:
            strat = welltops.stratigraphies["Top Tarbert"]
            geoAgeData = welltops.attributes["Geological age"].as_array(marker_stratigraphy=strat)
            for i in range(len(geoAgeData)):
                geoAgeData[i] = geoAgeData[i] + 4.56
            welltops.add_attribute(data=geoAgeData, name="Geological age", data_type="continuous", marker_stratigraphy=strat)
            geoAge1 = welltops.attributes["Geological age (1)"]
            geoAge2 = welltops.attributes["Geological age (2)"]

            input_var = return_workflow.input["input_object"]
            output_var = return_workflow.output["output_object"]
            wf_result = return_workflow.run({input_var: geoAge1})
            unpacked1 = wf_result[output_var]
            wf_result = return_workflow.run({input_var: geoAge2})
            unpacked2 = wf_result[output_var]

            assert isinstance(unpacked1, type(geoAge1))
            assert isinstance(unpacked2, type(geoAge2))
            assert unpacked1.petrel_name == geoAge1.petrel_name
            assert unpacked2.petrel_name == geoAge2.petrel_name
            assert unpacked1.path == geoAge1.path
            assert unpacked2.path == geoAge2.path
            assert unpacked1.droid == geoAge1.droid
            assert unpacked2.droid == geoAge2.droid
            assert unpacked1.droid != unpacked2.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: geoAge2})
