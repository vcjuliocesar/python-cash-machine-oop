from src.domain.entities.user import User
from src.domain.entities.account import Account
from src.domain.services.atm import Atm

if __name__ == "__main__":

    try:
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        user.register()
    
        print(f"user: {user.userInfo()}")
    
    except Exception as e:
    
        print(f"An exeption occurred: {str(e)}")