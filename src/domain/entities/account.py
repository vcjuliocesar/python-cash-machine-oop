"""_summary_
"""
from src.domain.entities.user import User
from src.domain.entities.debit import Debit
from src.domain.entities.credit import Credit

class Account:
    
    def __init__(self,user:User) -> None:
        
        if not user.statusRegister() :
            
            raise Exception(f"El usuario {user.name} no esta registrado")
        
        self.debit:Debit = Debit
        self.credit:Credit = Credit