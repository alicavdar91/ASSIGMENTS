#!/usr/bin/env python
# coding: utf-8

# # Assignment - 1 (if-Statements)
# 
# Task : Let's say you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
# Write a program that 
# 
# *Takes the first name from the user and compares it to yours,
# *Then if the name the user entered is the same as yours, print out such as : "Hello, Ali! The password is : W@12",
# *If the name the user entered is not the same as yours, print out such as : "Hello, {the name you entered}! See you later."
# 

# In[1]:


name = input("Please enter your name with only the first letter capital.")

if name == "Ali":
    print("Hello, Ali! The password is : W@12")
else:
    print("Hello, {}! See you later.".format(name))


# In[ ]:




