import pytest
import sys
import os
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=["petrel_context"])
class TestSurfaces:
    def test_surfaces_template(self, surface):
        surfaces = surface.parent_collection
        assert surfaces.template == ''
    
    def test_surfaces_get_indexed_item(self, surface):
        from cegalprizm.pythontool.surface import Surface
        surfaces = surface.parent_collection
        selected_surface = surfaces[0]
        assert isinstance(selected_surface, Surface)