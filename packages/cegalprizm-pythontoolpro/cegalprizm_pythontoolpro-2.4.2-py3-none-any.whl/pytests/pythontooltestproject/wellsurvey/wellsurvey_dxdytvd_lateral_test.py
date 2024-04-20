import pytest
import os
import sys
from cegalprizm.pythontool import Well
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Dxdytvd_Lateral:
    def test_wellsurvey_dxdytvd_lateral_petrel_name(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.petrel_name == 'DXDYTVD lateral'

    def test_wellsurvey_dxdytvd_lateral_path(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.path == 'Input/Wells/Well_Good lateral/DXDYTVD lateral'

    def test_wellsurvey_dxdytvd_lateral_droid(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.droid == '57c7fd0b-b9c3-451a-b680-a90b13e6aa5d'

    def test_wellsurvey_dxdytvd_lateral_well(self, well_good_lateral_dxdytvd_survey_lateral):
        well = well_good_lateral_dxdytvd_survey_lateral.well
        assert isinstance(well, Well)
        assert well.petrel_name == 'Well_Good lateral'

    def test_wellsurvey_dxdytvd_lateral_well_survey_type(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.well_survey_type == 'DX DY TVD survey'

    def test_wellsurvey_dxdytvd_lateral_azimuth_reference(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.azimuth_reference == 'Grid north'

    def test_wellsurvey_dxdytvd_lateral_record_count(self, well_good_lateral_dxdytvd_survey_lateral):
        assert well_good_lateral_dxdytvd_survey_lateral.record_count == 1

    def test_wellsurvey_dxdytvd_lateral_getset_algorithm(self, well_good_lateral_dxdytvd_survey_lateral):
        algorithm = well_good_lateral_dxdytvd_survey_lateral.algorithm
        assert(algorithm == 'Minimum curvature')
        well_good_lateral_dxdytvd_survey_lateral.algorithm = 'Linearization'
        algorithm = well_good_lateral_dxdytvd_survey_lateral.algorithm
        assert(algorithm == 'Linearization')
        well_good_lateral_dxdytvd_survey_lateral.algorithm = 'Minimum curvature'
        algorithm = well_good_lateral_dxdytvd_survey_lateral.algorithm
        assert(algorithm == 'Minimum curvature')

    def test_wellsurvey_dxdytvd_lateral_set_algorithm_wrong_string(self, well_good_lateral_dxdytvd_survey_lateral):
        with pytest.raises(ValueError) as error:
            well_good_lateral_dxdytvd_survey_lateral.algorithm = 'abcdefg'
        assert error.type is ValueError
        assert error.value.args[0] == "Algorithm must be set to either 'Minimum curvature' or 'Linearization'"

    def test_wellsurvey_dxdytvd_lateral_set(self, well_good_lateral_dxdytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_dxdytvd_survey_lateral.clone('clone', copy_values=False)

        dxs = [10, 20, 30, 40]
        dys = [15, 25, 35, 45]
        tvds = [15, 20, 500, 918]

        try:
            clone.set(dxs=dxs, dys=dys, tvds=tvds)
            clone.tie_in_md = 10
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
            assert df["TVD"][0] == pytest.approx(tvds[0])
            assert df["TVD"][1] == pytest.approx(tvds[1])
            assert df["TVD"][2] == pytest.approx(tvds[2])
            assert df["TVD"][3] == pytest.approx(tvds[3])
            df_calculated = clone.as_dataframe(get_calculated_trajectory=True)
            assert len(df_calculated.index) == 54
            assert df_calculated['X'][0] == pytest.approx(486738.5)
            assert df_calculated['X'][53] == pytest.approx(486778.5)
            assert df_calculated['Y'][0] == 6226789
            assert df_calculated['Y'][53] == pytest.approx(6226834)
            assert df_calculated['Z'][0] == 72
            assert df_calculated['Z'][53] == pytest.approx(-836)
            assert df_calculated['MD'][0] == pytest.approx(10)
            assert df_calculated['MD'][53] == pytest.approx(1075.22, 0.00001)
            assert df_calculated['Inclination'][0] == 0
            assert df_calculated['Inclination'][53] == pytest.approx(2.23, 0.001)
            assert df_calculated['Azimuth GN'][0] == 0
            assert df_calculated['Azimuth GN'][53] == pytest.approx(167.33, 0.00001)
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_wellsurvey_dxdytvd_lateral_set_make_survey_invalid(self, well_good_lateral_dxdytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_dxdytvd_survey_lateral.clone('clone', copy_values=False)

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

    def test_wellsurvey_dxdytvd_lateral_clone_copy(self, well_good_lateral_dxdytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_dxdytvd_survey_lateral.clone(well_good_lateral_dxdytvd_survey_lateral.petrel_name + 'clone_copy', copy_values=True)
        try: 
            df = clone.as_dataframe()
            assert len(df.index) == 1
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

    def test_wellsurvey_dxdytvd_lateral_clone_no_copy(self, well_good_lateral_dxdytvd_survey_lateral, delete_workflow):
        clone = well_good_lateral_dxdytvd_survey_lateral.clone(well_good_lateral_dxdytvd_survey_lateral.petrel_name + 'clone_no_copy', copy_values=False)
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