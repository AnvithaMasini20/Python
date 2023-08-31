#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Patterns

for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()


# In[8]:


for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
    


# In[27]:


temp=3
for i in range(1,5):
    for j in range(temp):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    temp-=1
    print()


# In[26]:


temp=0
for i in range(4,0,-1):
    for j in range(temp):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    temp+=1
    print()


# In[20]:


for i in range(5):
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()


# In[24]:


for i in range(5):
    for j in range(5):
        if(i==0 or j==0 or i==4 or j==4):
            print("#",end=" ")
        elif(i==2 and j==2):
            print("?",end=" ")
        else:
            print("$",end=" ")
    print()


# In[25]:


temp=3
for i in range(1,5):
    for j in range(temp):
        print(" ",end=" ")
    for k in range(2*i-1):
        if k%2==0:
            print("*",end=" ")
        else:
            print("$",end=" ")
    temp-=1
    print()


# In[10]:


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[21]:


for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# In[18]:


temp=4
for i in range(5,8):
    for j in range(1,temp):
        print(i*j,end=" ")
    temp-=1
    print()


# In[ ]:





# In[ ]:




