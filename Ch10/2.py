'''
Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu-
lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''
def cumsum(numbers: list):
    cumsum_object = []
    i = 1
    while i < len(numbers) + 1:
        cumsum_object.append(sum(numbers[:i]))
        i += 1
    return cumsum_object

t = [1, 2, 3]
print(cumsum(t))