import unittest

SpecialSym =['$', '@', '#', '%']

def is_valid_password(password):
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(char in SpecialSym for char in password):
            return False
        return True

def is_valid_long_password(password):
        if len(password) < 16:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.islower() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(char in SpecialSym for char in password):
            return False
        return True
    

class TestPasswordValidation(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_valid_password('P@ssw0rd')) # Valid everything 

    def test_password_too_short(self):
        self.assertFalse(is_valid_password('P@s1')) # Not long enough

    def test_password_missing_uppercase(self):
        self.assertFalse(is_valid_password('p@ssw0rd')) # No uppercase

    def test_password_missing_lowercase(self):
        self.assertFalse(is_valid_password('P@SSW0RD')) # No lowercase 

    def test_password_missing_number(self):
        self.assertFalse(is_valid_password('P@ssword')) # No number 

    def test_password_missing_special(self):
        self.assertFalse(is_valid_password('Passw0rd')) # No special 

    def test_password_great_password_short(self):
        self.assertFalse(is_valid_long_password('P@ssw0rd')) # Too short for great password 

    def test_password_great_password_long(self):
        self.assertTrue(is_valid_long_password('P@ssw0rdsuperlong123456789')) # Valid great password



if __name__ == '__main__':
    unittest.main()
