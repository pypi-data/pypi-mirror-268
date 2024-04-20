from math import isnan
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLogsDataframeZeroSamples:
    def test_logs_dataframe_one_log_zero_samples(self, well_log, petrellink, delete_workflow):
        try:
            zero_sample_well_log = well_log.clone('zero_sample_well_log')
            zero_sample_global_well_log = petrellink.global_well_logs['Input/Wells/Global well logs/zero_sample_well_log']

            zero_sample_mds = []
            zero_sample_values = []
            zero_sample_well_log.set_values(mds=zero_sample_mds, values=zero_sample_values)

            well = zero_sample_well_log.well       
            df = well.logs_dataframe([zero_sample_global_well_log])

            assert len(df.columns) == 5
            assert len(df.index) == 0
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: zero_sample_well_log})
            delete_workflow.run({input_obj: zero_sample_global_well_log})

    def test_logs_dataframe_multiple_logs_one_log_zero_samples(self, well_log, well_log_vs, petrellink, delete_workflow):
        try:
            zero_sample_well_log = well_log.clone('zero_sample_well_log')
            zero_sample_global_well_log = petrellink.global_well_logs['Input/Wells/Global well logs/zero_sample_well_log']
            zero_sample_mds = []
            zero_sample_values = []
            zero_sample_well_log.set_values(mds=zero_sample_mds, values=zero_sample_values)

            multiple_samples_well_log = well_log_vs.clone('multiple_samples_well_log')
            multiple_samples_global_well_log = petrellink.global_well_logs['Input/Wells/Global well logs/multiple_samples_well_log']
            multiple_sample_mds = [1111, 1112, 1113, 1114, 1115]
            multiple_sample_values = [10, 20, 30, 40, 50]
            multiple_samples_well_log.set_values(mds=multiple_sample_mds, values=multiple_sample_values)

            assert zero_sample_well_log.well.droid == multiple_samples_well_log.well.droid

            well = zero_sample_well_log.well
            df = well.logs_dataframe([zero_sample_global_well_log, multiple_samples_global_well_log])

            assert len(df.columns) == 6
            assert isnan(df['zero_sample_well_log'][0])
            assert isnan(df['zero_sample_well_log'][1])
            assert isnan(df['zero_sample_well_log'][2])
            assert isnan(df['zero_sample_well_log'][3])
            assert isnan(df['zero_sample_well_log'][4])
            assert isnan(df['zero_sample_well_log'][5])
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: zero_sample_well_log})
            delete_workflow.run({input_obj: multiple_samples_well_log})
            delete_workflow.run({input_obj: zero_sample_global_well_log})
            delete_workflow.run({input_obj: multiple_samples_global_well_log})
