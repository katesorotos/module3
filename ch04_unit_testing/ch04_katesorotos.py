# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:18:19 2019

@author: Kate Sorotos
"""

"""ch04_unit_testing"""

def is_prime(number):
    if number > 1:
        for num in range(2, number):
            
            if number % num == 0:
                return False
        return True
