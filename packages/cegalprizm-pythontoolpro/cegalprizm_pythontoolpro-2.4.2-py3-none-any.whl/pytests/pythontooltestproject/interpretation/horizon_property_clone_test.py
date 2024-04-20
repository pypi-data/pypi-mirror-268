import pytest
import sys
import os
import math
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestHorizonPropertyClone:
    def test_horizon_property_clone_copy_values_False(self, horizon_property, delete_workflow):
        try:
            num_prop_before_clone = len(horizon_property.horizon_interpretation_3d.horizon_property_3ds)
            clone = horizon_property.clone(name_of_clone='clone', copy_values=False)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Interpretation folder 1/BCU/Ardmore/clone'
            assert len(clone.horizon_interpretation_3d.horizon_property_3ds) == num_prop_before_clone + 1
            copied_values = clone.all().as_array()
            for i in range(5):
                for j in range(5):
                    assert math.isnan(copied_values[i, j])
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_horizon_property_clone_copy_values_True(self, horizon_property, delete_workflow):
        try:
            num_prop_before_clone = len(horizon_property.horizon_interpretation_3d.horizon_property_3ds)
            clone = horizon_property.clone(name_of_clone='clone', copy_values=True)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Interpretation folder 1/BCU/Ardmore/clone'
            assert len(clone.horizon_interpretation_3d.horizon_property_3ds) == num_prop_before_clone + 1
            orig_values = horizon_property.all().as_array()
            copied_values = clone.all().as_array()
            for i in range(5):
                for j in range(5):
                    if math.isnan(orig_values[i, j]):
                        assert math.isnan(copied_values[i, j])
                        continue
                    assert orig_values[i, j] == copied_values[i, j]
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})

    def test_horizon_property_clone_copy_values_False_template(self, horizon_property_autotracker_confidence, delete_workflow, petrellink):
        new_template = petrellink.templates['Templates/Geophysical templates/S-impedance']
        try:
            num_prop_before_clone = len(horizon_property_autotracker_confidence.horizon_interpretation_3d.horizon_property_3ds)
            clone = horizon_property_autotracker_confidence.clone(name_of_clone='clone', copy_values=False, template=new_template)
            assert clone.petrel_name == 'clone'
            assert clone.path == 'Input/Seismic/Interpretation folder 1/BCU/Ardmore/clone'
            assert len(clone.horizon_interpretation_3d.horizon_property_3ds) == num_prop_before_clone + 1
            clone_template = clone.get_template()
            assert clone_template.path == new_template.path
            assert clone_template.droid == new_template.droid
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: clone})