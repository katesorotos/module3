# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:53:03 2019

@author: Kate Sorotos
"""

"""ch01_Validation"""

#### Task 1 - 
try: 
    f = open('testfile')
except Exception:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
    
#### Task 2 - 
try:
    f = open('testfile.txt')
    s1 = not_exsit
except FileNotFoundError:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check.')
except Exception:
    print('Sorry. Something is wrong after opening function.')
    
#### Task 3 -     
try: 
    f = open('testfile.txt')
    s1 = not_exists 
except Exception as e: # e is a variable representing something wrong 
    print(e)

#name 'not_exists' is not defined
    
#### Task 4 - 
try: 
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

#[Errno 2] No such file or directory: 'testfile.txt'

#### Task 5 - 
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally..')

#[Errno 2] No such file or directory: 'testfile'
#Executing finally..

#### Task 6 - 
try:
    f = open('testfile.txt') # no error here as file name is correct
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally...')


 