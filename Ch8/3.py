'''
Exercise 8.3. A string slice can take a third index that specifies the “step size”; that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.
'''

def is_palindrome(word):
    if str(word) == str(word)[::-1]:
        return True
    else:
        return False

print(is_palindrome('popo'))
print(is_palindrome(123))
print(is_palindrome(1221))
print(is_palindrome('abba'))
print(is_palindrome('abab'))
print(is_palindrome('grarg'))
print(is_palindrome('super'))