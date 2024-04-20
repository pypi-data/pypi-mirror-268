import pytest
import os
import sys
from cegalprizm.pythontool import exceptions, Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Explicit:
    def test_wellsurvey_explicit_petrel_name(self, well_good_explicit_survey):
        assert well_good_explicit_survey.petrel_name == 'Explicit survey 1'

    def test_wellsurvey_explicit_path(self, well_good_explicit_survey):
        assert well_good_explicit_survey.path == 'Input/Wells/Well_Good/Explicit survey 1'

    def test_wellsurvey_explicit_droid(self, well_good_explicit_survey):
        assert well_good_explicit_survey.droid == '4c1b4291-3b0f-5b86-b348-9ad0943dfd99'

    def test_wellsurvey_explicit_retrieve_history(self, well_good_explicit_survey):
        history_df = well_good_explicit_survey.retrieve_history()
        first_row = history_df.iloc[0, 1:]
        assert first_row['User'] =='toreaa'
        assert first_row['Action'] == 'Upgraded to new well model'
        assert first_row['Description'] == 'DX, DY, TVDSS, MD'

    def test_wellsurvey_explicit_well(self, well_good_explicit_survey):
        well = well_good_explicit_survey.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good'

    def test_wellsurvey_explicit_well_survey_type(self, well_good_explicit_survey):
        assert well_good_explicit_survey.well_survey_type == 'Explicit survey'

    def test_wellsurvey_explicit_azimuth_reference(self, well_good_explicit_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            var = well_good_explicit_survey.azimuth_reference
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "X Y Z well survey, X Y TVD well survey and Explicit survey have no azimuth reference."

    def test_wellsurvey_explicit_record_count(self, well_good_explicit_survey):
        assert well_good_explicit_survey.record_count == 104

    def test_wellsurvey_explicit_as_dataframe(self, well_good_explicit_survey):
        df = well_good_explicit_survey.as_dataframe()
        assert df.columns[0] == 'X'
        assert df.columns[1] == 'Y'
        assert df.columns[2] == 'Z'
        assert df.columns[3] == 'MD'
        assert df.columns[4] == 'Inclination'
        assert df.columns[5] == 'Azimuth GN'
        assert len(df.index) == well_good_explicit_survey.record_count
        df_calculated = well_good_explicit_survey.as_dataframe(get_calculated_trajectory=True)
        assert df_calculated.columns[0] == 'X'
        assert df_calculated.columns[1] == 'Y'
        assert df_calculated.columns[2] == 'Z'
        assert df_calculated.columns[3] == 'MD'
        assert df_calculated.columns[4] == 'Inclination'
        assert df_calculated.columns[5] == 'Azimuth GN'
        assert len(df_calculated.index) == well_good_explicit_survey.record_count

    def test_wellsurvey_explicit_get_algorithm(self, well_good_explicit_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            var = well_good_explicit_survey.algorithm
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "Algorithm can only be retrieved for X Y Z, X Y TVD and DX DY TVD surveys"

    def test_wellsurvey_explicit_set_algorithm(self, well_good_explicit_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            well_good_explicit_survey.algorithm = 'Linearization'
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "Algorithm can only be modified for X Y Z, X Y TVD and DX DY TVD surveys"

    def test_wellsurvey_explicit_set(self, well_good_explicit_survey):
        df = well_good_explicit_survey.as_dataframe()
        df.loc[:,"X"] = df.loc[:,"X"] + 10
        with pytest.raises(exceptions.PythonToolException) as error:
            well_good_explicit_survey.set(xs=df.loc[:,"X"], ys=df.loc[:,"Y"], zs=df.loc[:,"Z"], mds=df.loc[:,"MD"], incls=df.loc[:,"Inclination"], azims=df.loc[:,"Azimuth GN"])
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "Cannot modify records for well survey of type Explicit survey"

    def test_wellsurvey_explicit_clone_copy(self, well_good_explicit_survey, delete_workflow):
        clone = well_good_explicit_survey.clone(well_good_explicit_survey.petrel_name + 'clone_copy', copy_values=True)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == 104
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'Z'
            assert df.columns[3] == 'MD'
            assert df.columns[4] == 'Inclination'
            assert df.columns[5] == 'Azimuth GN'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_explicit_clone_no_copy(self, well_good_explicit_survey, delete_workflow):
        clone = well_good_explicit_survey.clone(well_good_explicit_survey.petrel_name + 'clone_no_copy', copy_values=False)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == 0
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'Z'
            assert df.columns[3] == 'MD'
            assert df.columns[4] == 'Inclination'
            assert df.columns[5] == 'Azimuth GN'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_explicit_template(self, well_good_explicit_survey):
        assert well_good_explicit_survey.template == ''
        
    def test_wellsurvey_explicit_workflow_enabled(self, well_good_explicit_survey, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_good_explicit_survey})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_good_explicit_survey))
        assert unpacked_object.petrel_name == well_good_explicit_survey.petrel_name
        assert unpacked_object.path == well_good_explicit_survey.path
        assert unpacked_object.droid == well_good_explicit_survey.droid

    def test_wellsurvey_explicit_is_calculation_valid(self, well_good_explicit_survey):
    	assert well_good_explicit_survey.is_calculation_valid()
