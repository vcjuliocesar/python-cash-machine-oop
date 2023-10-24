"""This module contains the interface for all transactions
"""

from abc import ABC,abstractmethod

class TransactionsInterface(ABC):
    
    @abstractmethod
    def balance():
        pass
    
    @abstractmethod
    def with_draw(amount):
        pass
    
    @staticmethod
    @abstractmethod
    def update_balance(balance):
        pass