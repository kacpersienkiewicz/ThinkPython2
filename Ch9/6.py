'''
Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?
'''
def is_abecedarian(word):
    i = 0
    word = word.lower() # some strange things may happen if lower and upper case are mixed since 'a' > 'A' is True, for example. Without this line "is_abecedarian('aBc')" is False, though by intuition it is True.
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i += 1 
    return True

print(is_abecedarian('abc'))
print(is_abecedarian('aBc'))
print(is_abecedarian('cba'))
print(is_abecedarian('abbc'))