# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:07:41 2017

@author: williamdas
"""

def sum_of_squares(nums):
    squared_nums = [x ** 2 for x in nums]
    return sum(squared_nums)
    
def square_of_sums(nums):
    sum_nums = sum(nums)
    return sum_nums ** 2

def difference_val(nums):
    x = sum_of_squares(nums)
    y = square_of_sums(nums)
    return y - x

print(difference_val(list(range(1,101))))    
    
    
