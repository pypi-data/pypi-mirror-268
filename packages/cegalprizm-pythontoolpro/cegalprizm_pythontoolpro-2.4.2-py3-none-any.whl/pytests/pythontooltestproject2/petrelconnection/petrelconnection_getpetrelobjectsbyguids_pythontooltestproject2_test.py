import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject2

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject2)], indirect=['petrel_context'])
class TestPetrelConnection_GetPetrelObjectsByGuids_PythonToolTestProject2:

    def test_petrelconnection_getpetrelobjectsbyguids_check_path(self, petrellink):  
        tuple_data = []
        tuple_data.append( ('156b55f3-785f-45b1-9353-b35cda633a43', 'Input/Wavelet 1')) # wavelet
        tuple_data.append( ('6443affb-ddf5-4417-adc5-4688912203ef', 'Input/Wells/Well_Good/Observed/Bottom hole pressure')) # observed data
        tuple_data.append( ('25b53092-15ee-4849-835b-81ab36bd4e4c', 'Input/Wells/Global observed data/Observed data sets/Observed')) # global observed data set
        tuple_data.append( ('3bab68c7-86c4-45c6-91b0-71dd2f0aa242', 'Models/Structural grids/Model_Good/Properties/Subfolder')) # property collection
        tuple_data.append( ('b954436e-52bc-4976-a52e-2da6bb9e27f8', 'Models/Segmented model/Segmented grid/Zone filter/DPT_BCU - DPT_BaseZechestein')) # zone

        # domain object with no valid droid in petrel. they have .droid property because inheriting from PetrelObject, but that is the id coming from cache.
        # observed data set
        # segment

        droids = [item[0] for item in tuple_data]
        objs = petrellink.get_petrelobjects_by_guids(droids)
        for idx, obj in enumerate(objs):
            assert obj != None
            assert obj.path == tuple_data[idx][1]