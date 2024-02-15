def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)