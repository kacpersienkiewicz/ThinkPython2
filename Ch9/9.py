'''
Exercise 9.9. Here's another Car Talk Puzzler you can solve with a search (http: // www.
cartalk. com/ content/ puzzlers ):
“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she's 73, I'm 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we're lucky it would happen again in a few years, and
if we're really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”
Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
method zfill useful.
Solution: https: // thinkpython. com/ code/ cartalk3. py .
'''

def is_reversed(parent: str, child: str):
    if parent == child[::-1]:
        return True
    else:
        return False
    
def str_fill(age: int, n: int):
    # Makes sure the lengths of the parent and child's age are the same using zfill
    return str(age).zfill(n)

def check_palindrome_ages(parent: int, child: int):
    # parent = parent's age, child = child's age, both currently
    difference = parent - child

    child_age = 0

    while True:
        parent_age = child_age + difference
        if parent_age > 100: # basically, it is impossible for three digits to create a palindrome, unless I guess they had the child near 100.
            break
        if is_reversed(str_fill(parent_age, 2), str_fill(child_age, 2)):
            print(f"Palindrome at age {parent_age} for the parent, and at age {child_age} for the child.")
        child_age += 1

        
check_palindrome_ages(73, 37)
