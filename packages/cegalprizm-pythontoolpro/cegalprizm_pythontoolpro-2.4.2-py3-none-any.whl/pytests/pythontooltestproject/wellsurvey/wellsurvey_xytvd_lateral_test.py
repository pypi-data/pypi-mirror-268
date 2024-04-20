import pytest
import os
import sys
from cegalprizm.pythontool import exceptions, Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Xytvd_Lateral:
    def test_wellsurvey_xytvd_lateral_petrel_name(self, well_good_lateral_xytvd_survey_lateral):
        assert well_good_lateral_xytvd_survey_lateral.petrel_name == 'XYTVD lateral'

    def test_wellsurvey_xytvd_lateral_path(self, well_good_lateral_xytvd_survey_lateral):
        assert well_good_lateral_xytvd_survey_lateral.path == 'Input/Wells/Well_Good lateral/XYTVD lateral' 

    def test_wellsurvey_xytvd_lateral_droid(self, well_good_lateral_xytvd_survey_lateral):
        assert well_good_lateral_xytvd_survey_lateral.droid == '34ee5804-3071-4ba4-b486-575b6b54653c'

    def test_wellsurvey_xytvd_lateral_well(self, well_good_lateral_xytvd_survey_lateral):
        well = well_good_lateral_xytvd_survey_lateral.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good lateral'

    def test_wellsurvey_xytvd_lateral_well_survey_type(self, well_good_lateral_xytvd_survey_lateral):
        assert well_good_lateral_xytvd_survey_lateral.well_survey_type == 'X Y TVD survey'

    def test_wellsurvey_xytvd_lateral_azimuth_reference(self, well_good_lateral_xytvd_survey_lateral):
        with pytest.raises(exceptions.PythonToolException) as error:
            var = well_good_lateral_xytvd_survey_lateral.azimuth_reference
        assert error.type is exceptions.PythonToolException
        assert error.value.args[0] == "X Y Z well survey, X Y TVD well survey and Explicit survey have no azimuth reference."

    def test_wellsurvey_xytvd_lateral_record_count(self, well_good_lateral_xytvd_survey_lateral):
        assert well_good_lateral_xytvd_survey_lateral.record_count == 1

    def test_wellsurvey_xytvd_lateral_getset_algorithm(self, well_good_lateral_xytvd_survey_lateral):
        algorithm = well_good_lateral_xytvd_survey_lateral.algorithm
        assert(algorithm == 'Minimum curvature')
        well_good_lateral_xytvd_survey_lateral.algorithm = 'Linearization'
        algorithm = well_good_lateral_xytvd_survey_lateral.algorithm
        assert(algorithm == 'Linearization')
        well_good_lateral_xytvd_survey_lateral.algorithm = 'Minimum curvature'
        algorithm = well_good_lateral_xytvd_survey_lateral.algorithm
        assert(algorithm == 'Minimum curvature')

    def test_wellsurvey_xytvd_lateral_set(self, well_good_lateral_xytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_xytvd_survey_lateral.clone("clone", copy_values=False)

        xs = [486738.5, 486738.5, 486738.5, 486738.5]
        ys = [6226789.0, 6226789.0, 6226789.0, 6226789.0]
        tvds = [82, 100, 500, 918]

        try:
            clone.set(xs=xs, ys=ys, tvds=tvds)
            clone.tie_in_md = 10
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
            assert df["TVD"][0] == tvds[0]
            assert df["TVD"][1] == pytest.approx(tvds[1])
            assert df["TVD"][2] == pytest.approx(tvds[2])
            assert df["TVD"][3] == pytest.approx(tvds[3])
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 5
            assert df_calculated["Z"][0] == pytest.approx(72)
            assert df_calculated["Z"][4] == pytest.approx(-836)
            assert df_calculated["MD"][0] == pytest.approx(10)
            assert df_calculated["MD"][4] == pytest.approx(918)
            assert df_calculated["Inclination"][0] == 0
            assert df_calculated["Inclination"][4] == 0
            assert df_calculated["Azimuth GN"][0] == 0
            assert df_calculated["Azimuth GN"][4] == pytest.approx(0.18, 0.014)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_xytvd_lateral_set_make_survey_invalid(self, well_good_lateral_xytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_xytvd_survey_lateral.clone('clone', copy_values=False)

        xs = [486738.5, 486738.5, 486738.5, 486738.5]
        ys = [6226789.0, 6226789.0, 6226789.0, 6226789.0]
        tvds = [82.0, 10, 500, 66]

        try:
            clone.set(xs=xs, ys=ys, tvds=tvds)
            assert not clone.is_calculation_valid()
            assert clone.algorithm == 'Minimum curvature'
            df = clone.as_dataframe()
            assert len(df.index) == clone.record_count
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_xytvd_lateral_clone_copy(self, well_good_lateral_xytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_xytvd_survey_lateral.clone(well_good_lateral_xytvd_survey_lateral.petrel_name + 'clone_copy', copy_values=True)
        try:
            df = clone.as_dataframe()
            assert len(df.index) == 1
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'TVD'
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

    def test_wellsurvey_xytvd_lateral_clone_no_copy(self, well_good_lateral_xytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_xytvd_survey_lateral.clone(well_good_lateral_xytvd_survey_lateral.petrel_name + 'clone_no_copy', copy_values=False)
        try:
            df = clone.as_dataframe()
            assert clone.record_count == 0
            assert len(df.index) == 0
            assert df.columns[0] == 'X'
            assert df.columns[1] == 'Y'
            assert df.columns[2] == 'TVD'
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