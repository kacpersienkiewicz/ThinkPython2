'''
Exercise 13.7. Write a program that uses this algorithm to choose a random word from the book.
Solution: https://thinkpython.com/code/analyze_book3.py .

This algorithm works, but it is not very efficient; each time you choose a random word, it
rebuilds the list, which is as big as the original book. An obvious improvement is to build
the list once and then make multiple selections, but the list is still big.
An alternative is:
1. Use keys to get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 10.2). The last item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10.10) to find the index where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.
'''
import string

#From Ex 10.10
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

def parse_book(txt):
    start_line = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_line = "*** END OF THE PROJECT GUTENBERG EBOOK"
    freq_dict = {}
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

    return freq_dict

def cumsum(numbers: list):
    cumsum_object = []
    i = 1
    while i < len(numbers) + 1:
        cumsum_object.append(sum(numbers[:i]))
        i += 1
    return cumsum_object