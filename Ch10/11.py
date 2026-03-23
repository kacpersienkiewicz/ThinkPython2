'''
Exercise 10.11. Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution: https: // thinkpython. com/ code/
reverse_ pair. py .
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

def find_reverse_pair(word_list, word):
    reversed_word = word[::-1]
    if in_bisect(word_list, reversed_word):
        print(f"The word {word} and its reverse pair, {reversed_word} appears in the word list.")

word_list = word_build_append(fin)

for word in word_list:
    find_reverse_pair(word_list, word)
