import pytest
import sys
import os
from cegalprizm.pythontool.primitives import Point
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestPointSet:
    def test_pointset_add_point_with_attributes(self, pointset_many):
        pointset_many.readonly = False
        pointset_many.add_point(Point(50.0,50.0,915.0))
        assert pointset_many[10].x == 50.0
        assert pointset_many[10].y == 50.0
        assert pointset_many[10].z == 915.0
        pointset_many.delete_point(Point(50.0,50.0,915.0))
        pointset_many.readonly = True

    def test_pointset_add_point_no_attributes(self, pointset_noattributes):
        pointset_noattributes.readonly = False
        pointset_noattributes.add_point(Point(50.0,50.0,915.0))
        assert pointset_noattributes[3].x == 50.0
        assert pointset_noattributes[3].y == 50.0
        assert pointset_noattributes[3].z == 915.0
        pointset_noattributes.delete_point(Point(50.0,50.0,915.0))
        pointset_noattributes.readonly = True

    def test_pointset_complete(self, pointset_empty):
        pointset_empty.readonly = False
        assert pointset_empty.petrel_name == "Points empty"
        old_points = list(pointset_empty.points)
        pointset_empty.add_point(Point(1.0, 2.0, 914.40))
        assert len(pointset_empty.points) == 1
        assert pointset_empty.points[0].x == 1.0
        pointset_empty.add_point(Point(6, 7, 8))
        assert len(pointset_empty.points) == 2
        assert pointset_empty.points[1].x == 6.0
        pointset_empty.points = [Point(1,2,3), Point(4,5,6), Point(7,8,9)]
        assert len(pointset_empty.points) == 3
        assert pointset_empty.points[2].x == 7.0
        pointset_empty.delete_point(Point(4,5,6))
        assert len(pointset_empty.points) == 2
        assert pointset_empty.points[1].x == 7.0

        pointset_empty.points = old_points
        pointset_empty.readonly = True

    def test_pointset_petrelname(self, pointset_many):
        assert pointset_many.petrel_name == "Points 1 many points"

    def test_pointset_path(self, pointset_many):
        assert pointset_many.path == "Input/Geometry/Points 1 many points"

    def test_pointset_readonly(self, pointset_many):
        assert pointset_many.readonly == True
        pointset_many.readonly = False
        assert pointset_many.readonly == False
        pointset_many.add_point(Point(50,50,50))
        pointset_many.delete_point(Point(50,50,50))
        pointset_many.readonly = True

    def test_pointset_retrieve_history(self, pointset_many):
        # Why make it easy when you can make it hard?
        res = ""
        for lst in pointset_many.retrieve_history().iloc[:1,1:].values:
            for el in lst:
                res += el
        assert res.replace(" ", "") == "shubgoBluebacktoolboxExtractpointsExtractedpointsfromcube:Vptime"

    def test_pointset_retrieve_stats(self, pointset_many):
        stats = pointset_many.retrieve_stats()
        assert stats['Max'] == "-135.00"
        assert stats['Mean'] == "-2584.04"
        assert stats['Min'] == "-13531.00"
        assert stats['Number of attributes'] == "13"
        assert stats['Number of defined values'] == "10"
        assert stats['Number of points'] == "10"
        assert stats['Std. dev.'] == "3917.63"
        assert stats['Sum'] == "-25840.40"
        assert stats['Type of data'] == "Continuous"
        assert stats['Variance'] == "15347834.24"
        assert str(type(stats)) == "<class 'dict'>"

    def test_pointset_template(self, pointset_empty):
        assert pointset_empty.template == ''

    def test_pointset_attributes_info(self, seismic_pointset):
        assert seismic_pointset.petrel_name == "Seismic_pointset"

        info = seismic_pointset._attributes_info()
        keys = list(info.keys())
        keys.sort()

        units = ["'Seismic3D' -  ", "TWT auto - ms", "x - None", "y - None", "z - None"]
        templates = ["'Seismic3D' - Seismic (default)", "TWT auto - Elevation time", "x - None", "y - None", "z - None"]

        for key in keys:
            assert str(key) + ' - ' +  str(info[key]['Unit']) == units.pop(0)
            assert str(key) + ' - ' +  str(info[key]['Template']) == templates.pop(0)

    def test_pointset_exceptions(self, pointset):
        with pytest.raises(Exception):
            pointset.add_point(Point(6, 7, 8))

        with pytest.raises(Exception):
            pointset.points = [Point(1,2,3), Point(4,5,6), Point(7,8,9)]

        with pytest.raises(Exception):
            pointset.delete_point(pointset.points[0])

    def test_pointset_workflow_enabled(self, pointset, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: pointset})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(pointset))
        assert unpacked_object.petrel_name == pointset.petrel_name
        assert unpacked_object.path == pointset.path
        assert unpacked_object.droid == pointset.droid