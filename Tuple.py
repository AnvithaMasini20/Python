#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Create a tuple containing three elements 

t=("apple",5,True)
print(t)


# In[6]:


#Access the 2nd element from the given tuple 

t=("cat","dog","bird","fish")
print(t[1])


# In[7]:


#Concatenate two tuples

t1=(1,2,3)
t2=("a","b","c")
t3=t1+t2
print(t3)


# In[8]:


#Find the length of the tuple

t=(10,20,30,40,50)
print(len(t))


# In[10]:


#Check if the element 25 exists in the tuple

t=(10,20,0,40,50)
if 25 in t:
    print("True")
else:
    print("False")


# In[ ]:




