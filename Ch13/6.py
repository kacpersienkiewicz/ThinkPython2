'''
Exercise 13.6. Python provides a data structure called set that provides many common set
operations.
You can read about them in Section 19.5, or read the documentation at http://docs.python.org/3/library/stdtypes.html#types-set .
Write a program that uses set subtraction to find words in the book that are not in the word list.
Solution: https: //thinkpython.com/code/analyze_book2.py .
'''
# Ex 12.1's most_frequent function was reworked to fit this
# Ex 11.1's file_to_dict function was also used.
import string


txt = open('Ch13\\pg1.txt', 'r', encoding="utf-8")
fin = open('Ch9\\words.txt')

def file_to_dict(file):
    file_dict = {}
    for line in file:
        word = line.strip()
        file_dict[word] = word
    return file_dict

def parse_book(txt):
    start_line = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_line = "*** END OF THE PROJECT GUTENBERG EBOOK"
    freq_dict = {}
    book_name = ''
    start_of_text = False

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

    return book_name, freq_dict

book_name, freq_dict = parse_book(txt)
words = file_to_dict(fin)

set_subtract = set(freq_dict) - set(words)
print(set_subtract)