import pytest
import os
import sys
from cegalprizm.pythontool import exceptions, Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Xyz:
    def test_wellsurvey_xyz_petrel_name(self, well_good_xyz_survey):
        assert well_good_xyz_survey.petrel_name == 'XYZ'

    def test_wellsurvey_xyz_path(self, well_good_xyz_survey):
        assert well_good_xyz_survey.path == 'Input/Wells/Well_Good/XYZ'

    def test_wellsurvey_xyz_droid(self, well_good_xyz_survey):
        assert well_good_xyz_survey.droid == '752f79f0-de4a-4b12-91ae-b914a02d825e'

    def test_wellsurvey_xyz_well(self, well_good_xyz_survey):
        well = well_good_xyz_survey.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good'

    def test_wellsurvey_xyz_well_survey_type(self, well_good_xyz_survey):
        assert well_good_xyz_survey.well_survey_type == 'X Y Z survey'

    def test_wellsurvey_xyz_azimuth_reference(self, well_good_xyz_survey):
        with pytest.raises(exceptions.PythonToolException) as error:
            var = well_good_xyz_survey.azimuth_reference
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "X Y Z well survey, X Y TVD well survey and Explicit survey have no azimuth reference."

    def test_wellsurvey_xyz_record_count(self, well_good_xyz_survey):
        assert well_good_xyz_survey.record_count == 2

    def test_wellsurvey_xyz_getset_algorithm(self, well_good_xyz_survey):
        algorithm = well_good_xyz_survey.algorithm
        assert(algorithm == 'Minimum curvature')
        well_good_xyz_survey.algorithm = 'Linearization'
        algorithm = well_good_xyz_survey.algorithm
        assert(algorithm == 'Linearization')
        well_good_xyz_survey.algorithm = 'Minimum curvature'
        algorithm = well_good_xyz_survey.algorithm
        assert(algorithm == 'Minimum curvature')

    def test_wellsurvey_xyz_set_algorithm_wrong_string(self, well_good_xyz_survey):
        with pytest.raises(ValueError) as error:
            well_good_xyz_survey.algorithm = 'abcdefg'
        assert error.type is ValueError
        assert error.value.args[0] == "Algorithm must be set to either 'Minimum curvature' or 'Linearization'"

    def test_wellsurvey_xyz_set(self, well_good_xyz_survey, delete_workflow):
        clone = well_good_xyz_survey.clone('clone', copy_values=False)

        xs = [486738.5, 486738.5, 486738.5, 486738.5]
        ys = [6226789.0, 6226789.0, 6226789.0, 6226789.0]
        zs = [82.0, 10, -500, -918]

        try:
            clone.set(xs=xs, ys=ys, zs=zs)
            assert clone.is_calculation_valid()
            assert clone.algorithm == 'Minimum curvature'
            df = clone.as_dataframe()
            assert df["X"][0] == xs[0]
            assert df["X"][1] == xs[1]
            assert df["X"][2] == xs[2]
            assert df["X"][3] == xs[3]
            assert df["Y"][0] == ys[0]
            assert df["Y"][1] == ys[1]
            assert df["Y"][2] == ys[2]
            assert df["Y"][3] == ys[3]
            assert df["Z"][0] == zs[0]
            assert df["Z"][1] == pytest.approx(zs[1])
            assert df["Z"][2] == pytest.approx(zs[2])
            assert df["Z"][3] == pytest.approx(zs[3])
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 4
            assert df_calculated['MD'][0] == 0
            assert df_calculated['MD'][3] == pytest.approx(1000)
            assert df_calculated['Inclination'][0] == 0
            assert df_calculated['Inclination'][3] == 0
            assert df_calculated['Azimuth GN'][0] == 0
            assert df_calculated['Azimuth GN'][3] == pytest.approx(0.18, 0.014)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_xyz_set_make_survey_invalid(self, well_good_xyz_survey, delete_workflow):
        clone = well_good_xyz_survey.clone('clone', copy_values=False)

        xs = [486738.5, 486738.5, 486738.5, 486738.5]
        ys = [6226789.0, 6226789.0, 6226789.0, 6226789.0]
        zs = [82.0, 10, 500, -918]

        try:
            clone.set(xs=xs, ys=ys, zs=zs)
            assert not clone.is_calculation_valid()
            assert clone.algorithm == 'Minimum curvature'
            df = clone.as_dataframe()
            assert len(df.index) == clone.record_count
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_xyz_clone_copy(self, well_good_xyz_survey, delete_workflow):
        clone = well_good_xyz_survey.clone(well_good_xyz_survey.petrel_name + 'clone_copy', copy_values=True)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == clone.record_count
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'Z'
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

    def test_wellsurvey_xyz_clone_no_copy(self, well_good_xyz_survey, delete_workflow):
        clone = well_good_xyz_survey.clone(well_good_xyz_survey.petrel_name + 'clone_no_copy', copy_values=False)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == 0
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'Z'
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

    def test_wellsurvey_xyz_template(self, well_good_xyz_survey):
        assert well_good_xyz_survey.template == ''

    def test_wellsurvey_xyz_workflow_enabled(self, well_good_xyz_survey, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_good_xyz_survey})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_good_xyz_survey))
        assert unpacked_object.petrel_name == well_good_xyz_survey.petrel_name
        assert unpacked_object.path == well_good_xyz_survey.path
        assert unpacked_object.droid == well_good_xyz_survey.droid
        
    def test_wellsurvey_xyz_is_calculation_valid_True(self, well_good_xyz_survey):
        assert well_good_xyz_survey.is_calculation_valid()

    def test_wellsurvey_xyz_is_calculation_valid_False(self, well_good_xyz_invalid_survey):
        assert not well_good_xyz_invalid_survey.is_calculation_valid()