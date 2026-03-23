'''
Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car
Talk (http: // www. cartalk. com/ content/ puzzlers ):
Give me a word with three consecutive double letters. I'll give you a couple of words
that almost qualify, but don't. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the 'i' that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. If you could take out those i's it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
Write a program to find it. Solution: https: // thinkpython. com/ code/ cartalk1. py .
'''

def triple_double_letters(word):
    i = 0
    word = word.lower() # Weird issues may arise if lower and upper case letters are mixed.
    while i < len(word) - 1:
        if word[i] == word[i + 1] and len(word[i+2:]) >=4: # Split up because I think it helps performance, likely can just be done with several ands in one statement
            if word[i + 2]  == word[i + 3]:
                if word[i + 4]  == word[i + 5]:
                    return True
        i += 1
    return False

print(triple_double_letters('aabbcc'))
print(triple_double_letters('Mississippi'))
print(triple_double_letters('committee'))