# Copyright 2024 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import typing
from cegalprizm.pythontool import PetrelObject
if typing.TYPE_CHECKING:
    from cegalprizm.pythontool.grpc.borehole_collection_grpc import BoreholeCollectionGrpc

class WellFolder(PetrelObject):
    """A class holding information about a well folder (BoreholeCollection)."""

    def __init__(self, petrel_object_link: "BoreholeCollectionGrpc"):
        super(WellFolder, self).__init__(petrel_object_link)
        self._borehole_collection_object_link = petrel_object_link
    
    def __str__(self) -> str:
        """A readable representation"""
        return 'WellFolder(petrel_name="{0}")'.format(self.petrel_name)