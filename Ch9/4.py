'''
Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list. Can you make a sentence using only
the letters acefhlo? Other than “Hoe alfalfa”?
'''

def uses_only(word, allowed_letters):
    for letter in word:
        if letter not in allowed_letters:
            return False
        else:
            continue
    return True

allowed_letters = input("Enter your sacred letters of choice.\n")

test_word = input("Enter your word of choice.\n")

print(uses_only(test_word, allowed_letters))