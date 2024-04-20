import pytest
import os
import sys
parent_dir = os.path.abspath("..")
sys.path.insert(0, parent_dir)
from cegalprizm.pythontool.polylines import PolylineSet
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPolylinesetTestProject2:
    def test_polylineset_clone_root_copy_false(self, petrellink, delete_workflow):
        try:
            p1 = petrellink.polylinesets['Input/Polygon 0']
            p2 = p1.clone("polygon 0_clone", copy_values = False)
            assert isinstance(p2, PolylineSet)
            assert p2.petrel_name == "polygon 0_clone"
            assert p2.path == "Input/polygon 0_clone"
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: p2})

    def test_polylineset_clone_root_copy_true(self, petrellink, delete_workflow):
        try:
            p1 = petrellink.polylinesets['Input/Polygon 0']
            p2 = p1.clone("polygon 0_clone with values", copy_values = True)
            assert isinstance(p2, PolylineSet)
            assert p2.petrel_name == "polygon 0_clone with values"
            assert p2.path == "Input/polygon 0_clone with values"
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: p2})

    def test_polylineset_root_clone_a_clone_copy_false(self, petrellink, delete_workflow):
        try:
            p1 = petrellink.polylinesets['Input/Polygon 0']
            p2 = p1.clone("polygon 0_clone", copy_values = False)
            p4 = p2.clone("polygon 0_clone_clone", copy_values = False)
            assert isinstance(p4, PolylineSet)
            assert p4.petrel_name == "polygon 0_clone_clone"
            assert p4.path == "Input/polygon 0_clone_clone"
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: p4})
            delete_workflow.run({obj: p2})

    def test_polylineset_root_clone_a_clone_copy_true(self, petrellink, delete_workflow):
        try:
            p1 = petrellink.polylinesets['Input/Polygon 0']
            p2 = p1.clone("polygon 0_clone_values", copy_values = True)
            p4 = p2.clone("polygon 0_clone_values_clone", copy_values = True)
            assert isinstance(p4, PolylineSet)
            assert p4.petrel_name == "polygon 0_clone_values_clone"
            assert p4.path == "Input/polygon 0_clone_values_clone"
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: p4})
            delete_workflow.run({obj: p2})

    def test_polylineset_clone_empty(self, petrellink, delete_workflow):
        try:
            polygon = petrellink.polylinesets["Input/Geometry/Polygon"]
            poly = polygon.clone("New Empt test polygon", False)
            # as petreltest there was a comment that an exception should be raised here, but that is not the case
            poly2 = poly.clone('Some other enmpty polygon', True)
            assert isinstance(poly, PolylineSet)
            assert poly.petrel_name == "New Empt test polygon"
            assert isinstance(poly2, PolylineSet)
            assert poly2.petrel_name == "Some other enmpty polygon"
        finally:
            obj = delete_workflow.input['object']
            delete_workflow.run({obj: poly})
            delete_workflow.run({obj: poly2})


