# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool.completions_casingstring import CasingString
from cegalprizm.pythontool.completions_perforation import Perforation
from cegalprizm.pythontool.completions_plugback import Plugback
from cegalprizm.pythontool.completions_squeeze import Squeeze
from cegalprizm.pythontool.petrelobject import PetrelObject
import datetime

from cegalprizm.pythontool.checkshot import CheckShot
from cegalprizm.pythontool.grid import Grid
from cegalprizm.pythontool.gridproperty import GridProperty, GridDiscreteProperty, PropertyCollection
from cegalprizm.pythontool.surface import Surface, SurfaceAttribute, SurfaceDiscreteAttribute, Surfaces
from cegalprizm.pythontool.markerattribute import MarkerAttribute
from cegalprizm.pythontool.markercollection import MarkerCollection
from cegalprizm.pythontool.borehole import Well
from cegalprizm.pythontool.wellfolder import WellFolder
from cegalprizm.pythontool.welllog import WellLog, DiscreteWellLog, GlobalWellLog, DiscreteGlobalWellLog
from cegalprizm.pythontool.observeddata import ObservedData, ObservedDataSet, GlobalObservedDataSet
from cegalprizm.pythontool.points import PointSet
from cegalprizm.pythontool.polylines import PolylineSet
from cegalprizm.pythontool.horizoninterpretation import HorizonInterpretation3d, HorizonProperty3d, HorizonInterpretation
from cegalprizm.pythontool.seismic import SeismicCube, SeismicLine
from cegalprizm.pythontool.wavelet import Wavelet
from cegalprizm.pythontool.wellsurvey import WellSurvey
from cegalprizm.pythontool.template import Template, DiscreteTemplate

import typing

from cegalprizm.pythontool.zone import Zone
from cegalprizm.pythontool.segment import Segment

if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.workflow_grpc import WorkflowGrpc

class ReferenceVariable(PetrelObject):
    def __hash__(self):
        return hash((self.droid, self.path))

    def __eq__(self, other) -> bool:
        try:
            return (self.droid, self.petrel_name) == (other.droid, other.petrel_name)
        except:
            return False

    def __init__(self, python_reference_variable_object):
        super(ReferenceVariable, self).__init__(python_reference_variable_object)

    def __str__(self) -> str:
        return 'ReferenceVariable(petrel_name="{0}")'.format(self.petrel_name)

def _pb_PetrelObjectGuid_to_pyobj(pol):
    if pol is None:
        return None
    if pol._sub_type == "grid":
        return Grid(pol)
    elif pol._sub_type == "grid property":
        return GridProperty(pol)
    elif pol._sub_type == "grid discrete property":
        return GridDiscreteProperty(pol)
    elif pol._sub_type == "surface":
        return Surface(pol)
    elif pol._sub_type == "surface property":
        return SurfaceAttribute(pol)
    elif pol._sub_type == "surface discrete property":
        return SurfaceDiscreteAttribute(pol)
    elif pol._sub_type == "surface collection":
        return Surfaces(pol)
    elif pol._sub_type == "marker collection":
        return MarkerCollection(pol)
    elif pol._sub_type == "borehole":
        return Well(pol)
    elif pol._sub_type == "borehole collection":
        return WellFolder(pol)
    elif pol._sub_type == "well log":
        return WellLog(pol)
    elif pol._sub_type == "discrete well log":
        return DiscreteWellLog(pol)
    elif pol._sub_type == "global well log":
        return GlobalWellLog(pol)
    elif pol._sub_type == "global discrete well log":
        return DiscreteGlobalWellLog(pol)
    elif pol._sub_type == "seismic cube":
        return SeismicCube(pol)
    elif pol._sub_type == "seismic 2d":
        return SeismicLine(pol)
    elif pol._sub_type == "global observed data set":
        return GlobalObservedDataSet(pol)
    elif pol._sub_type == "observed data set":
        return ObservedDataSet(pol)
    elif pol._sub_type == "observed data":
        return ObservedData(pol)
    elif pol._sub_type == "property collection":
        return PropertyCollection(pol)
    elif pol._sub_type == "pointset":
        return PointSet(pol)
    elif pol._sub_type == "polylineset":
        return PolylineSet(pol)
    elif pol._sub_type == "horizon property 3d":
        return HorizonProperty3d(pol)
    elif pol._sub_type == "horizon interpretation 3d":
        return HorizonInterpretation3d(pol)
    elif pol._sub_type == "horizon interpretation":
        return HorizonInterpretation(pol)
    elif pol._sub_type == "wavelet":
        return Wavelet(pol)
    elif pol._sub_type == "xyz well survey":
        return WellSurvey(pol)
    elif pol._sub_type == "xytvd well survey":
        return WellSurvey(pol)
    elif pol._sub_type == "dxdytvd well survey":
        return WellSurvey(pol)
    elif pol._sub_type == "mdinclazim well survey":
        return WellSurvey(pol)
    elif pol._sub_type == "explicit well survey":
        return WellSurvey(pol)
    elif pol._sub_type == "template":
        return Template(pol)
    elif pol._sub_type == "discrete template":
        return DiscreteTemplate(pol)
    elif pol._sub_type == "referencevariable":
        return ReferenceVariable(pol)
    elif pol._sub_type == "workflow":
        return Workflow(pol)
    elif pol._sub_type == "checkshot":
        return CheckShot(pol)
    elif pol._sub_type == "marker attribute":
        return MarkerAttribute(pol)
    elif pol._sub_type == "casing string":
        return CasingString(pol)
    elif pol._sub_type == "perforation":
        return Perforation(pol)
    elif pol._sub_type == "squeeze":
        return Squeeze(pol)
    elif pol._sub_type == "plugback":
        return Plugback(pol)
    elif pol._sub_type == "zone":
        return Zone(pol)
    elif pol._sub_type == "segment":
        return Segment(pol)

class Workflow(PetrelObject):
    """A class holding information about a Petrel workflow"""

    def __init__(self, python_workflow_object: "WorkflowGrpc"):
        super(Workflow, self).__init__(python_workflow_object)
        self._workflow_object_link = python_workflow_object

    @property
    def input(self) -> typing.Dict[str, ReferenceVariable]:
        """The input variables for the workflow

        Returns:
            cegalprizm.pythontool.workflow.ReferenceVariable: the input variables for the workflow
        """        
        ref_vars = [ReferenceVariable(obj) for obj in self._workflow_object_link.GetWorkflowInputReferences()]
        return dict([(r.petrel_name, r) for r in ref_vars])

    @property
    def output(self) -> typing.Dict[str, ReferenceVariable]:
        """The output variables for the workflow

        Returns:
            cegalprizm.pythontool.workflow.ReferenceVariable: the output variables for the workflow
        """        
        ref_vars = [ReferenceVariable(obj) for obj in self._workflow_object_link.GetWorkflowOutputReferences()]
        return dict([(r.petrel_name, r) for r in ref_vars])

    def __str__(self) -> str:
        return 'Workflow(petrel_name="{0}")'.format(self.petrel_name)

    def run(self, 
            args: typing.Optional[typing.Dict[typing.Union[str,ReferenceVariable], typing.Union[str, float, int, bool, datetime.datetime, PetrelObject]]] = None,
            return_strings: typing.List[str] = [],
            return_numerics: typing.List[str] = [],
            return_dates: typing.List[str] = []
        )\
            -> typing.Dict[ReferenceVariable, typing.Union[PetrelObject, None]]:
        """Executes the workflow in Petrel.

        Args:
         A dictionary with input variables as keys and input as values. It is possible to define additional input variables in this dictionary.
        """
        if args is None:
            args = {}
        referenceVars = []
        referenceTargets = [] 
        doubleNames = [] 
        doubleVals = [] 
        intNames = [] 
        intVals = [] 
        boolNames = [] 
        boolVals = [] 
        dateNames = [] 
        dateVals = [] 
        stringNames = [] 
        stringVals = [] 

        for key, val in args.items():
            if isinstance(key, ReferenceVariable) and isinstance(val, PetrelObject):
                referenceVars.append(key._petrel_object_link)
                referenceTargets.append(val._petrel_object_link)
            elif isinstance(key, ReferenceVariable) and (isinstance(val, Template) or isinstance(val, DiscreteTemplate)):
                referenceVars.append(key._petrel_object_link)
                referenceTargets.append(val._petrel_object_link)
            elif isinstance(key, ReferenceVariable) and not isinstance(val, PetrelObject):
                raise ValueError("Reference variables must be paired with PetrelObjects")
            elif isinstance(key, str):
                if isinstance(val, float):
                    doubleNames.append(key)
                    doubleVals.append(val)
                if isinstance(val, int):
                    intNames.append(key)
                    intVals.append(val)
                if isinstance(val, bool):
                    boolNames.append(key)
                    boolVals.append(val)
                if isinstance(val, datetime.datetime):
                    dateNames.append(key)
                    dateVals.append(val)
                if isinstance(val, str):
                    stringNames.append(key)
                    stringVals.append(val)

        obj_dict, value_dict = self._workflow_object_link.RunSingle(
            referenceVars, 
            referenceTargets, 
            doubleNames, 
            doubleVals, 
            intNames, 
            intVals, 
            boolNames, 
            boolVals, 
            dateNames, 
            dateVals, 
            stringNames, 
            stringVals,
            return_strings,
            return_numerics,
            return_dates
        )

        results = {}
        for variable_ref, val in obj_dict.items():
            key = _pb_PetrelObjectGuid_to_pyobj(variable_ref)
            value = _pb_PetrelObjectGuid_to_pyobj(val)
            results[key] = value

        results.update(value_dict)

        return results # type: ignore

    def retrieve_history(self):
        print("History not available for this object type.")