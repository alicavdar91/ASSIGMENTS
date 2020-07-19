#!/usr/bin/env python
# coding: utf-8

# # Task : Print the FizzBuzz numbers.
# 
# FizzBuzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.
# 
# 

# # Print numbers from 1 to 100 inclusively following these instructions:
#     *if a number is multiple of 3, print "Fizz" instead of this number,
#     *if a number is multiple of 5, print "Buzz" instead of this number,
#     *for numbers that are multiples of both 3 and 5, print "FizzBuzz",
#     *print the rest of the numbers unchanged.
# Output each value on a separate line.

# In[7]:


numbers = list(range(1,100))
fizzbuzz = []

for i in numbers:
    if i % 3 == 0 and i % 5 != 0  :
        i = "Fizz"
        fizzbuzz.append(i)
    elif i % 5 == 0 and i % 3 != 0 :
        i = "Buzz"
        fizzbuzz.append(i)
    elif i % 3 == 0 and i % 5 == 0 :
        i = "FizzBuzz"
        fizzbuzz.append(i)
    else :
        fizzbuzz.append(i)
fizzbuzz

