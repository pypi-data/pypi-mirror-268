import pytest
import sys
import os
import pandas as pd
from cegalprizm.pythontool.welllog import WellLog
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestWellLogClone:
    def test_well_log_clone_copy_values_False(self, well_log_vs, delete_workflow):
        try:
            clone = well_log_vs.clone(name_of_clone='clone', copy_values=False)
            clone_global_well_log = clone.global_well_log
            assert isinstance(clone, WellLog)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Well_Good/Well logs/clone'
            assert clone.template == well_log_vs.template
            assert len(clone.samples) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_well_log_clone_copy_values_True(self, well_log_vs, delete_workflow):
        try:
            clone = well_log_vs.clone(name_of_clone='clone', copy_values=True)
            clone_global_well_log = clone.global_well_log
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Well_Good/Well logs/clone'
            assert clone.template == well_log_vs.template
            log_vs_samples = well_log_vs.samples
            log_vs_copy_samples = clone.samples
            for i in range(9300, 10000, 100):
                s = log_vs_samples.at(i)
                s_copy = log_vs_copy_samples.at(i)
                assert s.position == s_copy.position
                assert s.md == s_copy.md
                assert s.twt == s_copy.twt
                assert s.tvd == s_copy.tvd
                assert s.value == s_copy.value
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_well_log_clone_copy_values_False_template(self, well_log_vs, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Geophysical templates/S-impedance']
        try:
            clone = well_log_vs.clone(name_of_clone='clone', template=new_template)
            clone_global_well_log = clone.global_well_log
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_well_log_clone_respects_subfolders(self, petrellink, delete_workflow):
        try:
            log = petrellink.well_logs['Input/Wells/Well_Good/Well logs/Logs/ScaleUp/DEPTH 1']
            clone = log.clone("DEPTH 2")
            assert isinstance(clone, WellLog)
            assert clone.path == 'Input/Wells/Well_Good/Well logs/Logs/ScaleUp/DEPTH 2'
            assert clone.petrel_name == 'DEPTH 2'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_well_log_clone_novals(self, petrellink, delete_workflow):
        try:
            dt = petrellink.well_logs['Input/Wells/Well_Good/Well logs/DT']
            dt1 = dt.clone('DT_copy_noval', copy_values=False)
            facies = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies']
            facies_copy = facies.clone('Facies_copy_noval', False)

            pd.testing.assert_frame_equal(dt1.as_dataframe(), pd.DataFrame(columns=['X', 'Y', 'Z', 'MD', 'TWT', 'TVDSS', 'TVD', 'Value']))
            pd.testing.assert_frame_equal(facies_copy.as_dataframe(), pd.DataFrame(columns=['X', 'Y', 'Z', 'MD', 'TWT', 'TVDSS', 'TVD', 'Value', 'ValueText']))
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: dt1})
            delete_workflow.run({obj: facies_copy})

    def test_well_log_clone_vals(self, petrellink, delete_workflow):
        try:
            dt = petrellink.well_logs['Input/Wells/Well_Good/Well logs/DT']
            dt2 = dt.clone('DT_copy', copy_values=True)
            facies = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies']
            facies_copy = facies.clone('Facies_copy', True)

            pd.testing.assert_frame_equal(dt2.as_dataframe(), dt.as_dataframe())
            pd.testing.assert_frame_equal(facies_copy.as_dataframe(), facies.as_dataframe())
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: dt2})
            delete_workflow.run({obj: facies_copy})

    def test_well_log_clone_set_empty_values(self, petrellink, delete_workflow):
        try:
            dt = petrellink.well_logs['Input/Wells/Well_Good/Well logs/DT']
            dt1 = dt.clone('DT_copy_noval', copy_values=False)
            mds = []
            values = []
            dt1.readonly = False
            dt1.set_values(mds, values)

            facies = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies']
            facies_copy = facies.clone('Facies_copy_noval', False)
            facies_copy.readonly = False
            facies_copy.set_values(mds, values)

            pd.testing.assert_frame_equal(dt1.as_dataframe(), pd.DataFrame(columns=['X', 'Y', 'Z', 'MD', 'TWT', 'TVDSS', 'TVD', 'Value']))
            pd.testing.assert_frame_equal(facies_copy.as_dataframe(), pd.DataFrame(columns=['X', 'Y', 'Z', 'MD', 'TWT', 'TVDSS', 'TVD', 'Value', 'ValueText']))
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: dt1})
            delete_workflow.run({obj: facies_copy})