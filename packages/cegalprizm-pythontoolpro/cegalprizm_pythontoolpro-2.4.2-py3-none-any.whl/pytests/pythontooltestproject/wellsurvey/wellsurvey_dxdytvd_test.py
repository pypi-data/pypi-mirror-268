import pytest
import os
import sys
from cegalprizm.pythontool import Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Dxdytvd:
    def test_wellsurvey_dxdytvd_petrel_name(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.petrel_name == 'DXDYTVD'

    def test_wellsurvey_dxdytvd_path(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.path == 'Input/Wells/Well_Good/DXDYTVD'

    def test_wellsurvey_dxdytvd_droid(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.droid == '7d5a9a2c-37d9-40e7-942f-ec146b0fa3f0'

    def test_wellsurvey_dxdytvd_well(self, well_good_dxdytvd_survey):
        well = well_good_dxdytvd_survey.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good'

    def test_wellsurvey_dxdytvd_well_survey_type(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.well_survey_type == 'DX DY TVD survey'

    def test_wellsurvey_dxdytvd_azimuth_reference(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.azimuth_reference == 'Grid north'

    def test_wellsurvey_dxdytvd_record_count(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.record_count == 2

    def test_wellsurvey_dxdytvd_getset_algorithm(self, well_good_dxdytvd_survey):
        algorithm = well_good_dxdytvd_survey.algorithm
        assert(algorithm == 'Minimum curvature')
        well_good_dxdytvd_survey.algorithm = 'Linearization'
        algorithm = well_good_dxdytvd_survey.algorithm
        assert(algorithm == 'Linearization')
        well_good_dxdytvd_survey.algorithm = 'Minimum curvature'
        algorithm = well_good_dxdytvd_survey.algorithm
        assert(algorithm == 'Minimum curvature')

    def test_wellsurvey_dxdytvd_set_algorithm_wrong_string(self, well_good_dxdytvd_survey):
        with pytest.raises(ValueError) as error:
            well_good_dxdytvd_survey.algorithm = 'abcdefg'
        assert error.type is ValueError
        assert error.value.args[0] == "Algorithm must be set to either 'Minimum curvature' or 'Linearization'"

    def test_wellsurvey_dxdytvd_set(self, well_good_dxdytvd_survey, delete_workflow):
        clone = well_good_dxdytvd_survey.clone('clone', copy_values=False)

        dxs = [10, 20, 30, 40]
        dys = [15, 25, 35, 45]
        tvds = [0, 10, 500, 918]

        try:
            clone.set(dxs=dxs, dys=dys, tvds=tvds)
            assert clone.is_calculation_valid()
            assert clone.algorithm == 'Minimum curvature'
            df = clone.as_dataframe()
            assert df["DX"][0] == dxs[0]
            assert df["DX"][1] == dxs[1]
            assert df["DX"][2] == dxs[2]
            assert df["DX"][3] == dxs[3]
            assert df["DY"][0] == dys[0]
            assert df["DY"][1] == dys[1]
            assert df["DY"][2] == dys[2]
            assert df["DY"][3] == dys[3]
            assert df["TVD"][0] == tvds[0]
            assert df["TVD"][1] == pytest.approx(tvds[1])
            assert df["TVD"][2] == pytest.approx(tvds[2])
            assert df["TVD"][3] == pytest.approx(tvds[3])
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 73
            assert df_calculated['X'][0] == pytest.approx(486748.5)
            assert df_calculated['X'][72] == pytest.approx(486778.5)
            assert df_calculated['Y'][0] == pytest.approx(6226804)
            assert df_calculated['Y'][72] == pytest.approx(6226834)
            assert df_calculated['Z'][0] == 82
            assert df_calculated['Z'][72] == pytest.approx(-836)
            assert df_calculated['MD'][0] == 0
            assert df_calculated['MD'][72] == pytest.approx(1213.70, 0.00001)
            assert df_calculated['Inclination'][0] == pytest.approx(82.94, 0.001)
            assert df_calculated['Inclination'][72] == pytest.approx(74.58, 0.0001)
            assert df_calculated['Azimuth GN'][0] == pytest.approx(45.00, 0.00001)
            assert df_calculated['Azimuth GN'][72] == pytest.approx(45.00, 0.00001)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_dxdytvd_set_make_survey_invalid(self, well_good_dxdytvd_survey, delete_workflow):
        clone = well_good_dxdytvd_survey.clone('clone', copy_values=False)

        dxs = [10, 20, 30, 40]
        dys = [15, 25, 35, 45]
        tvds = [82.0, 10, 500, 66]

        try:
            clone.set(dxs=dxs, dys=dys, tvds=tvds)
            assert not clone.is_calculation_valid()
            assert clone.algorithm == 'Minimum curvature'
            df = clone.as_dataframe()
            assert len(df.index) == clone.record_count
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_dxdytvd_clone_copy(self, well_good_dxdytvd_survey, delete_workflow):
        clone = well_good_dxdytvd_survey.clone(well_good_dxdytvd_survey.petrel_name + 'clone_copy', copy_values=True)
        try: 
            df = clone.as_dataframe()
            assert len(df.index) == 2
            assert df.columns[0] == 'DX'
            assert df.columns[1] == 'DY'
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

    def test_wellsurvey_dxdytvd_clone_no_copy(self, well_good_dxdytvd_survey, delete_workflow):
        clone = well_good_dxdytvd_survey.clone(well_good_dxdytvd_survey.petrel_name + 'clone_no_copy', copy_values=False)
        try:
            df = clone.as_dataframe()
            assert clone.record_count == 0
            assert len(df.index) == 0
            assert df.columns[0] == 'DX'
            assert df.columns[1] == 'DY'
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

    def test_wellsurvey_dxdytvd_template(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.template == ''
        
    def test_wellsurvey_dxdytvd_workflow_enabled(self, well_good_dxdytvd_survey, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: well_good_dxdytvd_survey})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(well_good_dxdytvd_survey))
        assert unpacked_object.petrel_name == well_good_dxdytvd_survey.petrel_name
        assert unpacked_object.path == well_good_dxdytvd_survey.path
        assert unpacked_object.droid == well_good_dxdytvd_survey.droid

    def test_wellsurvey_dxdytvd_is_calculation_valid_True(self, well_good_dxdytvd_survey):
        assert well_good_dxdytvd_survey.is_calculation_valid()

    def test_wellsurvey_dxdytvd_is_calculation_valid_False(self, well_good_dxdytvd_invalid_survey):
        assert not well_good_dxdytvd_invalid_survey.is_calculation_valid()
