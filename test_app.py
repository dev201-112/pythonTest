from app import add, is_palindrome


def test_add_positive():
    assert add(2, 3) == 8

def test_add_negative():
    assert add(-1, 4) == 3

def test_palindrome_true():
    assert is_palindrome("Kayak")

def test_palindrome_false():
    assert not is_palindrome("Python")


