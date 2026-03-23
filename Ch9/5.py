'''
Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once. How many words are
there that use all the vowels aeiou? How about aeiouy?
'''

def uses_all(word, required_letters):
    used_required_letters = ''
    for letter in word:
        if letter in required_letters:
            if letter not in used_required_letters:
                used_required_letters += letter
            else:
                continue
    for letter in required_letters:
        if letter in used_required_letters:
            continue
        else:
            return False
    return True

print(uses_all('godly', 'dog'))
print(uses_all('because', 'accce'))
print(uses_all('zorro', 'five'))