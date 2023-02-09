# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:07:36 2017

@author: williamdas
"""
from collections import Counter

class Factor():

    def __init__(self, number, power):
        self.number = number
        self.power = power
        self.value = self.number ** (self.power)
        
    def __str__(self):
        return '<Factor Object-Number:{},Power:{}>'.format(self.number, self.power)

    def __repr__(self):
        return '{}^{}'.format(self.number, self.power)

    def __mul__(self, other):
        return self.value * other.value
        

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
    
def decreasing_prime_powers(num):
    primes = prime_factorization(num)
    #print(primes)
    counter = Counter(primes)
    factors = []
    for i in counter.most_common():
        factors += [Factor(i[0], i[1])]
    powers = [x.power for x in sorted(factors, key=lambda x: x.number)]
    return powers
    
def decreasing_list_test(num):
    reversed_list = list(reversed(decreasing_prime_powers(num)))
    if sorted(reversed_list) == reversed_list or len(set(reversed_list)) <= 1:
        return True
    else:
        return False
        
def num_decreasing_prime_powers(num):
    count = 0 
    for i in range(3, num + 1):
        tof = decreasing_list_test(i)
        if tof is True:
            pass
        elif tof is False:
            count += 1
    return num - count
    
def num_decreasing_prime_powers_1013(num):
    count = num - 77948
    for i in range((10 ** 6) + 1, num + 1):
        tof = decreasing_list_test(i)
        if tof is True:
            pass
        elif tof is False:
            count -= 1
    return count
    
def d(num):
    count = num - 77948
    for i in range((10 ** 6) + 1, num + 1):
        tof = decreasing_list_test(i)
        if tof is True:
            pass
        elif tof is False:
            count -= 1
    return count
    
#print(d(10 ** 7))
        
 
print(num_decreasing_prime_powers(10 ** 13))
# print(decreasing_list_test(360))
