#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 Day3

# In[4]:


altitude = 1000
if altitude <= 1000:
    print("Safe to land")
elif altitude <= 5000:
    print("Bring down to 5000")
else:
    print("Turn around")


# # Assignment 2 Day3

# In[5]:


lower=1
upper=200
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




