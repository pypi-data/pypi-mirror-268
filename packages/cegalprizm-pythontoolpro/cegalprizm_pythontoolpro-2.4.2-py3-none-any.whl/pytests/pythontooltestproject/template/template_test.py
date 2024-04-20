import pytest
import os
import sys
parent_dir = os.path.abspath("../..")
sys.path.insert(0, parent_dir)
from conftest import petrel_version, pythontooltestproject

@pytest.mark.parametrize("petrel_context", [(petrel_version, pythontooltestproject)], indirect=['petrel_context'])
class TestTemplate:
    def test_template_str(self, template_acoustic_impedance):
        assert str(template_acoustic_impedance) == 'Template(petrel_name="Acoustic impedance")'

    def test_template_petrel_name(self, template_acoustic_impedance):
        assert template_acoustic_impedance.petrel_name == 'Acoustic impedance'

    def test_template_path(self, template_acoustic_impedance):
        assert template_acoustic_impedance.path == 'Templates/Geophysical templates/Acoustic impedance'

    def test_template_droid(self, template_acoustic_impedance):
        assert template_acoustic_impedance.droid == '000000a1-0000-0000-0000-000000000000'

    def test_template_unit_symbol(self, template_acoustic_impedance):
        assert template_acoustic_impedance.unit_symbol == 'kPa.s/m'

    def test_template_workflow_enabled(self, template_acoustic_impedance, return_workflow):
        input_var = return_workflow.input["input_object"]
        output_var = return_workflow.output["output_object"]
        wf_result = return_workflow.run({input_var: template_acoustic_impedance})
        unpacked_object = wf_result[output_var]
        assert isinstance(unpacked_object, type(template_acoustic_impedance))
        assert unpacked_object.petrel_name == template_acoustic_impedance.petrel_name
        assert unpacked_object.path == template_acoustic_impedance.path
        assert unpacked_object.droid == template_acoustic_impedance.droid

    def test_template_units(self, template_acoustic_impedance):
        units = template_acoustic_impedance._available_units
        assert isinstance(units, list)
        assert len(units) == 17
        assert '1000 kPa.s/m' in units
        assert 'ft.g/(s.cm3)' in units
        assert 'g.ft/(cm3.s)' in units
        assert 'g/(m2.d)' in units
        assert 'g/cc.m/s' in units
        assert 'kg/(m2.a)' in units
        assert 'kg/(m2.s)' in units
        assert 'kPa.s/m' in units
        assert 'lbm/(ft2.a)' in units
        assert 'lbm/(ft2.s)' in units
        assert 'MPa.s/m' in units
        assert 'Mrayl' in units
        assert 'Mt/(km2.Ma)' in units
        assert 'Mt/(m2.Ma)' in units
        assert 'Pa.s/m' in units
        assert 'rayl' in units
        assert 't/(m2.Ma)' in units
        assert 'm/s' not in units