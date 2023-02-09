# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:21:30 2017

@author: williamdas
"""

def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def smpf(n):
    return sorted(prime_factorization(n))[0]
    
def S(n):
    smpfs = []
    for i in range(2, n + 1):
        smpfs += [smpf(i)]
    return sum(smpfs)
    
print(S(10 ** 5))