#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=input(" ")
my_dict=dict({"A":"Hello","B":"World","C":"Buddy"})
my_dict1=dict({"A":"Hello","C":"Buddy","D":"Welcome"})


if n=="A and B" or n=="B and A":
    print(list(my_dict.values())[0],end="")
    print(list(my_dict.values())[1])
if n=="B and C" or n=="C and B":
    print(list(my_dict.values())[1],end="")
    print(list(my_dict.values())[2])
if n=="A and C" or n=="C and A":
    print(list(my_dict.values())[0],end="")
    print(list(my_dict.values())[2])
if n=="D or B":
    print(list(my_dict.values())[1])
if n=="A or B":
    print(list(my_dict.values())[0])
if n=="B or A":
    print(list(my_dict.values())[1])
if n=="B or C":
    print(list(my_dict.values())[1])
if n=="C or B":
    print(list(my_dict.values())[2])
if n=="A or C":
    print(list(my_dict.values())[0])
if n=="C or A":
    print(list(my_dict.values())[2])
if n=="A and B and C":
    print(list(my_dict.values())[0],end="")
    print(list(my_dict.values())[1],end="")
    print(list(my_dict.values())[2])
if n=="A and (B or C)":
    print(list(my_dict.values())[0],end="")
    print(list(my_dict.values())[1],end="")
if n=="A and (C or D)":
    print(list(my_dict.values())[0],end="")
    print(list(my_dict.values())[2],end="")
if n=="A and (B or C) and D":
    print(list(my_dict1.values())[0],end="")
    print(list(my_dict1.values())[1],end="")
    print(list(my_dict1.values())[2])


# In[ ]:




