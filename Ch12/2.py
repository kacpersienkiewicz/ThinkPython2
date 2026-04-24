'''
Exercise 12.2. More anagrams!
1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
words that are anagrams.
Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']
Hint: you might want to build a dictionary that maps from a collection of letters to a list
of words that can be spelled with those letters. The question is, how can you represent the
collection of letters in a way that can be used as a key?
2. Modify the previous program so that it prints the longest list of anagrams first, followed by
the second longest, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
the board, to form an eight-letter word. What collection of 8 letters forms the most possible
bingos?
Solution: https://thinkpython.com/code/anagram_sets.py .
'''

fin = open('Ch9\\words.txt')

def anagram_sets(fin):
    anagram_dict ={}
    
    for line in fin:
        word = line.strip().lower()
        w = list(word)
        w.sort()
        letters = ''.join(w)
        anagram_dict[letters] = anagram_dict.get(letters,[]) + [word]
    return anagram_dict

def anagram_sets_sorted(anagram_dict):
    anagram_dict_sorted = []
    for val in anagram_dict.values():
        if len(val) > 1:
            anagram_dict_sorted.append((len(val),val))
        else:
            continue
    anagram_dict_sorted.sort(reverse=True)
    return anagram_dict_sorted

def best_scrabble_bingo(anagram_dict_sorted):
    bingos = []
    for element in anagram_dict_sorted:
        if len(element[1][0]) == 8:
            bingos.append(element)
        else:
            continue
    bingos.sort(reverse=True) # Likely unnecessary becuase it was sorted before and it iterated over it in order
    return bingos[0][1]

anagrams = anagram_sets(fin)
for vals in anagrams.values():
    print(vals)

sorted_anagrams = anagram_sets_sorted(anagrams)
for vals in sorted_anagrams:
    print(vals[1])

best_bingo = best_scrabble_bingo(sorted_anagrams)
print("Best bingo: " , best_bingo)