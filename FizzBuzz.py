#!/usr/bin/env python
# coding: utf-8

# In[1]:


#If the number is 3,print Fizz instead of the number
#If the number is 5,print Buzz instead of the number
#If the numbers are both 3 and 5,print FizzBuzz 

for i in range(1,101):
    if i%3 == 0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    elif i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    else:
        print(i)


# In[ ]:




