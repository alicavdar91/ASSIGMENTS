#!/usr/bin/env python
# coding: utf-8

# # Assignment-3 (Measure Converter)
# Task-1:
# 
# Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.
# 
# Task-2:
# Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.
# 

# In[1]:


#TASK 1 CODE : 
celcius = float(input("Enter the Celsius temperature you want to convert to Fahrenheit?"))
fahrenheit =(1.8*(celcius))+ 32

print(fahrenheit)


# In[2]:


#TASK 2 CODE :

kilometers = float(input("Enter the Kilometers you want to convert to Miles?"))

miles = kilometers*1.609344

print(miles)

