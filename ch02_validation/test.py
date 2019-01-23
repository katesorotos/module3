# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:28:15 2019

@author: Kate Sorotos
"""

class Spam(object): 
    def __init__(self, description, value):      
        if not description or value <=0:           
            raise ValueError      
        self.description = description      
        self.value = value

#s = Spam('s', 5)
#print(s.value)

#s = Spam('', -1) # given the wrong input it will raise an error message 

# similarly you can write the code using assert statements 
# this may happen alot in test conditions
class Spam(object): 
    def __init__(self, description, value):      
        assert description != ""          
        assert value > 0      
        self.description = description      
        self.value = value

s = Spam('', -1)
print(s.value)