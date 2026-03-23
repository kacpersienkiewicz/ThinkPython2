'''
Exercise 10.9. Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?

Solution: https: // thinkpython. com/ code/ wordlist. py .

Commnetary: Concatenation took less time than appending,
to the point that seems to have taken no time at all according to the time method.
This is likely incorrect since concatentation makes a new object, and appending does not.

'''
import time

fin = open('Ch9\\words.txt')

def word_build_append(file):
    start = time.time()
    word_list =[]
    for line in file:
        word_list.append(line)
    end = time.time()
    return word_list, end - start

def word_build_idiom(file):
    start = time.time()
    word_list =[]
    for line in file:
        word_list += line
    end = time.time()
    return word_list, end - start

word_list1, time1 = word_build_append(fin)
word_list2, time2 = word_build_idiom(fin)

print(f"Append took {time1} seconds, and the concatenation method took {time2} seconds.")