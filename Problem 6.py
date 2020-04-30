#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree
# Project 2 - Problems vs Algorithms
# Problem 6: Max and Min in a Unsorted Array

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None
    else:
        max=-float("inf")
        min=float("inf")
        for i in ints:
            if(i>max):
                max=i
            if(i<min):
                min=i
        return (min,max)  

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 200)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 199) == get_min_max(l)) else "Fail")




# In[ ]:




