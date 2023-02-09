# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 15:50:02 2017

@author: williamdas
"""

def smallest_positive_num_divisible_1_20():
    counter = 2520
    divisors = range(1, 21)
    while True:
        for i in divisors:
            if counter % i == 0:
                continue
            elif counter % i == 0 and i == 20:
                counter += 1
            else:
                counter += 1
                break
    return counter
            
print(smallest_positive_num_divisible_1_20())