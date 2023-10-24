from src.domain.entities.debit import Debit
from src.domain.entities.credit import Credit

class Atm:
    
    def __init__(self,account:Debit | Credit) -> None:
        
        self.account = account
        
    def balance(self) :
        
        try:
            
            return self.account.balance()
        
        except Exception as e:
            
            print(f"An exeption occurred: {str(e)}")
            
    def with_draw(self,amount) :
        
        try:
            
            return self.account.with_draw(amount)
        
        except Exception as e:
            
             print(f"An exeption occurred: {str(e)}")
             
    def saving(self,amount) :
        
        try:
            
            if isinstance(self.account,Credit):
                
                raise Exception("No se puede ahorrar en una cuenyta de credito") 
            
            return self.account.saving(amount)
        
        except Exception as e:
            
            print(f"An exeption occurred: {str(e)}")
            
    def pay(self,amount) :
        
        try:
            
            return self.account.pay(amount) 
        
        except Exception as e:
            
            print(f"An exeption occurred: {str(e)}")