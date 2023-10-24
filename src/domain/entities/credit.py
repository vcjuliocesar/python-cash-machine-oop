"""This module has definition of the Credit entity
"""

from src.domain.entities.user import User
from src.domain.value_objects import INITIALIZE_CREDIT_BALANCE_AMOUNT,EMPTY_BALANCE,FEE,LIMIT_CREDIT
from src.domain.entities.interfaces.credit_account_interface import CreditAccountInterface

class Credit(CreditAccountInterface):
    
    def __init__(self,user:User) -> None:
        
         self.user = user

         self.init_balance = INITIALIZE_CREDIT_BALANCE_AMOUNT
    
    def balance(self):
        
        return self.init_balance
    
    def with_draw(self, amount):

        if amount == 0:

            raise Exception(f"Indica una cantidad mayor a {amount}")

        if amount > self.init_balance:

            raise Exception(f"La cantidad es mayor al saldo disponible")

        if self.init_balance == EMPTY_BALANCE:

            raise Exception("La cuenta esta vacia")
        
        
        amount += self.fee(amount)
        
        Credit.update_balance(amount - amount)
    
    @staticmethod
    def update_balance(self, new_balance):

        self.init_balance = new_balance
        
        
    def fee(self,amount):
        
        return amount * FEE
    
    def pay(self,amount):
        
        if amount >= LIMIT_CREDIT :
            
            raise Exception(f"La cantidad {amount} supera el limite de credito")
        
        if LIMIT_CREDIT == 0:
            
            raise Exception(f"Excedite el limite de credito de tu cuenta")
        
        Credit.update_balance(self.balance + amount)