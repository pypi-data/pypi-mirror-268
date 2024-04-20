# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from datetime import datetime
import typing

from cegalprizm.pythontool.grpc import completions_casingstring_grpc, completions_perforation_grpc, completions_plugback_grpc, completions_squeeze_grpc, grid_grpc, zone_grpc #GridGrpc
from cegalprizm.pythontool.grpc import gridproperty_grpc#GridPropertyGrpc, GridDiscretePropertyGrpc, PropertyCollectionGrpc
from cegalprizm.pythontool.grpc import surface_grpc #SurfaceGrpc, SurfacePropertyGrpc, SurfaceDiscretePropertyGrpc
from cegalprizm.pythontool.grpc import seismic_grpc #Seismic2DGrpc, SeismicCubeGrpc 
from cegalprizm.pythontool.grpc import borehole_grpc #BoreholeGrpc, WellLogGrpc, DiscreteWellLogGrpc, GlobalWellLogGrpc, DiscreteGlobalWellLogGrpc
from cegalprizm.pythontool.grpc import borehole_collection_grpc #BoreholeCollectionGrpc
from cegalprizm.pythontool.grpc import markerattribute_grpc #MarkerAttributeGrpc
from cegalprizm.pythontool.grpc import markercollection_grpc #MarkerCollectionGrpc
from cegalprizm.pythontool.grpc import points_grpc #PointSetGrpc
from cegalprizm.pythontool.grpc import polylines_grpc #PolylineSetGrpc
from cegalprizm.pythontool.grpc import wavelet_grpc #WaveletGrpc
from cegalprizm.pythontool.grpc import wellsurvey_grpc #XyzWellSurveyGrpc, XytvdWellSurveyGrpc, DxdytvdWellSurveyGrpc, MdinclazimWellSurveyGrpc, ExplicitWellSurveyGrpc
from cegalprizm.pythontool.grpc import horizoninterpretation_grpc #HorizonInterpretation3dGrpc, HorizonProperty3dGrpc, HorizonInterpretationGrpc
from cegalprizm.pythontool.grpc import workflow_grpc #ReferenceVariableGrpc, WorkflowGrpc
from cegalprizm.pythontool.grpc import observeddata_grpc #ObservedDataSetGrpc, ObservedDataGrpc
from cegalprizm.pythontool.grpc import template_grpc #TemplateGrpc, DiscreteTemplateGrpc
from cegalprizm.pythontool.grpc import checkshot_grpc
from cegalprizm.pythontool.grpc import segment_grpc
from cegalprizm.pythontool.grpc import petrelinterface_pb2

def pb_PetrelObjectRef_to_grpcobj(pog, plink):
    if pog is None:
        return None
    elif pog.sub_type == "grid":
        pol = grid_grpc.GridGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "grid property":
        pol = gridproperty_grpc.GridPropertyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "grid discrete property":
        pol = gridproperty_grpc.GridDiscretePropertyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "surface":
        pol = surface_grpc.SurfaceGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "surface property":
        pol = surface_grpc.SurfacePropertyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "surface discrete property":
        pol = surface_grpc.SurfaceDiscretePropertyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "surface collection":
        pol = surface_grpc.SurfaceCollectionGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "marker collection":
        pol = markercollection_grpc.MarkerCollectionGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "marker attribute":
        pol = markerattribute_grpc.MarkerAttributeGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "borehole":
        pol = borehole_grpc.BoreholeGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "borehole collection":
        pol = borehole_collection_grpc.BoreholeCollectionGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "well log":
        pol = borehole_grpc.WellLogGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "discrete well log":
        pol = borehole_grpc.DiscreteWellLogGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "global well log":
        pol = borehole_grpc.GlobalWellLogGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "global discrete well log":
        pol = borehole_grpc.DiscreteGlobalWellLogGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "seismic cube":
        pol = seismic_grpc.SeismicCubeGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "seismic 2d":
        pol = seismic_grpc.Seismic2DGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "global observed data set":
        pol = observeddata_grpc.GlobalObservedDataSetsGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "observed data set":
        pol = observeddata_grpc.ObservedDataSetGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "observed data":
        pol = observeddata_grpc.ObservedDataGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "property collection":
        pol = gridproperty_grpc.PropertyCollectionGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "pointset":
        pol = points_grpc.PointSetGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "polylineset":
        pol = polylines_grpc.PolylineSetGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "horizon property 3d":
        pol = horizoninterpretation_grpc.HorizonProperty3dGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "horizon interpretation 3d":
        pol = horizoninterpretation_grpc.HorizonInterpretation3dGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "horizon interpretation":
        pol = horizoninterpretation_grpc.HorizonInterpretationGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "wavelet":
        pol = wavelet_grpc.WaveletGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "xyz well survey":
        pol = wellsurvey_grpc.XyzWellSurveyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "xytvd well survey":
        pol = wellsurvey_grpc.XytvdWellSurveyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "dxdytvd well survey":
        pol = wellsurvey_grpc.DxdytvdWellSurveyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "mdinclazim well survey":
        pol = wellsurvey_grpc.MdinclazimWellSurveyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "explicit well survey":
        pol = wellsurvey_grpc.ExplicitWellSurveyGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "referencevariable":
        pol = workflow_grpc.ReferenceVariableGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "workflow":
        pol = workflow_grpc.WorkflowGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "template":
        pol = template_grpc.TemplateGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "discrete template":
        pol = template_grpc.DiscreteTemplateGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "checkshot":
        pol = checkshot_grpc.CheckShotGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "casing string":
        pol = completions_casingstring_grpc.CasingStringGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "perforation":
        pol = completions_perforation_grpc.PerforationGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "squeeze":
        pol = completions_squeeze_grpc.SqueezeGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "plugback":
        pol = completions_plugback_grpc.PlugbackGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "zone":
        pol = zone_grpc.ZoneGrpc(pog.guid, plink)
        return pol
    elif pog.sub_type == "segment":
        pol = segment_grpc.SegmentGrpc(pog.guid, plink)
        return pol

def datetime_to_pb_date(datetime: datetime):
    grpcDate = petrelinterface_pb2.Date(
            year = datetime.year,
            month = datetime.month,
            day = datetime.day,
            hour = datetime.hour,
            minute = datetime.minute,
            second = datetime.second
        )
    return grpcDate

def isFloat(value) -> bool:
        if 'float' in str(type(value)).lower():
            return True
        return False

def GetWellGuid(borehole) -> petrelinterface_pb2.PetrelObjectGuid:
        well_guid = None
        if borehole is not None:
            well_guid = petrelinterface_pb2.PetrelObjectGuid(guid = borehole._borehole_object_link._guid, sub_type = borehole._borehole_object_link._sub_type)
        return well_guid
    

def GetWellGuids(boreholes) -> petrelinterface_pb2.PetrelObjectGuid:
        well_guids = []
        for borehole in boreholes:
            if borehole is not None:
                well_guids.append(GetWellGuid(borehole))
        return well_guids