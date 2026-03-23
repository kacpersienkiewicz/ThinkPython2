'''
Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn't use any of the forbidden letters.
Write a program that prompts the user to enter a string of forbidden letters and then prints the
number of words that don't contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
'''

def avoids(word, forbidden_letters):
    for letter in word:
        if letter in forbidden_letters:
            return False
        else:
            continue
    return True

forbidden_letters = input("Enter your forbidden letters of choice.\n")

fin = open('Ch9\words.txt')
word_count = 0
for line in fin:
    if avoids(line, forbidden_letters):
        word_count += 1
    else:
        continue

print(word_count)