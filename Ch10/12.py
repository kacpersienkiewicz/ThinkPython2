'''
Exercise 10.12. Two words “interlock” if taking alternating letters from each forms a new
word.
For example, “shoe” and “cold” interlock to form “schooled”.
Solution: https: //thinkpython. com/ code/ interlock. py . Credit: This exercise is inspired by an example at
http: // puzzlers. org .
1. Write a program that finds all pairs of words that interlock. Hint: don't enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
word, starting from the first, second or third?
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

def interlock(word_list, word):
    evens =word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)

def interlock_general(word_list, word, n):
    '''
    word_list: word list to check against the interlocked word
    word: interlocked word
    n: n-way interlock e.g. n=3 means three words interlock to create the word
    '''
    for i in range(n):
        interword = word[i::n]
        if not in_bisect(word_list, interword):
            return False
    return True

word_list = word_build_append(fin)

for word in word_list:
    if interlock(word_list, word):
        print(word, word[::2], word[1::2])

for word in word_list:
    if interlock_general(word_list, word, 3):
        print(word)