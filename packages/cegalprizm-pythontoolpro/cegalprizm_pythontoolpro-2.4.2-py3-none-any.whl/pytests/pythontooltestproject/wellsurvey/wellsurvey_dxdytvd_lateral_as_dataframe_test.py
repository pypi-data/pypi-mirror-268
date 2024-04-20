import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestWellSurvey_Dxdytvd_Lateral_AsDataframe:
    def test_wellsurvey_dxdytvd_lateral_as_dataframe_columns(self, well_good_lateral_dxdytvd_survey_lateral):
        df = well_good_lateral_dxdytvd_survey_lateral.as_dataframe(get_calculated_trajectory=False)
        assert df.columns[0] == 'DX'
        assert df.columns[1] == 'DY'
        assert df.columns[2] == 'TVD'
        assert len(df.index) == well_good_lateral_dxdytvd_survey_lateral.record_count

    def test_wellsurvey_dxdytvd_lateral_as_dataframe_columns_calculated(self, well_good_lateral_dxdytvd_survey_lateral):
        df = well_good_lateral_dxdytvd_survey_lateral.as_dataframe(get_calculated_trajectory=True)
        assert df.columns[0] == 'X'
        assert df.columns[1] == 'Y'
        assert df.columns[2] == 'Z'
        assert df.columns[3] == 'MD'
        assert df.columns[4] == 'Inclination'
        assert df.columns[5] == 'Azimuth GN'