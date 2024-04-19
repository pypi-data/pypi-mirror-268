from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

from amsdal_utils.errors import AmsdalInitiationError
from amsdal_utils.models.data_models.reference import Reference
from amsdal_utils.utils.singleton import Singleton

if TYPE_CHECKING:
    from amsdal_utils.models.data_models.metadata import Metadata


class MetadataInfoQueryBase(ABC):
    @classmethod
    @abstractmethod
    def get_reference_to(cls, metadata: 'Metadata') -> list['Reference']:
        """
        Get the list of References that the given metadata is referencing to.


        :param metadata: The metadata
        :type metadata: Metadata
        :return: The list of References that the given metadata is referencing to.
        :rtype: list[Reference]
        """

    @classmethod
    @abstractmethod
    def get_referenced_by(cls, metadata: 'Metadata') -> list['Reference']:
        """
        Get the list of References that have reference to the given metadata.

        :param metadata: The metadata
        :type metadata: Metadata
        :return: The list of References that have reference to the given metadata.
        :rtype: list[Reference]
        """


class MetadataInfoManager(metaclass=Singleton):
    def __init__(self) -> None:
        self._metadata_info_query: type[MetadataInfoQueryBase] | None = None

    def register_metadata_info_query(self, metadata_info_query: type[MetadataInfoQueryBase]) -> None:
        self._metadata_info_query = metadata_info_query

    def get_metadata_info_query(self) -> type[MetadataInfoQueryBase]:
        if self._metadata_info_query is None:
            msg = 'MetadataInfoQuery is not registered.'
            raise AmsdalInitiationError(msg)

        return self._metadata_info_query

    def get_reference_to(self, metadata: 'Metadata') -> list['Reference']:
        return self.get_metadata_info_query().get_reference_to(metadata)

    def get_referenced_by(self, metadata: 'Metadata') -> list['Reference']:
        return self.get_metadata_info_query().get_referenced_by(metadata)
