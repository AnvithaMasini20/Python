#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Write a program thta takes a number as input and print "Even" if it's an even number and "Odd" if it's an odd number.

n=int(input("Enter a number:"))
if (n%2==0):
    print("Even")
else:
    print("Odd")


# In[15]:


#Write a program that takes two numbers as input and print the larger number 

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if a>b:
    print("a is larger")
else:
    print("b is larger")


# In[24]:


#Check if the given number is positive,negative or zero

a=int(input("Enter a number:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")


# In[33]:


#Determine the type of a given number:even,odd,positive or negative

n=int(input("Enter a number:"))
if n>0:
    print("The number is positive")
elif n<0:
    print("The number is negative")
else:
    print("The number is zero")
if n%2==0:
    print("The number is even")
else:
    print("The number is odd")


# In[ ]:





# In[ ]:




