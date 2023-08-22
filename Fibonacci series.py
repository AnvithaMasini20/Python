#!/usr/bin/env python
# coding: utf-8

# In[22]:


#Fibonacci series using while loop

n=int(input("Enter the value nth term :"))
i=1
f1=0
f2=1
f3=0
print("Fibonacci series:")
while(i<=n):
    print(f3)
    i+=1
    f1=f2
    f2=f3
    f3=f1+f2
    


# In[23]:


#Fibonacci series using for loop

i=int(input("Enter the number of terms:"))
f1=0
f2=1
for i in range(2,n):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3


# In[ ]:




