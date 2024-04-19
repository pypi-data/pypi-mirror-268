from abc import abstractmethod

from pydantic import BaseModel

from amsdal_utils.models.data_models.metadata import Metadata
from amsdal_utils.query.mixin import QueryableMixin
from amsdal_utils.query.utils import Q


class ModelBase(QueryableMixin, BaseModel):  # pragma: no cover
    @abstractmethod
    def get_metadata(self) -> Metadata: ...

    def to_query(self, prefix: str = '', *, force_frozen: bool = False) -> Q:
        return self.get_metadata().to_query(prefix, force_frozen=force_frozen)
