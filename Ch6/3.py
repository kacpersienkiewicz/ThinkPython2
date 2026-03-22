'''
Exercise 6.3. A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome.
The following are functions that take a string argument and return the first, last, and middle letters:
def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]
We’ll see how they work in Chapter 8.
1. Type these functions into a file named palindrome.py and test them out. What happens if
you call middle with a string with two letters? One letter? What about the empty string,
which is written '' and contains no letters?
2. Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise. Remember that you can use the built-in function len
to check the length of a string.
Solution: https: // thinkpython. com/ code/ palindrome_ soln. py .
'''

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]
def is_palindrome(word):
    # This is a kinda recursive strategy, with a sort of base case for 1 or 0 word length.
    if len(word) <= 1:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False

print(is_palindrome(123))