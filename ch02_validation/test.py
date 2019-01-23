# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:28:15 2019

@author: Kate Sorotos
"""
print('Choice 1: Display my name')
print('Choice 2: Display my age')
print('Choice 3: Display my city')

choice = 0

while True:
    try:
        while choice < 1 or choice > 3:
            choice = int(input('What is your choice? '))
        break
    except ValueError:
        print('Error - Please type either a 1, 2 or 3')
        
if choice == 1:
    print('Kate')
elif choice == 2:
    print('23 years old')
elif choice == 3:
    print('London')
