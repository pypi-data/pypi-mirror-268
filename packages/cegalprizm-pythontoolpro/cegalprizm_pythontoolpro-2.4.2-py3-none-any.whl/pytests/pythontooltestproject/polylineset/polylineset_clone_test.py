import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPolylineSetClone:
    def test_polylineset_clone_no_attributes_no_copy(self, polylineset_no_attributes, delete_workflow):
        try:
            clone = polylineset_no_attributes.clone("Poly2", copy_values=False)
            assert clone.petrel_name == "Poly2"
            assert clone.path == "Input/Geometry/Poly2"
            assert clone.droid != polylineset_no_attributes.droid
            assert polylineset_no_attributes.get_positions(0) == clone.get_positions(0)
            # TODO once we have access to polyline attributes we should confirm clone also has none
            # Currently we have no way to check in the tests if copy-values actually works
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: clone})

    def test_polylineset_clone_no_attributes_copy(self, polylineset_no_attributes, delete_workflow):
        try:
            clone = polylineset_no_attributes.clone("Poly2", copy_values=True)
            assert clone.petrel_name == "Poly2"
            assert clone.path == "Input/Geometry/Poly2"
            assert clone.droid != polylineset_no_attributes.droid
            assert polylineset_no_attributes.get_positions(0) == clone.get_positions(0)
            # TODO once we have access to polyline attributes we should confirm clone also has none
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: clone})

    def test_polylineset_clone_attributes_no_copy(self, polylineset, delete_workflow):
        try:
            clone = polylineset.clone("Polygon_copy_noval", copy_values=False)
            assert clone.petrel_name == "Polygon_copy_noval"
            assert clone.path == "Input/Geometry/Polygon_copy_noval"
            assert clone.droid != polylineset.droid
            assert polylineset.get_positions(0) == clone.get_positions(0)
            ## Lines/points are copied even if copy_values is False
            lines_original = polylineset.polylines
            lines_clone = clone.polylines
            original_list = []
            clone_list = []
            for line in lines_original:
                for point in line.points:
                    original_list.append(point)
            for line in lines_clone:
                for point in line.points:
                    clone_list.append(point)

            assert original_list == clone_list
            
            # TODO once we have access to polyline attributes we should check values are not copied
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: clone})

    def test_polylineset_clone_attributes_copy(self, polylineset, delete_workflow):
        try:
            clone = polylineset.clone("Polygon_copy", copy_values=True)
            assert clone.petrel_name == "Polygon_copy"
            assert clone.path == "Input/Geometry/Polygon_copy"
            assert clone.droid != polylineset.droid
            assert polylineset.get_positions(0) == clone.get_positions(0)

            lines_original = polylineset.polylines
            lines_clone = clone.polylines
            original_list = []
            clone_list = []
            for line in lines_original:
                for point in line.points:
                    original_list.append(point)
            for line in lines_clone:
                for point in line.points:
                    clone_list.append(point)

            assert original_list == clone_list
            # TODO once we have access to polyline attributes we should check values are actually copied
        finally:
            obj = delete_workflow.input["object"]
            delete_workflow.run({obj: clone})

    def test_polylineset_cloning_respects_subfolder(self, petrellink, delete_workflow):
        try:
            from cegalprizm.pythontool.polylines import PolylineSet
            poly = petrellink.polylinesets["Input/Geometry/GeometrySubFolder/Polylines/Polygon 2"]
            assert isinstance(poly, PolylineSet)
        finally:
            obj = delete_workflow.input["object"]