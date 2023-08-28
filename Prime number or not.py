#!/usr/bin/env python
# coding: utf-8

# In[35]:


# The given number is prime or not

n=int(input("Enter number:"))
if n>1:
    for i in range(2,n//2):
        if (n%i) == 0:
            print("The number is prime")
            break
    else:
        print("The number is not prime")
else:
    print("The number is neither prime nor composite")


# In[ ]:





# 
