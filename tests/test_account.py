import unittest
from src.domain.entities.user import User
from src.domain.entities.account import Account

class TestAccount(unittest.TestCase):
    
    def test_it_return_an_exception_if_user_is_not_register(self) -> None :
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        with self.assertRaises(Exception):
            
            Account(user)
            
            
            
if __name__ == "__main__" :
    
    unittest.main()
            
        
        
        