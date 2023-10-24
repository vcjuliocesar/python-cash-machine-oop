"""This module contains the interface for the Credit
"""

from abc import abstractmethod
from src.domain.entities.interfaces.transactions_interface import TransactionsInterface

class CreditAccountInterface(TransactionsInterface):
    
    @abstractmethod
    def fee(amout):
        pass
    
    def pay(amout):
        pass