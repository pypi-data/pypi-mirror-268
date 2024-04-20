import pytest
import subprocess
from cegalprizm.hub import Hub, ConnectorFilter
from pathlib import Path
import psutil
import os
import logging

logging.basicConfig()
logger=logging.getLogger()

petrel_version_override = 2021
try:
    petrel_version = os.environ["PRIZM_PETREL_VERSION"]
except: 
    petrel_version = petrel_version_override

hub_local_path = r".\pytests\cegalhub\hub_local.ps1"
teardown_script_path = r".\pytests\cegalhub\hub_petrel_teardown.ps1"
if os.environ.get("USERNAME").lower() == "vmadministrator":  # if running on azure devops:
    directory = os.environ.get("BUILD_ARTIFACTSTAGINGDIRECTORY")
    pythontoolgridsproject = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolGridsProject", "PythonToolGridsProject" + ".pet") 
    pythontooltestproject = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolTestProject", "PythonToolTestProject" + ".pet")
    pythontooltestproject2 = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolTestProject2", "PythonToolTestProject2" + ".pet")
    pythontoolmanywellsproject = os.path.join(directory, "PetrelUnitTestFramework", "PythonToolManyWellsProject", "PythonToolManyWellsProject" + ".pet")
    hub_local_path = r".\pytests\cegalhub\hub_local_" + str(petrel_version) + r"_azdo.ps1"
else:
    if petrel_version_override is not None:
        petrel_version = petrel_version_override
    home_path = os.environ.get("BBR_UNIT_TEST_FRAMEWORK_FOLDER")
    if home_path is None:
        home_path = str(Path.home())
        pythontoolgridsproject = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolGridsProject\PythonToolGridsProject.pet"
        pythontooltestproject = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolTestProject\PythonToolTestProject.pet"
        pythontooltestproject2 = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolTestProject2\PythonToolTestProject2.pet"
        pythontoolmanywellsproject = home_path + r"\OneDrive - Cegal AS\Documents\PetrelUnitTestFramework\1\PythonToolManyWellsProject\PythonToolManyWellsProject.pet"

def process_exists(process_name: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def initialize_hub_local():
    process = subprocess.Popen(["powershell.exe", hub_local_path], stdout=subprocess.PIPE)
    print('')
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
        if ("Agent configured to allow scripts." in output.decode()):
            logger.info("Hub in Local mode initialized! Ready for test.")
            break
    return process

def initialize_teardown_script():
    process = subprocess.Popen(["powershell.exe", teardown_script_path], stdout=subprocess.PIPE)

def pytest_configure(config):
    pytest.petrel_was_already_running = True
    if not process_exists('cegalhub'):
        pytest.petrel_was_already_running = False
        initialize_hub_local()

def pytest_unconfigure(config):
    hub = Hub()
    connectionfilter = ConnectorFilter(labels_dict = {'gui': 'false'})
    headless_petrel = len(hub.query_connectors(connector_filter=connectionfilter)) > 0
    if headless_petrel:
        initialize_teardown_script()

def get_petrel_version(petrellink, hub):
    petrel_version = hub.query_connectors(connector_filter=petrellink._ptp_hub_ctx.connector_filter)[0].labels.get('petrel-major-version')
    return petrel_version

def get_current_petrel_project(petrel_context, hub):
    path_to_current_loaded_project = hub.query_connectors(connector_filter=petrel_context.connector_filter)[0].labels.get('primary-project-path')
    return path_to_current_loaded_project

def petrel_is_running(hub):
    is_running = True
    petrel_connector = hub.query_connectors('cegal.hub.petrel')
    if len(petrel_connector) == 0:
        is_running = False
    return is_running

@pytest.fixture(scope="package")
def petrellink(petrel_context):
    from cegalprizm.pythontool.petrelconnection import PetrelConnection
    petrellink = PetrelConnection(allow_experimental=True, petrel_ctx=petrel_context)
    yield petrellink

@pytest.fixture(scope="package")
def hub():
    hub = Hub()
    yield hub

@pytest.fixture(scope="package")
def petrel_context(request, hub):
    if petrel_is_running(hub):
        petrel_ctx = hub.default_petrel_ctx()
    else:
        agent_ctx = hub.default_agent_ctx()
        petrel_ctx = agent_ctx.new_petrel_instance(petrel_version=request.param[0], connect_timeout_secs=720)

    path_to_current_loaded_project = get_current_petrel_project(petrel_ctx, hub)
    if path_to_current_loaded_project.lower() != request.param[1].lower():
        print('Loading project: ' + request.param[1])
        petrel_ctx.load_project(path=request.param[1])
    yield petrel_ctx

@pytest.fixture(scope="package")
def petrel_version_fixture(petrellink, hub):
    petrel_version = get_petrel_version(petrellink, hub)
    yield int(petrel_version)

@pytest.fixture(scope="package")
def checkshot_all(petrellink):
    checkshot_all = petrellink.checkshots["Input/Wells/Global well logs/AllCheckShots.txt"]
    yield checkshot_all

@pytest.fixture(scope="package")
def checkshot_user_properties(petrellink):
    checkshot_user_properties = petrellink.checkshots['Input/Wells/Global well logs/CheckShots/AllTheCheckShotProperties']
    yield checkshot_user_properties

@pytest.fixture(scope="package")
def checkshot_other(petrellink):
    checkshot_other = petrellink.checkshots["Input/Wells/Global well logs/CheckShots/AnotherLevel/SomeOtherCheckShots.txt"]
    yield checkshot_other

@pytest.fixture(scope="package")
def welltops(petrellink):
    welltops = petrellink.markercollections['Input/WellTops']
    yield welltops

@pytest.fixture(scope="package")
def wellb1(petrellink):
    wellb1 = petrellink.wells['Input/Wells/B Wells/B1']
    yield wellb1

@pytest.fixture(scope="package")
def wellb2(petrellink):
    wellb2 = petrellink.wells['Input/Wells/B Wells/B2']
    yield wellb2

@pytest.fixture(scope="package")
def wellb8(petrellink):
    wellb8 = petrellink.wells['Input/Wells/B Wells/B8']
    yield wellb8

@pytest.fixture(scope="package")
def well_good(petrellink):
    well_good = petrellink.wells['Input/Wells/Well_Good']
    yield well_good

@pytest.fixture(scope="package")
def completions_set(petrellink):
    well = petrellink.wells['Input/Wells/Well_Good']
    completions_set = well.completions_set
    yield completions_set

@pytest.fixture(scope="package")
def completions_set_empty(petrellink):
    well = petrellink.wells['Input/Wells/Well_Good lateral']
    completions_set = well.completions_set
    yield completions_set

@pytest.fixture(scope="package")
def delete_workflow(petrellink):
    delete_workflow = petrellink.workflows['Workflows/New folder/delete_object']
    yield delete_workflow

@pytest.fixture(scope="package")
def return_workflow(petrellink):
    return_workflow = petrellink.workflows['Workflows/New folder/return_object']
    yield return_workflow

@pytest.fixture(scope="package")
def pointset_empty(petrellink):
    pointset_empty = petrellink.pointsets['Input/Geometry/Points empty']
    yield pointset_empty

@pytest.fixture(scope="package")
def pointset_noattributes(petrellink):
    pointset_noattributes = petrellink.pointsets['Input/Geometry/Points no attributes']
    yield pointset_noattributes

@pytest.fixture(scope="package")
def pointset(petrellink):
    pointset = petrellink.pointsets['Input/Geometry/Points 1']
    yield pointset

@pytest.fixture(scope="package")
def pointset_many(petrellink):
    pointset_many = petrellink.pointsets['Input/Geometry/Points 1 many points']
    yield pointset_many

@pytest.fixture(scope="package")
def pointset_custom_property_units(petrellink):
    pointset_empty = petrellink.pointsets['Input/Geometry/Copy of Points 1 many points']
    yield pointset_empty

@pytest.fixture()
def cloned_pointset_custom_property_units(petrellink):
    pointset = petrellink.pointsets['Input/Geometry/Copy of Points 1 many points']
    clone = pointset.clone('Points 1_copy 2', copy_values = True)
    yield clone
    delete_workflow = petrellink.workflows['Workflows/New folder/delete_object']
    obj = delete_workflow.input['object']
    delete_workflow.run({obj: clone})

@pytest.fixture()
def global_observed_data_set(petrellink):
    globalobserveddata = petrellink.global_observed_data_sets["Input/Wells/Global observed data/Observed data sets/Observed"]
    yield globalobserveddata

@pytest.fixture()
def cloned_global_observed_data_set(petrellink):
    globalobserveddata = petrellink.global_observed_data_sets["Input/Wells/Global observed data/Observed data sets/Observed"]
    clone = globalobserveddata.clone('datasetclone')
    yield clone
    delete_workflow = petrellink.workflows['Workflows/New folder/delete_object']
    obj = delete_workflow.input['object']
    delete_workflow.run({obj: clone})

@pytest.fixture()
def seismic_cube(petrellink):
    seismic_cube = petrellink.seismic_cubes['Input/Seismic/Ardmore/Seismic3D']
    yield seismic_cube

@pytest.fixture(scope="package")
def grid(petrellink):
    grid = petrellink.grids['Models/Segmented model/Segmented grid']
    yield grid

@pytest.fixture()
def model_grid(petrellink):
    model_grid = petrellink.grids["Models/Structural grids/Model_Good"]
    yield model_grid

@pytest.fixture()
def grid_noprops(petrellink):
    model = petrellink.grids['Models/Structural grids/Model_NoProperties']
    yield model

@pytest.fixture()
def grid_property_ai(petrellink):
    grid_property = petrellink.grid_properties['Models/Structural grids/Model_Good/Properties/AI']
    yield grid_property

@pytest.fixture()
def grid_property_rho(petrellink):
    grid_property = petrellink.grid_properties['Models/Structural grids/Model_NoData/Properties/Rho']
    yield grid_property

@pytest.fixture()
def grid_property_vp(petrellink):
    grid_property = petrellink.grid_properties['Models/Structural grids/Model_Good/Properties/Vp']
    yield grid_property

@pytest.fixture()
def grid_property_crazy_por(petrellink):
    grid_property = petrellink.grid_properties['Models/Structural grids/Model_Crazy/Properties/Por']
    yield grid_property

@pytest.fixture()
def discrete_grid_property_good(petrellink):
    discrete_grid_property_good = petrellink.discrete_grid_properties['Models/Structural grids/Model_Good/Properties/Facies']
    yield discrete_grid_property_good

@pytest.fixture()
def discrete_grid_property_layers(petrellink):
    discrete_grid_property_layers = petrellink.discrete_grid_properties['Models/Structural grids/Model_Good/Properties/Layers']
    yield discrete_grid_property_layers

@pytest.fixture()
def discrete_grid_property_nodata(petrellink):
    discrete_grid_property_nodata = petrellink.discrete_grid_properties['Models/Structural grids/Model_NoData/Properties/Facies']
    yield discrete_grid_property_nodata

@pytest.fixture()
def surface(petrellink):
    surface = petrellink.surfaces["Input/TWT Surface/BCU"]
    yield surface

@pytest.fixture()
def surface_attribute(petrellink):
    surface_attribute = petrellink.surface_attributes["Input/TWT Surface/BCU/TWT"]
    yield surface_attribute

@pytest.fixture()
def surface_attribute_discrete(petrellink):
    surface_attribute_discrete = petrellink.discrete_surface_attributes["Input/TWT Surface/BCU/Facies"]
    yield surface_attribute_discrete

@pytest.fixture()
def interpretation(petrellink):
    interpretation = petrellink.horizon_interpretation_3ds['Input/Seismic/Interpretation folder 1/BCU/Ardmore']
    yield interpretation

@pytest.fixture()
def seismic_pointset(petrellink):
    seismic_pointset = petrellink.pointsets['Input/Geometry/Seismic_pointset']
    yield seismic_pointset

@pytest.fixture()   
def well_good_explicit_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/Explicit survey 1']
    assert(survey.well_survey_type == 'Explicit survey')
    yield survey

@pytest.fixture()
def well_good_xyz_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/XYZ']
    assert(survey.well_survey_type == 'X Y Z survey')
    yield survey

@pytest.fixture()
def well_good_xyz_invalid_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/XYZ invalid trajectory']
    assert(survey.well_survey_type == 'X Y Z survey')
    yield survey

@pytest.fixture()
def well_good_xytvd_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/XYTVD']
    assert(survey.well_survey_type == 'X Y TVD survey')
    yield survey

@pytest.fixture()
def well_good_xytvd_invalid_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/XYTVD invalid trajectory']
    assert(survey.well_survey_type == 'X Y TVD survey')
    yield survey

@pytest.fixture()
def well_good_dxdytvd_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/DXDYTVD']
    assert(survey.well_survey_type == 'DX DY TVD survey')
    yield survey

@pytest.fixture()
def well_good_dxdytvd_invalid_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/DXDYTVD invalid trajectory']
    assert(survey.well_survey_type == 'DX DY TVD survey')
    yield survey

@pytest.fixture()
def well_good_mdinclazim_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/MDINCLAZIM']
    assert(survey.well_survey_type == 'MD inclination azimuth survey')
    yield survey

@pytest.fixture()
def well_good_mdinclazim_invalid_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good/MDINCLAZIM invalid trajectory']
    assert(survey.well_survey_type == 'MD inclination azimuth survey')
    yield survey

@pytest.fixture()
def well_good_lateral_xytvd_survey_lateral_to_explicit(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good lateral/XYTVD lateral to explicit']
    yield survey

@pytest.fixture()
def well_good_lateral_xyz_survey(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good lateral/XYZ lateral']
    yield survey

@pytest.fixture()
def well_good_lateral_xytvd_survey_lateral(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good lateral/XYTVD lateral']
    yield survey

@pytest.fixture()
def well_good_lateral_dxdytvd_survey_lateral(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good lateral/DXDYTVD lateral']
    yield survey

@pytest.fixture()
def well_good_lateral_mdinclazim_survey_lateral(petrellink):
    survey = petrellink.well_surveys['Input/Wells/Well_Good lateral/MDINCLAZIM lateral']
    yield survey

@pytest.fixture()
def template_acoustic_impedance(petrellink):
    template = petrellink.templates['Templates/Geophysical templates/Acoustic impedance']
    yield template

@pytest.fixture()
def discrete_template_facies(petrellink):
    template = petrellink.discrete_templates['Templates/Discrete property templates/Facies']
    yield template

@pytest.fixture()
def discrete_global_well_log_facies(petrellink):
    log = petrellink.discrete_global_well_logs['Input/Wells/Global well logs/Facies']
    yield log

@pytest.fixture()
def discrete_well_log(petrellink):
    log = petrellink.discrete_well_logs['Input/Wells/Well_Good/Well logs/Facies']
    yield log

@pytest.fixture()
def global_well_log(petrellink):
    log = petrellink.global_well_logs['Input/Wells/Global well logs/LambdaRho']
    yield log

@pytest.fixture()
def horizon_interpretation(petrellink):
    horizon_interpretation = petrellink.horizon_interpretations['Input/Seismic/Interpretation folder 1/BCU']
    yield horizon_interpretation

@pytest.fixture()
def horizon_interpretation_3d(petrellink):
    horizon_interpretation = petrellink.horizon_interpretation_3ds['Input/Seismic/Interpretation folder 1/BCU/Ardmore']
    yield horizon_interpretation

@pytest.fixture()
def horizon_property(petrellink):
    horizon_property = petrellink.horizon_properties['Input/Seismic/Interpretation folder 1/BCU/Ardmore/TWT']
    yield horizon_property

@pytest.fixture()
def horizon_property_autotracker_confidence(petrellink):
    horizon_property = petrellink.horizon_properties['Input/Seismic/Interpretation folder 1/BCU/Ardmore/Autotracker: Confidence']
    yield horizon_property

@pytest.fixture()
def polylineset(petrellink):
    polylineset = petrellink.polylinesets['Input/Geometry/Polygon']
    yield polylineset

@pytest.fixture()
def polylineset_no_attributes(petrellink):
    polylineset_no_attributes = petrellink.polylinesets['Input/Geometry/Polygon no attributes']
    yield polylineset_no_attributes

@pytest.fixture()
def property_collection(petrellink):
    property_collection = petrellink.property_collections['Models/Structural grids/Model_NoProperties/Properties']
    yield property_collection

@pytest.fixture()
def seismic_2d(petrellink):
    seismic_2d = petrellink.seismic_2ds['Input/Seismic/Survey 1/Seismic2D']
    yield seismic_2d

@pytest.fixture()
def seismic_cube_tiny3d(petrellink):
    seismic_cube = petrellink.seismic_cubes['Input/Seismic/Survey 2/Tiny3D']
    yield seismic_cube

@pytest.fixture()
def seismic_cube_ardmore_seismic3d(petrellink):
    seismic_cube = petrellink.seismic_cubes['Input/Seismic/Ardmore/Seismic3D']
    yield seismic_cube

@pytest.fixture()
def seismic_line(petrellink):
    seismic_line = petrellink.seismic_lines['Input/Seismic/Survey 1/Seismic2D']
    yield seismic_line

@pytest.fixture()
def well_log(petrellink):
    log = petrellink.well_logs['Input/Wells/Well_Good/Well logs/Vp_K']
    yield log

@pytest.fixture()
def well_log_vs(petrellink):
    log = petrellink.well_logs['Input/Wells/Well_Good/Well logs/Vs']
    yield log

@pytest.fixture()
def observed_data(well_good):
    obs = well_good.observed_data_sets[0]
    ob = obs.observed_data[0]
    yield ob

@pytest.fixture()
def observed_data_set(well_good):
    obs = well_good.observed_data_sets[0]
    yield obs

@pytest.fixture()
def segment(grid):
    segment = grid.segments[0]
    yield segment

@pytest.fixture()
def wavelet(petrellink):
    wavelet = petrellink.wavelets['Input/Wavelet 1']
    yield wavelet

@pytest.fixture()
def zone(grid):
    zone = grid.zones[0]
    yield zone

# GRID PROJECT FIXTURES

@pytest.fixture()
def grid_model_115(petrellink):
    grid = petrellink.grids['Models/New model/LHInv-115-Ti']
    yield grid

@pytest.fixture()
def grid_model_155(petrellink):
    grid = petrellink.grids['Models/New model/LHInv-155-Ti']
    yield grid

@pytest.fixture()
def grid_model_515(petrellink):
    grid = petrellink.grids['Models/New model/LHInv-515-Ti']
    yield grid

@pytest.fixture()
def grid_model_555(petrellink):
    grid = petrellink.grids['Models/New model/LHInv-555-Ti']
    yield grid

@pytest.fixture()
def grid_model_111(petrellink):
    grid = petrellink.grids['Models/New model/RH-111-Ti']
    yield grid

@pytest.fixture()
def grid_model_151(petrellink):
    grid = petrellink.grids['Models/New model/RH-151-Ti']
    yield grid

@pytest.fixture()
def grid_model_511(petrellink):
    grid = petrellink.grids['Models/New model/RH-511-Ti']
    yield grid

@pytest.fixture()
def grid_model_551(petrellink):
    grid = petrellink.grids['Models/New model/RH-551-Ti']
    yield grid

@pytest.fixture()
def grid_property_115(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/LHInv-115-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_155(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/LHInv-155-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_515(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/LHInv-515-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_555(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/LHInv-555-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_111(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/RH-111-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_151(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/RH-151-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_511(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/RH-511-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_551(petrellink):
    grid_property = petrellink.grid_properties['Models/New model/RH-551-Ti/Properties/IJK cell value']
    yield grid_property

@pytest.fixture()
def grid_property_discrete_115(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/LHInv-115-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_155(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/LHInv-155-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_515(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/LHInv-515-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_555(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/LHInv-555-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_111(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/RH-111-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_151(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/RH-151-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_511(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/RH-511-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop

@pytest.fixture()
def grid_property_discrete_551(petrellink):
    disc_prop = petrellink.discrete_grid_properties['Models/New model/RH-551-Ti/Properties/discrete_IJK_cell_value']
    yield disc_prop