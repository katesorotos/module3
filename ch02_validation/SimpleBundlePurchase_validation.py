# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:52:48 2018

@author: Kate Sorotos
"""

"""ch02_Data Bundle Purchase_validation"""

import time 

def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode):
        print('\nPassword OK')
        
        time.sleep(1)
        
        print('\nTo request your balance enter "1"')
        print('To purchase data enter "2"')
        print('To top up your account enter "3"')
        
        time.sleep(1)
        
        transactionType = 0
        while True:
            try:
                while transactionType < 1 or transactionType > 3:
                    transactionType = int(input('Please enter your choice: '))
                break
            except ValueError:
                print('Error: please make your choice by entering a number')
                
        print()
        
        if transactionType == 1:
            print('Your balance is: £{}'.format(balance))
            print('Would you like another service? ')
            print('Type "y" for yes or "n" for no')
            restart = input().lower()
            if restart == 'y':
                DataBundlePurchase(truePasscode, balance)
            else:
                print('Thanks, have a nice day!')
                return 'display balance'
        elif transactionType == 2:
             checkNumber(truePasscode, balance)
        elif transactionType == 3:
            topUp(truePasscode, balance)
#        else:
#            print('Error: please make your choice by entering "1" or "2"')
#            return 'Transaction choice error'
    else: 
        print('Password incorrect, would you like to try again? ')
        retryPassword(truePasscode, balance)
        return 'Incorrect password'


        
def retryPassword(truePasscode, balance):
    print('Type "y" for yes or "n" for no')
    retry = input().lower()
    if retry == 'y':
        DataBundlePurchase(truePasscode, balance)
    else:
        print('Thanks, have a nice day!')
        return 'Retry password exit'
    
def passwordCheck(truePasscode):
    attempt = input('Please enter your password ')
    if attempt == truePasscode:
        return True 
    else:
        return False
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def checkNumber(truePasscode, balance):
    phone_number = 0
    while True:
        try:
            while len(str(phone_number)) != 11:
                print('Error - please enter an 11 digit phone number')
                phone_number = input('Please enter your phone number to proceed: ')
            break
        except ValueError:
            print('Error')
    if len(str(phone_number)) == 11:
        print('Password OK')
        dataAmount(truePasscode, balance)  


def dataAmount(truePasscode, balance):
    max = 100.00
    print('>>The maximum amount you are able to top up by is £100')
    print('>>Your top-up amount must be a multiple of 5')
    print()
    time.sleep(1)
    print('You have £' + str(balance) + ' remaining in your balance. \nHow much money would you like to top up by? ')
    money = int(input())
    new_balance = round(balance - money,2)
    
    if money > max:
        print('I\'m afraid you are only able to top up by £100 or less')
        time.sleep(1)
        print('Transaction cancelled')
    elif money > balance:
        print('Amount greater than available balance.')
        time.sleep(1)
        print('Transaction cancelled')
    elif money == int(money/5)*5:
        print('Thanks for your purchase. You now have £' + str(new_balance) + ' left in your account.')
        time.sleep(1)
        print('Would you like another service? ')
        print('Type "y" for yes or "n" for no')
        restart = input().lower()
        if restart == 'y':
            DataBundlePurchase(truePasscode, balance)
        else:
            print('Thanks, have a nice day!')
    else:
        print('Transaction type not recognised.')
    
    
def topUp(truePasscode, balance):
    print('\nYour current balance is £' + str(balance))
    time.sleep(1)
    amount = int(input('How much would you like to top-up by today? £ '))
    balance = balance + amount
    
    print('You have topped up your account by £' + str(amount) + '\nYour balance is now £' + str(balance)) 
    time.sleep(1)
    print('\nWould you like another service? ')
    print('Type "y" for yes or "n" for no')
    restart = input().lower()
    if restart == 'y':
        DataBundlePurchase(truePasscode, balance)
    else:
        print('Thanks, have a nice day!')
        return 'Exit'
    
DataBundlePurchase('1234', 34.55)


    
