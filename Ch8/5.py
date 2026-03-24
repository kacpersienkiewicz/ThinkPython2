'''
Exercise 8.5. A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.
Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, and
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution:
https: // thinkpython. com/ code/ rotate. py .
'''



def rotate_word(word, rotation_value):
    '''
    Notes: % 26 is because the rotation only makes sense with values from 0 - 26 (length of the English alphabet). This allows for large values like the 33 found in the last test case to work properly.
    The conditionals like value >/< ord(ZzAa) is there to keep the values within the bounds of a-z or A-Z.

    There may be some additional optimizations, but it seems good as is.
    '''
    rotation_value = rotation_value % 26
    rotated_word = ''
    for letter in word:
        value = ord(letter) + rotation_value
        if letter.isupper():
            if value > ord('Z'):
                value -= 26
            elif value < ord('A'):
                value += 26
        if letter.islower():
            if value > ord('z'):
                value -= 26
            elif value < ord('a'):
                value += 26
        
        rotated_word += chr(value)
    return rotated_word

print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('IBM', -1))
print(rotate_word('cheer', 33))

#ROT13 Ciphers, from Wikipedia and elsewhere
print(rotate_word('aha nun', 13))
print(rotate_word('balk onyx', 13))
print(rotate_word('barf ones', 13))
print(rotate_word('bin ova', 13))
print(rotate_word('envy rail', 13))
print(rotate_word('errs reef', 13))
print(rotate_word('fur she', 13))
print(rotate_word('gnat tang', 13))
print(rotate_word('clerk pyrex', 13))
print(rotate_word('PNG cat', 13))
print(rotate_word('furby sheof', 13))
print(rotate_word('what Jung', 13))
print(rotate_word('ant nag', 13))
print(rotate_word('bar one', 13))
print(rotate_word('be or', 13))
print(rotate_word('ebbs roof', 13))
print(rotate_word('er re', 13))
print(rotate_word('flap sync', 13))
print(rotate_word('gel try', 13))
print(rotate_word('irk vex', 13))
print(rotate_word('purely cheryl', 13))
print(rotate_word('SHA fun', 13))
print(rotate_word('terra green', 13))
print(rotate_word('URL hey', 13))
print(rotate_word('Ares Nerf', 13))
