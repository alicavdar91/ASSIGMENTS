#!/usr/bin/env python
# coding: utf-8

# # Count the number of each letter in a sentence.
# The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.

# In[10]:


sentence = input("Please enter a sentence: ")

dictionary = {}

for i in sentence:
    letter = sentence.count(i)
    dictionary[i] = letter
print(dictionary)


# In[ ]:




