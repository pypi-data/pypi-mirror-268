import time

from pydantic import BaseModel
from pydantic import Field
from pydantic import PrivateAttr

from amsdal_utils.classes.transaction_manager import TransactinInfoManager
from amsdal_utils.models.data_models.address import Address
from amsdal_utils.models.data_models.reference import Reference
from amsdal_utils.utils.lazy_object import LazyInstanceObject


class Transaction(BaseModel):
    _changes: LazyInstanceObject['Transaction', list[Reference]] = PrivateAttr(
        LazyInstanceObject(lambda transaction: TransactinInfoManager().get_changes(transaction))
    )
    address: Address
    """The address of the transcation."""

    label: str
    """The label of the transaction. Can be a name of transaction or a function name."""

    tags: list[str] = Field(default_factory=list)
    """The tags of the transaction. Can be used to group transactions."""

    started_at: float = Field(default_factory=lambda: round(time.time() * 1000))
    """The timestamp when the transaction was started"""

    ended_at: float = Field(default_factory=lambda: round(time.time() * 1000))
    """The timestamp when the transaction was ended"""

    @property
    def changes(self) -> list[Reference]:
        """
        The list of References that the given transaction has created.

        :return: The list of References that the given transaction has created.
        :rtype: list[Reference]
        """
        return self._changes.value(self)
