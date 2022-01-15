import bcrypt
from user import User

person1 = User('John', 'Max', 'johnmax@hotmail.com', 'Password123!', None)
person2 = User('Sarah', 'Michael', 'sarahM@hotmail.com', 'Pass5738!', None)

def test_1_is_correct_password():
    """
    
    Given the password: 'Password123!'
    WHEN the string 'Pass5738!' is passed to the is_correct_password function
    THEN the result should return false
    """
    entered_password = 'Pass5738!'
    result = person1.is_correct_password(entered_password)
    assert result == False

def test_2_is_correct_password():
    """
    Given the password: 'Pass5738!'
    WHEN the string 'Pass5738!' is passed to the is_correct_password function
    THEN the result should return True
    """   
    entered_password = 'Pass5738!'
    result2 = person2.is_correct_password(entered_password)
    assert result2 == True