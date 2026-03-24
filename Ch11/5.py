'''
Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_word in Exercise 8.5).
Write a program that reads a wordlist and finds all the rotate pairs.
Solution: https: //
thinkpython. com/ code/ rotate_ pairs. py .
'''

def file_to_dict(file):
    file_dict = {}
    for line in file:
        word = line.strip()
        file_dict[word] = word
    return file_dict


def rotate_word(word, rotation_value):
    rotation_value = rotation_value % 26
    rotated_word = ''
    for letter in word:
        value = ord(letter) + rotation_value
        if letter.isupper():
            if value > ord('Z'):
                value -= 26
            elif value < ord('A'):
                value += 26
        if letter.islower():
            if value > ord('z'):
                value -= 26
            elif value < ord('a'):
                value += 26
        
        rotated_word += chr(value)
    return rotated_word

def rotate_pairs(word, word_dict):
    for i in range(1,25): 
        rotated_word = rotate_word(word, i)
        if rotated_word in word_dict:
            print(f"{word} rotated by {i} is {rotated_word}")

fin = open('Ch9\\words.txt')
word_dict = file_to_dict(fin)

for word in word_dict:
    rotate_pairs(word, word_dict)
