'''
Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
to frequency. For example, for this histogram:
>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
'''
# Ex 12.1's most_frequent function was reworked to fit this
# Ex 11.1's file_to_dict function was also used.
import string
import random

txt = open('Ch13\\pg1.txt', 'r', encoding="utf-8")

def random_from_histogram(hist: dict):
    word_list = []
    for key, value in hist.items():
        for i in range(value):
            word_list.append(key)
    return random.choice(word_list)

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

freq_tuple = []
for letter, freq in freq_dict.items():
        freq_tuple.append((freq, letter))
freq_tuple.sort(reverse=True)

random_choice = random_from_histogram(freq_dict)
print(random_choice)

