# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



from cegalprizm.pythontool import PetrelObject, _utils
from cegalprizm.pythontool.template import Template, DiscreteTemplate
from cegalprizm.pythontool.borehole import Well
import typing
from typing import List
import pandas as pd


if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.checkshot_grpc import CheckShotGrpc

class CheckShot(PetrelObject):
    def __init__(self, petrel_object_link: "CheckShotGrpc"):
        super(CheckShot, self).__init__(petrel_object_link)
        self._petrel_object_link = petrel_object_link

    def __str__(self) -> str:
        return "CheckShot(petrel_name=\"{0}\")".format(self.petrel_name)
    
    def __repr__(self) -> str:
        return str(self)
    
    def as_dataframe(self,
                     include_unconnected_checkshots: bool = True,
                     include_user_defined_properties: bool = True,
                     wells_filter: List[Well] = None) -> pd.DataFrame:
        """Gets a dataframe with information about the CheckShotSamples for this CheckShot.

        **Example**:

        Get a dataframe with information about all CheckShotSamples in the CheckShot.

        .. code-block:: python

            checkshot = petrel_connection.checkshots["Input/Path/To/CheckShot"]
            df = checkshot.as_dataframe()

        **Example**:

        Get a dataframe with information about CheckShotSamples for only those wells that exist in the current Petrel project.

        .. code-block:: python

            checkshot = petrel_connection.checkshots["Input/Path/To/CheckShot"]
            df = checkshot.as_dataframe(include_unconnected_checkshots=False)

        **Example**:

        Get a dataframe with information about CheckShotSamples for two specific wells, excluding user-defined properties.

        .. code-block:: python
            well1 = petrel_connection.wells["Input/Path/To/Well1"]
            well2 = petrel_connection.wells["Input/Path/To/Well2"]
            checkshot = petrel_connection.checkshots["Input/Path/To/CheckShot"]
            df = checkshot.as_dataframe(include_user_defined_properties=False, wells_filter=[well1, well2])

        Args:
            include_unconnected_checkshots (bool, optional): Whether to include CheckShotSamples that are not connected to a well. Defaults to True.
            include_user_defined_properties (bool, optional): Whether to include user-defined properties in the dataframe. Defaults to True.
            wells_filter (List[Well], optional): Include CheckShotSamples from only specific wells by supplying a list of :class:`Well`. Defaults to None, which returns data for all wells.

        Returns:
            DataFrame: A dataframe with information about the CheckShotSamples for this CheckShot.
        """
        wells = _utils.get_wells(wells_filter=wells_filter)
        df = self._petrel_object_link.GetCheckShotDataFrame(include_unconnected_checkshots, wells, include_user_defined_properties)
        return df
