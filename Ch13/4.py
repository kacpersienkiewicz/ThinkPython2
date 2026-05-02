'''
Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and then print all
the words in the book that are not in the word list. How many of them are typos? How many of
them are common words that should be in the word list, and how many of them are really obscure?
'''

# Ex 12.1's most_frequent function was reworked to fit this
# Ex 11.1's file_to_dict function was also used.
import string

start_line = "*** START OF THE PROJECT GUTENBERG EBOOK" # This is the real start of every Project Gutenberg books
end_line = "START: FULL LICENSE" # This is the start of the license, and thus the end of the book

txt = open('Ch13\\pg1.txt', 'r', encoding="utf-8")
freq_dict = {}
start_of_text = False
book_name = ''

fin = open('Ch9\\words.txt')

def file_to_dict(file):
    file_dict = {}
    for line in file:
        word = line.strip()
        file_dict[word] = word
    return file_dict

for line in txt:
    if line.startswith(end_line) and start_of_text == True:
        start_of_text = False


    if start_of_text:
        curr_line = line.lower().strip()
        for char in string.punctuation:
            curr_line = curr_line.replace(char, '')
        curr_line = curr_line.split()
        for word in curr_line:
            freq_dict[word] = freq_dict.get(word, 0) + 1

    if line.startswith(start_line) and start_of_text == False:
        start_of_text = True
        book_name = line[41:-4] # goes around the bounds of the book name in the same line: *** START OF THE PROJECT GUTENBERG EBOOK BOOK NAME *** - > BOOK NAME


freq_tuple = []
for letter, freq in freq_dict.items():
        freq_tuple.append((freq, letter))
freq_tuple.sort(reverse=True)
words = file_to_dict(fin)

nonshared_words = []
for word in freq_dict.keys():
    if word not in words:
        nonshared_words.append(word)
print(nonshared_words)