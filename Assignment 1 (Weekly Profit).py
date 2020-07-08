#!/usr/bin/env python
# coding: utf-8

# # Assignment-1 (Weekly Profit)
# If you had deposited a coin on the cryptocurrency exchange that brought 7% fixed profit daily for a week, how much would your $ 1000 reach at the end of the 7th day?

# In[2]:


money_to_invest = int(input("Please enter the amount you want to deposit?")) # the money we want to deposit

day = int(input("Please enter the number of days you want your money to remain?")) # the  days we want to remain

constant_profit = 7/100 # % of daily earnings

gain = 1 + constant_profit # the amount we will earn daily

have_amount = money_to_invest*gain**day 

    

print("Money in your hand after {} days : {}".format(day,have_amount ))

