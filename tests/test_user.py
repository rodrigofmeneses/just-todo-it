from todo.models.user import User, UserRequest, UserResponse
from todo.security import get_password_hash, verify_password


def test_encode_password_hash():
    password = '1234'
    password_hashed = get_password_hash(password)
    assert password != password_hashed
    
def test_verify_password_with_correctly_data():
    password = '1234'
    password_hashed = get_password_hash(password)
    assert verify_password(password, password_hashed)
    
def test_verify_password_with_wrong_data():
    password = '1234'
    wrong_password = '5555'
    password_hashed = get_password_hash(password)
    assert not verify_password(wrong_password, password_hashed)

def test_two_passwords_has_different_hashs():
    password = '1234'
    assert get_password_hash(password) != get_password_hash(password)

def test_user_password_is_hashed():
    test_user = User(username='Test', password='1234')
    assert test_user.password != '1234'