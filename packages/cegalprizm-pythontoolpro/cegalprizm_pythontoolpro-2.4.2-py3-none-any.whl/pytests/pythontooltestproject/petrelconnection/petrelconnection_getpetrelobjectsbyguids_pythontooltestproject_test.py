import pytest
import os
import sys
from cegalprizm.pythontool.exceptions import PythonToolException
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestPetrelConnection_GetPetrelObjectsByGuids_PythonToolTestProject:

    def test_petrelconnection_getpetrelobjectsbyguids_surfacecollection(self, petrellink):
        from cegalprizm.pythontool.surface import Surfaces
        surface_col = petrellink.get_petrelobjects_by_guids(['3f533110-b6d6-4612-9f43-89043590ea3e'])[0]
        assert isinstance(surface_col, Surfaces)

    def test_petrelconnection_getpetrelobjectsbyguids_bool_error(self, petrellink):
        with pytest.raises(PythonToolException) as excinfo:
            petrellink.get_petrelobjects_by_guids([True])
        assert excinfo.value.args[0] == "Input argument 'GUIDs' must be a list and all items must be string"

    def test_petrelconnection_getpetrelobjectsbyguids_int_error(self, petrellink):
        with pytest.raises(PythonToolException) as excinfo:
            petrellink.get_petrelobjects_by_guids([2022])
        assert excinfo.value.args[0] == "Input argument 'GUIDs' must be a list and all items must be string"

    def test_petrelconnection_getpetrelobjectsbyguids_nolist_error(self, petrellink):
        well_droid = petrellink.wells['Input/Wells/Well_Good'].droid
        with pytest.raises(PythonToolException) as excinfo:
            petrellink.get_petrelobjects_by_guids(well_droid)
        assert excinfo.value.args[0] == "Input argument 'GUIDs' must be a list and all items must be string"

    def test_petrelconnection_getpetrelobjectsbyguids_get_delete_get_None(self, petrellink, delete_workflow):
        pointset = petrellink.pointsets['Input/Geometry/Points empty']
        clone = pointset.clone('clone')
        guid_for_object = clone.droid
        petrel_object = petrellink.get_petrelobjects_by_guids([guid_for_object])[0]
        from cegalprizm.pythontool.points import PointSet
        assert isinstance(petrel_object, PointSet)
        input_object = delete_workflow.input['object']
        delete_workflow.run({input_object: petrel_object})
        petrel_object = petrellink.get_petrelobjects_by_guids([guid_for_object])[0]
        assert petrel_object is None

    def test_petrelconnection_getpetrelobjectsbyguids_wrong_guid_returns_None(self, petrellink):
        wrong_guid_format = 'CCE6E19B611E418C822A1E4FFDC3DEAF'
        objs = petrellink.get_petrelobjects_by_guids([wrong_guid_format])
        assert objs[0] == None

    def test_petrelconnection_getpetrelobjectsbyguids_check_path(self, petrellink):
        tuple_data = []
        tuple_data.append( ('e8b3c9b8-6fc6-429c-99e6-49733a6981ea', 'Input/Wells/Well_Good')) # well
        tuple_data.append( ('ebdde903-a742-4bed-ae21-5add0b471cde', 'Input/Wells/Well_Good/Completions/Casing 1')) # casing string
        tuple_data.append( ('fc808a4f-db92-4f78-9b2b-7458e0f561f3', 'Input/Wells/Well_Good/Completions/Perforation 1')) # perforation
        tuple_data.append( ('6e194af4-9f94-434b-975e-baeeddc1e961', 'Input/Wells/Well_Good/Completions/Squeeze 1')) # squeeze
        tuple_data.append( ('82381d84-2a56-44d4-8dca-a4bc4003fba6', 'Input/Wells/Well_Good/Completions/Plugback 1')) # plugback
        tuple_data.append( ('ab5ce842-d8b0-4d92-b219-399cfd84a695', 'Input/Wells/Global well logs/Vp')) # global well log
        tuple_data.append( ('61c5d165-211d-43ca-932f-843a6103bbaf', 'Input/Wells/Global well logs/Facies')) # discrete global well log
        tuple_data.append( ('e700c3a3-a94d-4e71-80ed-85dd4ef98cc2', 'Input/Wells/Well_Good/Well logs/GR')) # well log
        tuple_data.append( ('1a9ab912-41df-4a16-ab68-df53125b912c', 'Input/Wells/Well_Good/Well logs/Facies')) # discrete well log
        tuple_data.append( ('752f79f0-de4a-4b12-91ae-b914a02d825e', 'Input/Wells/Well_Good/XYZ')) # well survey
        tuple_data.append( ('89876478-0e72-4a49-bdf1-c2e9eed2c9fe', 'Input/WellTops/Attributes/Confidence factor')) # marker attribute
        tuple_data.append( ('2aac1a70-456b-4583-ba1f-c028be1f70b0', 'Input/WellTops/Attributes/Observation number')) # discrete marker attribute
        tuple_data.append( ('e4091f84-53cb-4cbf-935b-75bb7bc46c10', 'Input/WellTops')) # marker collection
        tuple_data.append( ('cd0de2f1-0cba-46f0-8603-c7677e94fec4', 'Models/Structural grids/Model_NoData')) # grid
        tuple_data.append( ('a539b6df-1157-4dec-92ea-430e9b692b7d', 'Models/Structural grids/Model_Good/Properties/Por')) # grid property
        tuple_data.append( ('48dd111f-6628-4ce3-b2af-ed54f2523288', 'Models/Structural grids/Model_Good/Properties/Facies-IndicatorKrig')) # discrete grid property
        tuple_data.append( ('0a3caaa5-b73e-4670-a6ac-828b5fa552d5', 'Input/Seismic/Interpretation folder 1/BCU')) # horizon interpretation
        tuple_data.append( ('c30d53f0-0578-4dfb-8598-b9925d0c553f', 'Input/Seismic/Interpretation folder 1/BCU/Ardmore')) # horizon interpretation 3d
        tuple_data.append( ('4d304154-757d-480f-bf0f-953faf11cee1', 'Input/Seismic/Interpretation folder 1/BCU/Ardmore/Autotracker: Confidence')) # horizon property 3d
        tuple_data.append( ('67233c5a-afae-460a-969e-fb6cb6a073ec', 'Input/Seismic/Ardmore/Seismic3D')) # seismic cube
        tuple_data.append( ('9b8f6ca8-39c0-40d1-b986-c874e75458bf', 'Input/Seismic/Survey 1/Seismic2D')) # seismic line
        tuple_data.append( ('178715de-59a7-4df5-98cd-ae02e998b167', 'Input/TWT Surface/BCU')) # surface
        tuple_data.append( ('fcb51e21-889e-4250-a5da-f92ca5162006', 'Input/TWT Surface/BCU/TWT')) # surface attribute
        tuple_data.append( ('2c8cd4b2-a571-4eb1-b04d-ea4085542295', 'Input/TWT Surface/BCU/Facies')) # discrete surface attribute
        tuple_data.append( ('6bbf8f8f-3af8-4fe5-bea5-ce913433dc7f', 'Input/Geometry/Points 1')) # pointset
        tuple_data.append( ('3831f635-4e33-426b-9982-ac2afb4fffd8', 'Input/Geometry/Polygon')) # polylineset

        droids = [item[0] for item in tuple_data]
        objs = petrellink.get_petrelobjects_by_guids(droids)
        for idx, obj in enumerate(objs):
            assert obj != None
            assert obj.path == tuple_data[idx][1]