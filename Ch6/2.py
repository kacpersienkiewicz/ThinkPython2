'''
Exercise 6.2. The Ackermann function, A(m, n), is defined:

See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
that evaluates the Ackermann function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n? Solution: https: // thinkpython. com/ code/
ackermann. py .
'''

def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        print("Both m and n must be integers greater to or equal to 0.")

print(ack(3, 4))
# print(ack(250,300)) this reaches recursion depth