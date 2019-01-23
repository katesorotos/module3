# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 09:39:33 2019

@author: Kate Sorotos
"""

"""ch02_validation"""

### Task 1 - Revise input function
print ("What’s your age?") 
Age = input()

#or

Age = input("What’s your age? ") 

### Task 2 - Cast to int data type 
print("What’s your age?") 
age = int(input()) 
type(age) 

### Task 3 - Validating string content
option = input("Please type yes or no to continue ").lower()
print(option)

#or 

option_2 = input("Please type yes or no to continue ").lower()
if option_2[0] == 'y' or 'n':
    print(option_2)
else:
    print('Error - invalid input')
    
### Task 4 - Validating string length 
while True:
  passcode = input("Please enter your passcode to continue: ")
  if len(passcode) > 4:
     print("Your passcode can only be 4 digits long")
  else:
    break

print("The passcode you entered is " + passcode)

    
phonenumber = []
phone = int(input("Please enter your phone number to continue: "))
if len(str(phone)) == 11:
    phonenumber.append(phone)
    print(phonenumber)
else: 
    phone = int(input("Please enter an 11 digit phone number to continue: "))
    

### Task 5 - Checking errorful input
print('Choice 1: Display my name')
print('Choice 2: Display my age')
print('Choice 3: Display my city')

choice = 0

choice = int(input('What is your choice? '))

while choice < 1 or choice > 3:
    choice = int(input('What is your choice? '))

if choice == 1:
    print('Kate')
elif choice == 2:
    print('23 years old')
elif choice == 3:
    print('London')
    
### Task 6 - Handling errorful input
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
        
### Task 7 - Class based user input validation 
class Spam(object): 
    def __init__(self, description, value):      
        if not description or value <=0:           
            raise ValueError      
        self.description = description      
        self.value = value


s = Spam('s', 5) # given the input with correct range
print(s.value)

s = Spam('', -1) # given the wrong input it will raise an error message 

class Spam(object): 
    def __init__(self, description, value):      
        assert description != ""# similarly you can write the code using assert statements          
        assert value > 0 # this may happen alot in test conditions       
        self.description = description      
        self.value = value

s = Spam('', -1)
print(s.value)