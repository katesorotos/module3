# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:52:12 2019

@author: Kate Sorotos
"""
    
class Calculator(object):
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance (x, number_types) and isinstance (y, number_types): #isinstance() checks if x or y is of type (number_types)
            result = x + y
            print('Result is: {}'.format(result))
            return result
        else:
            raise ValueError
            
calc1 = Calculator()
calc1.add(3,4)