#!/usr/bin/env python
# coding: utf-8

# #  ASSİGMENT 6- 1 (PROFİT)
# TASK1 
# You work for a manufacturer as a programmer and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary (sales) containing the cost price per unit (in dollars), sell price per unit (in dollars), and the beginning inventory. Write a program to return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold. The name and the keys of the dictionary are constant, so use them as they are.
# 
# 

# In[1]:


#TASK1
cv = float(input("Please enter the cost value of your product in dollars")) #cv = Abbreviation of cost value
sv = float(input("Please enter the sell value of your product in dollars")) #sv = Abbreviation of sell value
inv = int(input("Please enter the amount of product in your inventory")) #inv = Abbreviation of inventory

sales = {
  "cost_value": cv,
  "sell_value": sv,
  "inventory": inv
}  

profit = (inv*sv) - (inv*cv)
print("Profit from product sales: %.0f" % (profit) )


# TASK2
# Your boss wants you to prepare the payrolls of the workers in your department. You have to convert the amount of dollars into payroll format. In order to help move things along, you have volunteered to write a code that will take a float and return the amount formatting in dollars and cents. 
# 

# In[ ]:


#TASK2
salary = float(input("Please enter quantity"))
transformation = "$%.2f"%salary
print(transformation)

