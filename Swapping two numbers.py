#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Swapping of two numbers in different methods

#Method 1
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
a=a^b
b=a^b
a=a^b
print(a,b)

#Method 2
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
a,b=b,a
print(a,b)

#Method 3
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
a=a+b
b=a-b
a=a-b
print(a,b)

#Method 4
a=int(input("Enter the value"))
b=int(input("Enter the value"))
temp=a
a=b
b=temp
print(a,b)

#Method 5
a=int(input("Enter the value"))
b=int(input("Enter the value"))
a=a*b
b=a//b
a=a//b
print(a,b)


# 
