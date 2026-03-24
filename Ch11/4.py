'''
Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates. Solution: https: //
thinkpython. com/ code/ has_ duplicates. py .
'''

def has_duplicates(item):
    sorted_item = sorted(item)
    for i in range(len(sorted_item) - 1):
        if sorted_item[i] == sorted_item[i + 1]:
            return True
    return False

def has_duplicates2(items):
    item_dict = {}
    for item in items:
        if item in item_dict:
            return True
        else:
            item_dict[item] = item
    return False

print(has_duplicates2([1,2,1,4]))
print(has_duplicates2(['a','A','b','A']))
print(has_duplicates2([5,9,2,3]))