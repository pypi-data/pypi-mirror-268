from math import isnan
import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLogsDataframeSingleLogSingleSample:

    def test_logs_dataframe_single_log_single_sample(self, well_log, petrellink, delete_workflow):
        try:
            single_sample_mds = [1112]
            single_sample_values = [2]

            well_log_clone = well_log.clone('well_log_clone')
            well_log_clone.set_values(mds=single_sample_mds, values=single_sample_values)            

            df = well_log_clone.well.logs_dataframe([well_log_clone.global_well_log])
            global_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_clone']

            assert len(df.columns) == 5
            assert len(df.index) == 1
            assert df['well_log_clone'][0] == pytest.approx(2)
            assert df['MD'][0] == pytest.approx(1112)
            assert df['TWT'][0] == pytest.approx(332.7550)
            assert df['TVDSS'][0] == pytest.approx(1029.97)
            assert df['TVD'][0] == pytest.approx(1111.97)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: well_log_clone})
            delete_workflow.run({input_obj: global_clone})

    def test_logs_dataframe_multiple_logs_one_log_has_single_sample_within(self, well_log, well_log_vs, petrellink, delete_workflow):
        try:
            single_sample_mds = [1112]
            single_sample_values = [2]
            multiple_sample_mds = [1111, 1112, 1113, 1114, 1115]
            multiple_sample_values = [10, 20, 30, 40, 50]

            well_log_clone = well_log.clone('well_log_clone')
            well_log_clone.set_values(mds=single_sample_mds, values=single_sample_values)

            well_log_vs_clone = well_log_vs.clone('well_log_vs_clone')
            well_log_vs_clone.set_values(mds=multiple_sample_mds, values=multiple_sample_values)

            global_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_clone']
            global_vs_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_vs_clone']

            assert well_log_clone.well.droid == well_log_vs_clone.well.droid

            well = well_log_clone.well
            df = well.logs_dataframe([well_log_clone.global_well_log, well_log_vs_clone.global_well_log])

            assert len(df.columns) == 6
            assert len(df.index) == 9

            assert isnan(df['well_log_clone'][0])
            assert df['well_log_vs_clone'][0] == 10
            assert df['MD'][0] == pytest.approx(1111)

            assert isnan(df['well_log_clone'][1])
            assert df['well_log_vs_clone'][1] == 15
            assert df['MD'][1] == pytest.approx(1111.5)

            assert df['well_log_clone'][2] == 2
            assert df['well_log_vs_clone'][2] == 20
            assert df['MD'][2] == pytest.approx(1112)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: well_log_clone})
            delete_workflow.run({input_obj: well_log_vs_clone})
            delete_workflow.run({input_obj: global_clone})
            delete_workflow.run({input_obj: global_vs_clone})

    def test_logs_dataframe_multiple_logs_one_log_has_single_sample_above(self, well_log, well_log_vs, petrellink, delete_workflow):
        try:
            single_sample_mds = [1110]
            single_sample_values = [2]
            multiple_sample_mds = [1111, 1112, 1113, 1114, 1115]
            multiple_sample_values = [10, 20, 30, 40, 50]

            well_log_clone = well_log.clone('well_log_clone')
            well_log_clone.set_values(mds=single_sample_mds, values=single_sample_values)

            well_log_vs_clone = well_log_vs.clone('well_log_vs_clone')
            well_log_vs_clone.set_values(mds=multiple_sample_mds, values=multiple_sample_values)

            global_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_clone']
            global_vs_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_vs_clone']

            assert well_log_clone.well.droid == well_log_vs_clone.well.droid

            well = well_log_clone.well
            df = well.logs_dataframe([well_log_clone.global_well_log, well_log_vs_clone.global_well_log])

            assert len(df.columns) == 6
            assert len(df.index) == 11

            # top 3 rows
            assert df['well_log_clone'][0] == 2
            assert isnan(df['well_log_vs_clone'][0])
            assert df['MD'][0] == pytest.approx(1110)

            assert isnan(df['well_log_clone'][1])
            assert isnan(df['well_log_vs_clone'][1])
            assert df['MD'][1] == pytest.approx(1110.5)

            assert isnan(df['well_log_clone'][2])
            assert df['well_log_vs_clone'][2] == 10
            assert df['MD'][2] == pytest.approx(1111)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: well_log_clone})
            delete_workflow.run({input_obj: well_log_vs_clone})
            delete_workflow.run({input_obj: global_clone})
            delete_workflow.run({input_obj: global_vs_clone})

    def test_logs_dataframe_multiple_logs_one_log_has_single_sample_below(self, well_log, well_log_vs, petrellink, delete_workflow):
        try:
            single_sample_mds = [1116]
            single_sample_values = [2]
            multiple_sample_mds = [1111, 1112, 1113, 1114, 1115]
            multiple_sample_values = [10, 20, 30, 40, 50]

            well_log_clone = well_log.clone('well_log_clone')
            well_log_clone.set_values(mds=single_sample_mds, values=single_sample_values)

            well_log_vs_clone = well_log_vs.clone('well_log_vs_clone')
            well_log_vs_clone.set_values(mds=multiple_sample_mds, values=multiple_sample_values)

            global_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_clone']
            global_vs_clone = petrellink.global_well_logs['Input/Wells/Global well logs/well_log_vs_clone']

            assert well_log_clone.well.droid == well_log_vs_clone.well.droid

            well = well_log_clone.well
            df = well.logs_dataframe([well_log_clone.global_well_log, well_log_vs_clone.global_well_log])

            assert len(df.columns) == 6
            assert len(df.index) == 11

            # bottom 3 rows
            assert isnan(df['well_log_clone'][8])
            assert df['well_log_vs_clone'][8] == 50
            assert df['MD'][8] == pytest.approx(1115)

            assert isnan(df['well_log_clone'][9])
            assert isnan(df['well_log_vs_clone'][9])
            assert df['MD'][9] == pytest.approx(1115.5)

            assert df['well_log_clone'][10] == 2
            assert isnan(df['well_log_vs_clone'][10])
            assert df['MD'][10] == pytest.approx(1116)
        finally:
            input_obj = delete_workflow.input['object']
            delete_workflow.run({input_obj: well_log_clone})
            delete_workflow.run({input_obj: well_log_vs_clone})
            delete_workflow.run({input_obj: global_clone})
            delete_workflow.run({input_obj: global_vs_clone})

