import unittest
from src.domain.entities.user import User
from src.domain.entities.debit import Debit


class TestDebitAccount(unittest.TestCase):
    
    
    def test_it_returns_an_exception_if_amount_is_zero(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        account = Debit()
        
        with self.assertRaises(Exception):
            
            account.with_draw(0)
    
    def test_it_returns_debit_amount_balance(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        account = Debit()
        
        self.assertEqual(10500,account.balance())
        
if __name__ == "__main__":
    
    unittest.main()