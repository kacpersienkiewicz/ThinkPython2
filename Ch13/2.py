'''
Go to Project Gutenberg (http: // gutenberg. org ) and download your favorite
out-of-copyright book in plain text format.
Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.
Then modify the program to count the total number of words in the book, and the number of times
each word is used.
Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?
'''
# Ex 12.1's most_frequent function was reworked to fit this
import string

start_line = "*** START OF THE PROJECT GUTENBERG EBOOK" # This is the real start of every Project Gutenberg books
end_line = "START: FULL LICENSE" # This is the start of the license, and thus the end of the book

txt = open('Ch13\\pg1.txt', 'r', encoding="utf-8")
freq_dict = {}
start_of_text = False
book_name = ''

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
print(f"{book_name} uses {len(freq_tuple)} unique words.")
print(freq_tuple)