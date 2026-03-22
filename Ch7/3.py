'''
The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/π:
1
π = 2
√
2
9801
∞
∑
k=0
(4k)!(1103 + 26390k)
(k!)43964k
Write a function called estimate_pi that uses this formula to compute and return an estimate of
π. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.
Solution: https: // thinkpython. com/ code/ pi. py .
'''

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def estimate_pi():
    term = 1
    k = 0
    pi_estimate = 0
    coeff = 2 * math.sqrt(2) / 9801
    while term > 1e-15:
        term = (factorial(4 * k) * (1103 + 26390 * k)) / (math.pow(factorial(k),4) * math.pow(396, 4 * k))
        pi_estimate += term
        k+=1
    return 1 / (coeff * pi_estimate)
print(math.pi - estimate_pi())