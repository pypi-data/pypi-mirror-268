import time

from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

from amsdal_utils.classes.metadata_manager import MetadataInfoManager
from amsdal_utils.models.data_models.address import Address
from amsdal_utils.models.data_models.reference import Reference
from amsdal_utils.models.enums import SchemaTypes
from amsdal_utils.models.enums import Versions
from amsdal_utils.models.utils.reference_builders import build_reference
from amsdal_utils.query.mixin import QueryableMixin
from amsdal_utils.query.utils import Q
from amsdal_utils.utils.lazy_object import LazyInstanceObject


class Metadata(QueryableMixin, BaseModel):
    _is_frozen: bool = PrivateAttr(False)
    _reference_to: LazyInstanceObject['Metadata', list[Reference]] = PrivateAttr(
        LazyInstanceObject(lambda metadata: MetadataInfoManager().get_reference_to(metadata))
    )
    _referenced_by: LazyInstanceObject['Metadata', list[Reference]] = PrivateAttr(
        LazyInstanceObject(lambda metadata: MetadataInfoManager().get_referenced_by(metadata))
    )

    address: Address
    """The address of the object/record."""

    class_schema_reference: Reference
    """The reference to class schema"""

    class_meta_schema_reference: Reference | None = None
    """The reference to class meta schema"""

    transaction: Address | None = None
    """The address of the transaction that created the object/record"""

    class_schema_type: SchemaTypes = SchemaTypes.USER
    """The type of class schema"""

    is_deleted: bool = False
    """Flag to indicate if the object/record is deleted"""

    next_version: str | None = None
    """The next version of the object/record"""

    prior_version: str | None = None
    """The previous version of the object/record"""

    created_at: float = Field(default_factory=lambda: round(time.time() * 1000))
    """The timestamp when the object/record was created"""

    updated_at: float = Field(default_factory=lambda: round(time.time() * 1000))
    """The timestamp when the object/record was last updated"""

    @property
    def is_latest(self) -> bool:
        """
        Flag to indicate if the object/record is the latest version

        :rtype: bool
        """
        return self.next_version is None

    @property
    def reference(self) -> Reference:
        """
        Reference of the object/record. If the object/record is frozen or not latest, the version of object is pinned.
        Otehrwise, it will store the latest version.

        :rtype: Reference
        """
        reference_address = self.address

        if not self._is_frozen and self.is_latest:
            reference_address = self.address.model_copy(
                update={'object_version': Versions.LATEST},
            )

        return build_reference(
            resource=reference_address.resource,
            class_name=reference_address.class_name,
            object_id=reference_address.object_id,
            class_version=reference_address.class_version,
            object_version=reference_address.object_version,
        )

    @property
    def frozen_reference(self) -> Reference:
        """
        Reference of the object/record. Always return the pinned version of the object/record.

        :rtype: Reference
        """
        reference_address = self.address

        return build_reference(
            resource=reference_address.resource,
            class_name=reference_address.class_name,
            object_id=reference_address.object_id,
            class_version=reference_address.class_version,
            object_version=reference_address.object_version,
        )

    @property
    def reference_to(self) -> list[Reference]:
        """
        The list of references to other objects/records

        :rtype: list[Reference]
        """
        return self._reference_to.value(self)

    @property
    def referenced_by(self) -> list[Reference]:
        """
        The list of references from other objects/records

        :rtype: list[Reference]
        """
        return self._referenced_by.value(self)

    def to_query(self, prefix: str = '', *, force_frozen: bool = False) -> Q:
        reference = self.frozen_reference if force_frozen else self.reference

        return reference.to_query(prefix=prefix)
