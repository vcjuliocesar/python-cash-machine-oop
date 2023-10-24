import unittest
from src.domain.entities.user import User
from src.domain.entities.credit import Credit


class TestCreditAccount(unittest.TestCase):
    
    
    def test_it_returns_an_exception_if_amount_is_zero(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        account = Credit(user)
        
        with self.assertRaises(Exception):
            
            account.with_draw(0)
    
    def test_it_returns_credit_amount_balance(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        account = Credit(user)
        
        self.assertEqual(500,account.balance())
        
if __name__ == "__main__":
    
    unittest.main()