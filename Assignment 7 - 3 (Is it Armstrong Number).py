#!/usr/bin/env python
# coding: utf-8

# # Task:
# 
# Find out if a given number is an "Armstrong Number".
# 
# An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
# 371 = 33 + 73 + 13;
# 9474 = 94 + 44 + 74 + 44;
# 93084 = 95 + 35 + 05 + 85 + 45.
# 
# # Write a Python program that;
# takes a positive integer number from the user,
# checks the entered number if it is Armstrong,
# consider the negative, float and any entries other than numeric values then display a warning message to the user.
# 

# In[2]:


number = input("Please enter a positive integer number : ")
digits = [] 
coefficient = []
total = 0


if   number.isdigit() == True   :
    
    for i in range(0,(len(number))):
        digits.append(number[i]) # Digit numbers of the number we entered
    
    for ii in digits:
        coefficient.append(int(ii)**len(digits)) # Coefficients of their digits as many as their own digits
    
    for iii in coefficient:
        total = total + iii # Sum of the coefficients of the digits as much as their own number of digits
    

    
    if int(number) == total:
        print( f"{number} is an Armstrong number")
    elif int(number) != total:
        print( f"{number} is not an Armstrong number")
        
else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

