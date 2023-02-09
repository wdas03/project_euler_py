# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:35:59 2017

@author: williamdas
"""


def palindrome(num):
    n = str(num)
    num_array = []
    for i in n:
        num_array += [i]
    if list(reversed(num_array)) == num_array:
        return True
    else:
        return False
    

def largest_3digit_palindrome_product():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if palindrome(product):
                palindromes += [product]
    return sorted(palindromes)[-1]
    
print(largest_3digit_palindrome_product())