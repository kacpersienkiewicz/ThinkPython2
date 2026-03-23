'''
Exercise 10.10. To check whether a word is in the word list, you could use the in operator, but it
would be slow because it searches through the words in order.
Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary
(the book, not the data structure). You start in the middle and check to see whether the word you are
looking for comes before the word in the middle of the list. If so, you search the first half of the list
the same way. Otherwise you search the second half.
Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it's not there.
Write a function called in_bisect that takes a sorted list and a target value and returns True if
the word is in the list and False if it's not.
Or you could read the documentation of the bisect module and use that! Solution: https:
// thinkpython. com/ code/ inlist. py .
'''

fin = open('Ch9\\words.txt')

def word_build_append(file):
    word_list =[]
    for line in file:
        word = line.strip() # Not stripping whitespace seems to prevent words from being matched properly
        word_list.append(word)
    return word_list

def in_bisect(sorted_list, target_word):
    if len(sorted_list) == 0:
        return False
    i = len(sorted_list) // 2

    if sorted_list[i] == target_word:
        return True
    elif sorted_list[i] > target_word:
        return in_bisect(sorted_list[:i], target_word)
    elif sorted_list[i] < target_word:
        return in_bisect(sorted_list[i+1:], target_word)
    else:
        print("LogicError")

word_list = word_build_append(fin)
print(in_bisect(word_list,'aardvark'))
print(in_bisect(word_list,'fakeword'))