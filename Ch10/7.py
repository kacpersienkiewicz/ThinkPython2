'''
Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
'''

def has_duplicates(item):
    sorted_item = sorted(item)
    for i in range(len(sorted_item) - 1):
        if sorted_item[i] == sorted_item[i + 1]:
            return True
    return False

print(has_duplicates([1,2,1,4]))
print(has_duplicates(['a','A','b','A']))
print(has_duplicates([5,9,2,3]))