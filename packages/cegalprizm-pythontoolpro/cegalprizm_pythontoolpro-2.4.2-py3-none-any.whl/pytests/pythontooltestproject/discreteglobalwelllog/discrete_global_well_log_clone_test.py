import pytest
import sys
import os
from cegalprizm.pythontool.welllog import DiscreteGlobalWellLog
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestDiscreteGlobalWellLogClone:
    def test_discrete_global_well_log_clone(self, discrete_global_well_log_facies, delete_workflow):
        try:
            clone = discrete_global_well_log_facies.clone(name_of_clone='clone')
            assert isinstance(clone, DiscreteGlobalWellLog)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Global well logs/clone'
            assert clone.template == discrete_global_well_log_facies.template
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_global_well_log_clone_template(self, discrete_global_well_log_facies, delete_workflow, petrellink):
        new_template = petrellink.discrete_templates['Templates/Discrete property templates/Fluvial facies']
        try:
            clone = discrete_global_well_log_facies.clone(name_of_clone='clone', discrete_template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_global_well_log_clone_warns_on_copy_values(self, discrete_global_well_log_facies, delete_workflow):
        try:
            with pytest.warns(DeprecationWarning) as warning:
                clone = discrete_global_well_log_facies.clone(name_of_clone='clone', copy_values=True)
            assert warning.pop(DeprecationWarning).message.args[0] == "The copy_values argument is not implemented for DiscreteGlobalWellLog objects and will be removed in Python Tool Pro version 3.0."
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_discrete_global_well_log_clone_respects_subfolders(self, petrellink, delete_workflow):
        try:
            disc_log = petrellink.discrete_global_well_logs['Input/Wells/Global well logs/Logs/ScaleUp/Facies 2']
            clone = disc_log.clone(name_of_clone='Facies 3')
            assert isinstance(clone, DiscreteGlobalWellLog)
            assert clone.path == 'Input/Wells/Global well logs/Logs/ScaleUp/Facies 3'
            assert clone.petrel_name == 'Facies 3'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})