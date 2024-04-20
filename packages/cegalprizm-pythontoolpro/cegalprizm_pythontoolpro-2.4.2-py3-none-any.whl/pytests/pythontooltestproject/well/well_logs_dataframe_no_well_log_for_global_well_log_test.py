from math import isnan
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLogsDataframeNoWellLogForGlobalWellLog:
    def test_logs_dataframe_no_welllog_for_globalwelllog_alone(self, well_log, global_well_log, delete_workflow):
        try:       
            global_clone_no_local_log = global_well_log.clone('global_clone_no_local_log')

            df = well_log.well.logs_dataframe([global_clone_no_local_log])
            ## Returns empty df due to global log not in well.logs list
            assert df.empty
            assert len(df.columns) == 0
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: global_clone_no_local_log})

    def test_logs_dataframe_no_welllog_for_globalwelllog_with_others(self, well_log, petrellink, delete_workflow):
        try:
            multiple_sample_mds = [1111, 1112, 1113, 1114, 1115]
            multiple_sample_values = [10, 20, 30, 40, 50]

            multiple_sample_log = well_log.clone('multiple_sample_log')
            multiple_sample_log_global = petrellink.global_well_logs['Input/Wells/Global well logs/multiple_sample_log']
            multiple_sample_log.set_values(mds=multiple_sample_mds, values=multiple_sample_values)            

            global_clone_no_local_log = multiple_sample_log_global.clone('global_clone_no_local_log')

            well = multiple_sample_log.well
            df = well.logs_dataframe([multiple_sample_log.global_well_log, global_clone_no_local_log])

            assert len(df.columns) == 5
            assert len(df.index) == 5
            assert df['multiple_sample_log'][1] == pytest.approx(20)
            assert df['MD'][1] == pytest.approx(1112)
            assert df['TWT'][1] == pytest.approx(332.7550)
            assert df['TVDSS'][1] == pytest.approx(1029.97)
            assert df['TVD'][1] == pytest.approx(1111.97)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: multiple_sample_log})
            delete_workflow.run({input_obj: multiple_sample_log_global})
            delete_workflow.run({input_obj: global_clone_no_local_log})