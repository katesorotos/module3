# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:59:29 2019

@author: Kate Sorotos
"""

import unittest
from calculator_app import Calculator


class calculator_test(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add_method(self):
        result = self.calc.add(2,2)
        self.assertEqual(4,result)
    def test_error_message(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        
if __name__ == '__main__':
    unittest.main()