import pytest
import sys
import os
from cegalprizm.pythontool.welllog import GlobalWellLog
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestGlobalWellLogClone:
    def test_global_well_log_clone(self, global_well_log, delete_workflow):
        try:
            clone = global_well_log.clone(name_of_clone='clone')
            assert isinstance(clone, GlobalWellLog)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Wells/Global well logs/clone'
            assert clone.template == global_well_log.template
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_global_well_log_clone_template(self, global_well_log, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Geophysical templates/S-impedance']
        try:
            clone = global_well_log.clone(name_of_clone='clone', template=new_template)
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_global_well_log_clone_warns_on_copy_values(self, global_well_log, delete_workflow):
        try:
            with pytest.warns(DeprecationWarning) as warning:
                clone = global_well_log.clone(name_of_clone='clone', copy_values=True)
            assert warning.pop(DeprecationWarning).message.args[0] == "The copy_values argument is not implemented for GlobalWellLog objects and will be removed in Python Tool Pro version 3.0."
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_global_well_log_clone_respects_subfolders(self, petrellink, delete_workflow):
        try:
            log = petrellink.global_well_logs['Input/Wells/Global well logs/Logs/ScaleUp/RHOB_ScaleUp_4ms 2']
            clone = log.clone(name_of_clone='RHOB_ScaleUp_4ms 3')
            assert isinstance(clone, GlobalWellLog)
            assert clone.path == 'Input/Wells/Global well logs/Logs/ScaleUp/RHOB_ScaleUp_4ms 3'
            assert clone.petrel_name == 'RHOB_ScaleUp_4ms 3'
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})