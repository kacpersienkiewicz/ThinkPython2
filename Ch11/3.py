'''
Exercise 11.3. Memoize the Ackermann function from Exercise 6.2 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: https:
// thinkpython. com/ code/ ackermann_ memo. py .
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


known = {}

def ack_memo(m,n):
    if (m,n) in known:
        return known[m,n]
    elif m == 0:
        result = n + 1
        known[0,n] = result
        return result
    elif m > 0 and n == 0:
        result = ack_memo(m-1,1)
        known[m,n] = result
        return result
    elif m > 0 and n > 0:
        result = ack_memo(m-1, ack_memo(m, n-1))
        known[m,n] = result
        return result
    else:
        print("Both m and n must be integers greater to or equal to 0.")


print(f"Memo: {str(ack_memo(3, 4))}, standard: {str(ack(3,4))}")
print(f"Memo: {str(ack_memo(3, 6))}, standard: {str(ack(3,6))}")
print(known)