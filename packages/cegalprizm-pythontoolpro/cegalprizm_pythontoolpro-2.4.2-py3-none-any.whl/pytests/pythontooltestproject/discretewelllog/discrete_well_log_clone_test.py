import pytest
import sys
import os
from cegalprizm.pythontool.welllog import DiscreteWellLog
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteWellLogClone:
    def test_discrete_well_log_clone_copy_values_False(self, discrete_well_log, delete_workflow):
        try:
            clone = discrete_well_log.clone(name_of_clone='clone', copy_values=False)
            clone_global_well_log = clone.global_well_log
            assert isinstance(clone, DiscreteWellLog)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Well_Good/Well logs/clone'
            assert len(clone.samples) == 0
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_discrete_well_log_clone_copy_values_True(self, discrete_well_log, delete_workflow):
        try:
            clone = discrete_well_log.clone(name_of_clone='clone', copy_values=True)
            clone_global_well_log = clone.global_well_log
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Well_Good/Well logs/clone'
            log_facies_samples = discrete_well_log.samples
            log_facies_copy_samples = clone.samples
            for i in range(9300, 10000, 100):
                s = log_facies_samples.at(i)
                s_copy = log_facies_copy_samples.at(i)
                assert s.position == s_copy.position
                assert s.md == s_copy.md
                assert s.twt == s_copy.twt
                assert s.tvd == s_copy.tvd
                assert s.value == s_copy.value
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_discrete_well_log_clone_copy_values_False_template(self, discrete_well_log, delete_workflow, petrellink):
        new_template = petrellink.discrete_templates['Templates/Discrete property templates/Fluvial facies']
        try:
            clone = discrete_well_log.clone(name_of_clone='clone', discrete_template=new_template)
            clone_global_well_log = clone.global_well_log
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})
            delete_workflow.run({obj: clone_global_well_log})

    def test_discrete_well_log_clone_respects_subfolders(self, petrellink, delete_workflow):
        from cegalprizm.pythontool.welllog import DiscreteWellLog
        try:
            log = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Logs/ScaleUp/Facies 4']
            clone = log.clone("Facies 5")
            assert isinstance(clone, DiscreteWellLog)
            assert clone.path == 'Input/Wells/Well_Good/Well logs/Logs/ScaleUp/Facies 5'
            assert clone.petrel_name == 'Facies 5'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})