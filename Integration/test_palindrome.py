import palindrome

def test_is_palindrome():
    assert palindrome.is_palindrome("radar") == True
    assert palindrome.is_palindrome("hello") == False
    assert palindrome.is_palindrome("level") == True

def test_is_palindrome():
    assert palindrome.is_palindrome("radar") == True
    assert palindrome.is_palindrome("hello") == False
    assert palindrome.is_palindrome("level") == False



def test_factorial():
    assert palindrome.factorial(5) == 120
    assert palindrome.factorial(3) == 6
    assert palindrome.factorial(0) == 1