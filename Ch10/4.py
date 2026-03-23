'''
Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''

def chop(item):
    del(item[0])
    del(item[-1])
    
t = [1, 2, 3, 4]
chop(t)
print(t)