import pytest
import os
import sys
from cegalprizm.pythontool.observeddata import ObservedDataSet
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestGlobalObservedDataSet:
    def test_global_observed_data_set_droid(self, global_observed_data_set):
        assert global_observed_data_set.droid == '25b53092-15ee-4849-835b-81ab36bd4e4c'

    def test_global_observed_data_set_path(self, global_observed_data_set):
        assert global_observed_data_set.path == 'Input/Wells/Global observed data/Observed data sets/Observed'

    def test_global_observed_data_set_readonly(self, global_observed_data_set):
        assert global_observed_data_set.readonly == True

    def test_global_observed_data_set_petrel_name(self, global_observed_data_set):
        assert global_observed_data_set.petrel_name == 'Observed'

    def test_global_observed_data_set_clone(self, global_observed_data_set, delete_workflow):
        try: 
            clone = global_observed_data_set.clone('clone')
            assert clone.petrel_name == 'clone'
            assert clone.readonly == False
            assert clone.path == 'Input/Wells/Global observed data/Observed data sets/clone'
        finally: 
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_global_observed_data_set_create_observed_data_set(self, cloned_global_observed_data_set, well_good):
        # using a cloned observed_data set to avoid adding a new observed_data to the actual test data - not able to delete the observed data afterwards. but we can delete the cloned observed data set!
        created_observed_data_set = cloned_global_observed_data_set.create_observed_data_set(well_good)
        assert isinstance(created_observed_data_set, ObservedDataSet)
        assert created_observed_data_set.petrel_name == 'datasetclone'
        assert created_observed_data_set.path == 'Input/Wells/Well_Good/datasetclone'
        assert len(created_observed_data_set.droid) == 152
        assert created_observed_data_set.well.petrel_name == 'Well_Good'
        assert str(created_observed_data_set.observed_data) == 'WellObservedData(observed_data_set="ObservedDataSet(petrel_name="datasetclone")")'

    def test_global_observed_data_set_template(self, global_observed_data_set):
        assert global_observed_data_set.template == ''

    def test_global_observed_data_set_workflow_enabled(self, global_observed_data_set, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: global_observed_data_set})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(global_observed_data_set))
        assert unpacked_object.petrel_name == global_observed_data_set.petrel_name
        assert unpacked_object.path == global_observed_data_set.path
        assert unpacked_object.droid == global_observed_data_set.droid
