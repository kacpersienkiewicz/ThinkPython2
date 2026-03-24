'''
Exercise 11.6. Here's another Puzzler from Car Talk (http: // www. cartalk. com/ content/
puzzlers ):
This was sent in by a fellow named Dan O'Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove the
first letter, the remaining letters form a homophone of the original word, that is a word
that sounds exactly the same. Replace the first letter, that is, put it back and remove
the second letter and the result is yet another homophone of the original word. And the
question is, what's the word?
Now I'm going to give you an example that doesn't work. Let's look at the five-letter
word, 'wrack.' W-R-A-C-K, you know like to 'wrack with pain.' If I remove the first
letter, I am left with a four-letter word, 'R-A-C-K.' As in, 'Holy cow, did you see the
rack on that buck! It must have been a nine-pointer!' It's a perfect homophone. If you
put the 'w' back, and remove the 'r,' instead, you're left with the word, 'wack,' which is
a real word, it's just not a homophone of the other two words.
But there is, however, at least one word that Dan and we know of, which will yield two
homophones if you remove either of the first two letters to make two, new four-letter
words. The question is, what's the word?
You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.
To
check
whether
two
words
are
homophones,
you
can
use
the
CMU
Pronouncing
Dictionary.
You can download it from http: // www. speech. cs. cmu. edu/ cgi-bin/
cmudict
or from https: // thinkpython. com/ code/ c06d
and you can also down-
load https: // thinkpython. com/ code/ pronounce. py , which provides a function named
read_dictionary that reads the pronouncing dictionary and returns a Python dictionary that
maps from each word to a string that describes its primary pronunciation.


Write a program that lists all the words that solve the Puzzler. Solution: https: // thinkpython.
com/ code/ homophone. py .
'''

cmu_dict = open('Ch11\\cmudict-0.7b')

def dictionary_creation(fin):
    # Takes the cmu dict and creates key-value pairs for the word and its pronounciation
    pronounciation_dict = {}
    for line in fin:
        if line[0] == ';':
            continue
        split_line = line.split()
        word = split_line[0]
        pronounciation = split_line[1:]
        pronounciation_dict[word] = pronounciation
    return pronounciation_dict

pronounciation_dict = dictionary_creation(cmu_dict)

for word in pronounciation_dict:
    word2 = word[1:]
    word3 = word[0] + word[2:]
    if word2 in pronounciation_dict and word3 in pronounciation_dict:
        if pronounciation_dict[word] == pronounciation_dict[word2] == pronounciation_dict[word3]:
            print(f"{word}, {word2}, and {word3} are homophones.")