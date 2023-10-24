import unittest

from src.domain.entities.user import User

class TestUser(unittest.TestCase):
    
    def test_it_can_register_a_user(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        self.assertTrue(user.statusRegister())
    
    def test_it_validates_status_when_register_us_true(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        user.register()
        
        self.assertTrue(user.statusRegister())
        
    def test_it_validates_status_when_register_us_false(self) -> None:
        
        user = User(name='Jhon Doe',email='jhon.doe@gmail.com')
        
        self.assertFalse(user.statusRegister())
    
if __name__ == "__main__":
    
    unittest.main()