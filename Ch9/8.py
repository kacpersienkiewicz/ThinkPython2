'''
Exercise 9.8. Here's another Car Talk Puzzler (http: // www. cartalk. com/ content/
puzzlers ):
“I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I'd see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”
Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements. Solution: https: // thinkpython. com/ code/ cartalk2. py .
'''

def is_palindrome(word):
    # Reusing a previously created function.
    if word == word[::-1]:
        return True
    else:
        return False
    
def test_odometer():
    i = 100000
    while i < 1000000:
        if i % 10000:
            print(f"On mile number {i}")
        if is_palindrome(str(i)[2:]):
            if is_palindrome(str(i + 1)[1:]):
                if is_palindrome(str(i + 2)[1:5]):
                    if is_palindrome((str(i + 3))):
                        print(i)
    i += 1

test_odometer()

'''
Answers:
198888
'''