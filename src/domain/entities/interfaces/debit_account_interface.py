"""This module contains the interface for the Debit
"""

from abc import abstractmethod
from src.domain.entities.interfaces.transactions_interface import TransactionsInterface

class DebitAccountInterface(TransactionsInterface):
    
    @abstractmethod
    def saving(amount):
        pass