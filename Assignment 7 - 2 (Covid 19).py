#!/usr/bin/env python
# coding: utf-8

# # Assignment 7- 2 (Covid-19)
# Problem :
# 
# Task : Estimating the risk of death from coronavirus. Write a program that;
# 
# Takes "Yes" or "No" from the user as an answer to the following questions :
# 
# Are you a cigarette addict older than 75 years old? Variable → age
# 
# Do you have a severe chronic disease? Variable → chronic
# 
# Is your immune system too weak? Variable → immune
# 
# Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).
# 

# In[1]:


age = input("Are you a cigarette addict older than 75 years old?(yes/no)")
if age == "yes":
    age = True
else:
    age = False

chronic = input("Do you have a severe chronic disease?(yes/no)")
if chronic == "yes":
    chronic = True
else:
    chronic = False

    
immune = input("Is your immune system too weak?(yes/no)")
if immune == "yes":
    immune = True
else:
    immune = False
 
risk = (age or chronic or immune)


if risk == True :
    print("You are in risky group")
else:
    print("You are not in risky group")


# In[ ]:




