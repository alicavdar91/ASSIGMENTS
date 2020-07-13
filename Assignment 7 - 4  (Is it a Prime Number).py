#!/usr/bin/env python
# coding: utf-8

# # Task : Write a program that takes a number from the user and prints the result to check if it is a prime number.
# 
# The examples of the desired output are as follows :
# 
# input →  19 ⇉ output : 19 is a prime number
# input →  10 ⇉ output : 10 is not a prime number 

# In[3]:


number = int(input("Please enter a number : "))

count = 0

for i in range(1, (number+1)):
    if number % i == 0:
        count = count + 1
        
if (number == 0) or (number == 1) or count >= 3 :
    print(f"{number} is not a prime number")
else :
    print(f"{number} is a prime number")

