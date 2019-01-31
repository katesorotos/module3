# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:22 2019

@author: Kate Sorotos
"""
"""ch04_unit_testing"""

import unittest
import sys
from ch04_katesorotos import is_prime

class prime_test(unittest.TestCase): # takes an input of test case method
    def test_is_five_prime(self): # giving attributes to prime_test() function using 'self' 
        self.assertTrue(is_prime(5))
        
    def test_sys_input(self):
        self.assertIsInstance(sys.argv[0], int) # position [0] is file name
        self.assertTrue(is_prime(sys.argv[0]))
        
if __name__ == '__main__':
    unittest.main()