'''
Exercise 12.1. Write a function called most_frequent that takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies .
Solution: https://thinkpython.com/code/most_frequent.py .
'''

def most_frequent(text:str):
    text = text.lower()
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    freq_tuple = []
    for letter, freq in freq_dict.items():
        freq_tuple.append((freq, letter))
    
    freq_tuple.sort(reverse=True)

    for x in freq_tuple:
        print(x[1])

    return

wikitext = """Letter frequency is the number of times letters of the alphabet appear on average in written language. Letter frequency analysis dates back
to the Arab mathematician Al-Kindi (c. AD 801–873), who formally developed the method to break ciphers. Letter frequency analysis gained importance in
Europe with the development of movable type in AD 1450, wherein one must estimate the amount of type required for each letterform. Linguists use letter
frequency analysis as a rudimentary technique for language identification, where it is particularly effective as an indication of whether an unknown
writing system is alphabetic, syllabic, or logographic. The use of letter frequencies and frequency analysis plays a fundamental role in cryptograms
and several word puzzle games, including hangman, Scrabble, Wordle and the television game show Wheel of Fortune. One of the earliest descriptions in
classical literature of applying the knowledge of English letter frequency to solving a cryptogram is found in Edgar Allan Poe's famous story "The Gold-Bug",
where the method is successfully applied to decipher a message giving the location of a treasure hidden by Captain Kidd. Herbert S. Zim, in his classic
introductory cryptography text Codes and Secret Writing, gives the English letter frequency sequence as "ETAON RISHD LFCMU GYPWB VKJXZQ",
the most common letter pairs as "TH HE AN RE ER IN ON AT ND ST ES EN OF TE ED OR TI HI AS TO", and the most common doubled letters as
"LL EE SS OO TT FF RR NN PP CC". Different ways of counting can produce somewhat different orders. Letter frequencies also have a strong effect on the
design of some keyboard layouts. The most frequent letters are placed on the home row of the Blickensderfer typewriter, the Dvorak keyboard layout,
Colemak and other optimized layouts."""

lorem_ipsum = """Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi
pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl
malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos."""

most_frequent(wikitext)
most_frequent(lorem_ipsum)