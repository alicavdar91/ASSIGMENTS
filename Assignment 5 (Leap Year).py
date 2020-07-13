#!/usr/bin/env python
# coding: utf-8

# # Assignment-5(Leap Year)
# Task:
# 
# Find out if a given year is a "leap" year.
# 
# In the Gregorian calendar, three criteria must be taken into account to identify leap years:
# The year must be evenly divisible by 4;
# If the year can also be evenly divided by 100, it is not a leap year; unless...
# The year is also evenly divisible by 400. Then it is a leap year.
# According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
# Write a Python program that;
# Takes a 4-digit year from the user,
# Prints True if the given year by the user is a leap year, prints False otherwise.

# In[2]:


# Method 1
year = int(input("Please enter a four-digit year. :"))
leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print(leap * f"{year} is a leap year")
print((not leap) * f"{year} is not a leap year")


# In[8]:


# Method 2
year = int(input("Enter the year you want to test for the leap year?"))

if (year % 4) == 0:

    year4 = True

else:

    year4 = False    

if (year % 400) == 0:

    year400 = True

else:

    year400 = False

if (year % 100) == 0:

    year100 = False

else:

    year100 = True    

    

print("Is the year leap year entered?: {}".format(year4 and year400 or year100))

