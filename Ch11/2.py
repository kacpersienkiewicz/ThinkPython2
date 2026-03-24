'''
Exercise 11.2. Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict. Solution: https://thinkpython.com/code/invert_dict.py .
'''

def invert_dict(d):
    inverse = {}
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse
