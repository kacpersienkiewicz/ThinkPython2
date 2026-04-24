'''
Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don't test all pairs of words, and don't test all possible
swaps. Solution: https://thinkpython.com/code/metathesis.py . Credit: This exercise
is inspired by an example at http://puzzlers.org .
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

def check_metathesis_pair(word1, word2):
    count = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            count += 1
        else:
            continue
    
    if count == 2:
        return True
    else:
        return False

def print_meta_metathesis_pairs(anagram_dict):
    for word in anagram_dict.values():
        for i in range(len(word)):
            str_word1 = str(word[i])
            for j in range(len(word)):
                str_word2 = str(word[j])
                if i < j: # prevents duplicate entries
                    continue
                else:
                    if check_metathesis_pair(str_word1,str_word2):
                        print(str_word1 + ' ' + str_word2)
                    else:
                        continue
    return

anagrams = anagram_sets(fin)
print_meta_metathesis_pairs(anagrams)