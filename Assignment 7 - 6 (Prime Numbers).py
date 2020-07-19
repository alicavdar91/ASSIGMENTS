#!/usr/bin/env python
# coding: utf-8

# # Task : Print the prime numbers which are between 1 to entered limit number (n).
# 
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :
# 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
# 

# In[28]:


number = int(input("Please enter a number: "))
prime_number = []
count = 0
for i in range(2,number):
    for j in range(1,(i+1)):
        if i % j == 0:
            count += 1
    if count == 2 :
        prime_number.append(i)
    count = 0 
        
print(prime_number)

