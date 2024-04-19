from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

from amsdal_utils.errors import AmsdalInitiationError
from amsdal_utils.models.data_models.reference import Reference
from amsdal_utils.utils.singleton import Singleton

if TYPE_CHECKING:
    from amsdal_utils.models.data_models.transaction import Transaction


class TransactionInfoQueryBase(ABC):
    @classmethod
    @abstractmethod
    def get_changes(cls, transaction: 'Transaction') -> list['Reference']:
        """
        Get the list of References that the given transaction has created.

        :param transaction: The transaction
        :type transaction: Transaction
        :return: The list of References that the given transaction has created.
        :rtype: list[Reference]
        """


class TransactinInfoManager(metaclass=Singleton):
    def __init__(self) -> None:
        self._transaction_info_query: type[TransactionInfoQueryBase] | None = None

    def register_transaction_info_query(self, transaction_info_query: type[TransactionInfoQueryBase]) -> None:
        self._transaction_info_query = transaction_info_query

    def get_transaction_info_query(self) -> type[TransactionInfoQueryBase]:
        if self._transaction_info_query is None:
            msg = 'TransactionInfoQuery is not registered.'
            raise AmsdalInitiationError(msg)

        return self._transaction_info_query

    def get_changes(self, transaction: 'Transaction') -> list['Reference']:
        return self.get_transaction_info_query().get_changes(transaction)
