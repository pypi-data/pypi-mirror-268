import pytest
import os
import sys
from cegalprizm.pythontool import exceptions, Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Mdinclazim:
    def test_wellsurvey_mdinclazim_petrel_name(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.petrel_name == 'MDINCLAZIM'

    def test_wellsurvey_mdinclazim_path(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.path == 'Input/Wells/Well_Good/MDINCLAZIM'

    def test_wellsurvey_mdinclazim_droid(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.droid == '2dc05388-10ac-4019-b166-4089094048ca'

    def test_wellsurvey_mdinclazim_well(self, well_good_mdinclazim_survey):
        well = well_good_mdinclazim_survey.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good'

    def test_wellsurvey_mdinclazim_well_survey_type(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.well_survey_type == 'MD inclination azimuth survey'

    def test_wellsurvey_mdinclazim_azimuth_reference(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.azimuth_reference == 'Grid north'

    def test_wellsurvey_mdinclazim_record_count(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.record_count == 2

    def test_wellsurvey_mdinclazim_get_algorithm(self, well_good_mdinclazim_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            var = well_good_mdinclazim_survey.algorithm
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "Algorithm can only be retrieved for X Y Z, X Y TVD and DX DY TVD surveys"

    def test_wellsurvey_mdinclazim_set_algorithm(self, well_good_mdinclazim_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            well_good_mdinclazim_survey.algorithm = 'Linearization'
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "Algorithm can only be modified for X Y Z, X Y TVD and DX DY TVD surveys"

    def test_wellsurvey_mdinclazim_set(self, well_good_mdinclazim_survey, delete_workflow):
        clone = well_good_mdinclazim_survey.clone('clone', copy_values=False)

        mds = [0, 10, 500, 918]
        incls = [5, 15, 25, 35]
        azims = [10, 20, 30, 40]

        try:
            clone.set(mds=mds, incls=incls, azims=azims)
            assert clone.is_calculation_valid()
            assert clone.azimuth_reference == 'Grid north'
            df = clone.as_dataframe()
            assert df["MD"][0] == mds[0]
            assert df["MD"][1] == pytest.approx(mds[1])
            assert df["MD"][2] == pytest.approx(mds[2])
            assert df["MD"][3] == pytest.approx(mds[3])
            assert df["Inclination"][0] == pytest.approx(incls[0])
            assert df["Inclination"][1] == pytest.approx(incls[1])
            assert df["Inclination"][2] == incls[2]
            assert df["Inclination"][3] == pytest.approx(incls[3])
            assert df["Azimuth GN"][0] == pytest.approx(azims[0])
            assert df["Azimuth GN"][1] == pytest.approx(azims[1])
            assert df["Azimuth GN"][2] == pytest.approx(azims[2])
            assert df["Azimuth GN"][3] == pytest.approx(azims[3])
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 23
            assert df_calculated['X'][0] == pytest.approx(486738.50)
            assert df_calculated['X'][22] == pytest.approx(486798.15)
            assert df_calculated['Y'][0] == 6226789.0
            assert df_calculated['Y'][22] == pytest.approx(6226886.55)
            assert df_calculated['Z'][0] == 82.0
            assert df_calculated['Z'][22] == pytest.approx(-749.59, 0.00001)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_mdinclazim_set_make_survey_invalid(self, well_good_mdinclazim_survey, delete_workflow):
        clone = well_good_mdinclazim_survey.clone('clone', copy_values=False)

        mds = [0]
        incls = [5]
        azims = [10]

        try:
            clone.set(mds=mds, incls=incls, azims=azims)
            assert not clone.is_calculation_valid()
            assert clone.azimuth_reference == 'Grid north'
            df = clone.as_dataframe()
            assert len(df.index) == clone.record_count
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_mdinclazim_clone_copy(self, well_good_mdinclazim_survey, delete_workflow):
        clone = well_good_mdinclazim_survey.clone(well_good_mdinclazim_survey.petrel_name + 'clone_copy', copy_values=True)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == 2
            assert df.columns[0] == 'MD'
            assert df.columns[1] == 'Inclination'
            assert df.columns[2] == 'Azimuth GN'
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) >= clone.record_count
            assert df_calculated.columns[0] == 'X'
            assert df_calculated.columns[1] == 'Y'
            assert df_calculated.columns[2] == 'Z'
            assert df_calculated.columns[3] == 'MD'
            assert df_calculated.columns[4] == 'Inclination'
            assert df_calculated.columns[5] == 'Azimuth GN'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_mdinclazim_clone_no_copy(self, well_good_mdinclazim_survey, delete_workflow):
        clone = well_good_mdinclazim_survey.clone(well_good_mdinclazim_survey.petrel_name + 'clone_no_copy', copy_values=False)
        try:
            df = clone.as_dataframe()
            assert clone.record_count == 0
            assert len(df.index) == 0
            assert df.columns[0] == 'MD'
            assert df.columns[1] == 'Inclination'
            assert df.columns[2] == 'Azimuth GN'
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 0
            assert df_calculated.columns[0] == 'X'
            assert df_calculated.columns[1] == 'Y'
            assert df_calculated.columns[2] == 'Z'
            assert df_calculated.columns[3] == 'MD'
            assert df_calculated.columns[4] == 'Inclination'
            assert df_calculated.columns[5] == 'Azimuth GN'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_mdinclazim_template(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.template == ''
        
    def test_wellsurvey_mdinclazim_workflow_enabled(self, well_good_mdinclazim_survey, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_good_mdinclazim_survey})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_good_mdinclazim_survey))
        assert unpacked_object.petrel_name == well_good_mdinclazim_survey.petrel_name
        assert unpacked_object.path == well_good_mdinclazim_survey.path
        assert unpacked_object.droid == well_good_mdinclazim_survey.droid

    def test_wellsurvey_mdinclazim_is_calculation_valid_True(self, well_good_mdinclazim_survey):
        assert well_good_mdinclazim_survey.is_calculation_valid()

    def test_wellsurvey_mdinclazim_is_calculation_valid_False(self, well_good_mdinclazim_invalid_survey):
        assert not well_good_mdinclazim_invalid_survey.is_calculation_valid()