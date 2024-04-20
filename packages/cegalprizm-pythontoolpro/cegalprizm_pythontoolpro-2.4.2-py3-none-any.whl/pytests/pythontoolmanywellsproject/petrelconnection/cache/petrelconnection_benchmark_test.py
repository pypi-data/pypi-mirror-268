import pytest
import pytest_benchmark
import os
import sys
import time
import numpy as np
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontoolmanywellsproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontoolmanywellsproject)], indirect=['petrel_context'])
class TestPetrelConnection_Benchmark:
    def clear_cache(self, petrellink):
        petrellink._clearcache()

    def get_first_object_after_clear(self, petrellink):
        petrellink._clearcache("well")
        obj = petrellink.wells["Input/Wells/Well_Good"]
        return obj
    
    def get_workflow_after_clear(self, petrellink):
        petrellink._clearcache("workflow")
        obj = petrellink.workflows['Workflows/New folder/return_object']
        return obj
    
    def get_seismic_after_clear(self, petrellink):
        petrellink._clearcache("seismic")
        obj = petrellink.seismic_cubes["Input/Seismic/Ardmore/Seismic3D"]
        return obj
    
    def get_object_no_clear(self, petrellink):
        obj = petrellink.seismic_cubes["Input/Seismic/Ardmore/Seismic3D"]
        return obj
    
    def get_two_subsequent_objects(self, petrellink):
        petrellink._clearcache()
        obj = petrellink.wells["Input/Wells/Well_Good"]
        obj2 = petrellink.seismic_cubes["Input/Seismic/Ardmore/Seismic3D"]
    
    def get_two_subsequent_objects_clear(self, petrellink):
        petrellink._clearcache("well")
        obj = petrellink.wells["Input/Wells/Well_Good"]
        petrellink._clearcache("seismic")
        obj2 = petrellink.seismic_cubes["Input/Seismic/Ardmore/Seismic3D"]
    
    def test_clear_cache(self, benchmark, petrellink):
        benchmark(self.clear_cache, petrellink)

    def test_petrelconnection_get_first_object_after_clear_cache(self, benchmark, petrellink):
        well = benchmark(self.get_first_object_after_clear, petrellink)
        assert well is not None

    def test_petrelconnection_get_first_workflow_after_clear_cache(self, benchmark, petrellink):
        workflow = benchmark(self.get_workflow_after_clear, petrellink)
        assert workflow is not None

    def test_petrelconnection_get_first_seismic_after_clear_cache(self, benchmark, petrellink):
        seismic = benchmark(self.get_seismic_after_clear, petrellink)
        assert seismic is not None

    def test_petrelconnection_get_two_subsequent_objects(self, benchmark, petrellink):
        benchmark(self.get_two_subsequent_objects, petrellink)

    def test_petrelconnection_get_two_subsequent_objects_clear(self, benchmark, petrellink):
        benchmark(self.get_two_subsequent_objects_clear, petrellink)

    def test_petrelconnection_get_object_cache_exists(self, benchmark, petrellink):
        petrellink._clearcache("well")
        obj = petrellink.wells["Input/Wells/Well_Good"]
        benchmark(self.get_first_object_after_clear, petrellink)

    def test_petrelconnection_get_object_and_multiple_sub_objects(self, benchmark, petrellink):
        benchmark(self.petrelconnection_get_object_and_multiple_sub_objects, petrellink)
 
    def test_petrelconnection_get_object_and_multiple_sub_objects_clear_cache(self, benchmark, petrellink):
        benchmark(self.petrelconnection_get_object_and_multiple_sub_objects_clear_cache, petrellink)

    def petrelconnection_get_object_and_multiple_sub_objects(self, petrellink):
        petrellink._clearcache("well")
        well = petrellink.wells["Input/Wells/Well_Good"]
        completions_set = well.completions_set
        casing_string = completions_set.casings[0]
        perforation = completions_set.perforations[0]
        plugback = completions_set.plugbacks[0]
        squeeze = completions_set.squeezes[0]
        
    def petrelconnection_get_object_and_multiple_sub_objects_clear_cache(self, petrellink):
        petrellink._clearcache("well")
        well = petrellink.wells["Input/Wells/Well_Good"]
        petrellink._clearcache("well")
        completions_set = well.completions_set
        petrellink._clearcache("well")
        casing_string = completions_set.casings[0]
        petrellink._clearcache("well")
        perforation = completions_set.perforations[0]
        petrellink._clearcache("well")
        plugback = completions_set.plugbacks[0]
        petrellink._clearcache("well")
        squeeze = completions_set.squeezes[0]

    def petrelconnection_get_property_no_cache(self, petrellink):
        petrellink._clearcache()
        well = petrellink._get_well_by_guid("e8b3c9b8-6fc6-429c-99e6-49733a6981ea")
        crs = well.crs_wkt
        return crs
    
    def petrelconnection_get_object_from_droid_private(self, petrellink):
        petrellink._clearcache()
        well = petrellink._get_well_by_guid("e8b3c9b8-6fc6-429c-99e6-49733a6981ea")
        return well
    
    def petrelconnection_get_object_from_droid_public(self, petrellink):
        petrellink._clearcache()
        a_list = petrellink.get_petrelobjects_by_guids(["e8b3c9b8-6fc6-429c-99e6-49733a6981ea"])
        return a_list[0]
    
    def petrelconnection_get_property_with_cache(self, petrellink):
        petrellink._clearcache()
        well = petrellink._get_well_by_guid("e8b3c9b8-6fc6-429c-99e6-49733a6981ea")
        path = well.path
        return path
    
    def test_petrelconnection_get_property_no_cache(self, benchmark, petrellink):
        crs = benchmark(self.petrelconnection_get_property_no_cache, petrellink)
        assert "ED50-UTM31" in crs

    def test_petrelconnection_get_property_with_cache(self, benchmark, petrellink):
        path = benchmark(self.petrelconnection_get_property_with_cache, petrellink)
        assert "Input/Wells/Well_Good" in path

    def test_petrelconnection_get_object_from_droid_private(self, benchmark, petrellink):
        well = benchmark(self.petrelconnection_get_object_from_droid_private, petrellink)
        assert well is not None
    
    def test_petrelconnection_get_object_from_droid_public(self, benchmark, petrellink):
        well = benchmark(self.petrelconnection_get_object_from_droid_public, petrellink)
        assert well is not None