"""This module contains the interface for the User
"""
from abc import ABC,abstractmethod

class UserInterface(ABC):
    
    @abstractmethod
    def register():
        pass
        
    @abstractmethod
    def statusRegister():
        pass