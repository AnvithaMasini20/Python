#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create an empty dictionary

d={}
print(d)


# In[8]:


#Create a dictionary to store the age of two people 

d={
    "John":25,
   "Alice":30
            }
print(d)


# In[13]:


#Access the value associated with the key "city" from the given dictionary

d={
    "Name":"ALice",
    "City":"New York",
    "Age":30
              }
print(d["City"])


# In[14]:


#Create a dictionary to store the contact information of a person 

d={
    "Name":"Bob",
    "Email":"bob@sample.com"
}
print(d)


# In[18]:


#Access the value asssociated with the key "score" from the given dictionary

d={
    "Name":"John",
    "Age":22,
    "Score":85
}
print(d["Score"])


# In[19]:


#Create a dictionary to represent a rectangle.The rectangle has a width of 10 and a height of 5

d={
    "width":10,
    "height":5
}
print(d)


# In[22]:


#Access the value associated with the key "phone" from the given dictionary.If the key does not exist,return "Not available"

d={
    "name":"Eve",
    "age":27
}
phone=d.get("phone","Not available")
print(phone)


# In[33]:


#Given the initial dictionary employee and modify the value of the key "age" to 35

employee={
           "name":"Alice",
           "age":30
}
employee["age"]=35
print(employee)


# In[35]:


#Add a new key-value pair to the dictionary fruits,where the key is "orange" and the value is 3

fruits={
         "apple":5,
         "banana":7
}
fruits["orange"]=3
print(fruits)


# In[39]:


#Given the dictionary inventory,remove the key "sugar" and its associated value from the dictionary

inventory={
           "apple":10,
           "banana":15,
           "sugar":2
}
inventory.pop("sugar")
print(inventory)


# In[ ]:




