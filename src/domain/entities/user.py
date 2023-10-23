""" This module has definition of the User entity
"""

from src.domain.value_objects import userId,_registered

from src.domain.entities.interfaces.user_interface import UserInterface

class User(UserInterface):
    
    def __init__(self,name:str,email:str) -> None:
        
        self.id:userId = userId
        
        self.name:str = name
        
        self.email:str = email
        
        self._registered = _registered
        
    def register(self) -> None:
        
        self._registered = True
        
    
    def statusRegister(self):
        
        return self._registered
    
    def userInfo(self):
        
        return f"Id: {self.id} name: {self.name} email: {self.email}" 