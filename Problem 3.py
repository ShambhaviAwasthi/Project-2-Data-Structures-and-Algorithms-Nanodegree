#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree
# Project 2 - Problems vs Algorithms
# Problem 4: Dutch National Flag Problem

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    output_list=[]
    list1=[]              # list to store all 1
    list2=[]              # list to store all 2
    for i in input_list:
        if i==0:
            output_list.append(i)
        elif i==1:
            list1.append(i)
        else:
            list2.append(i)
    output_list+=list1[:] # merging the lists
    output_list+=list2[:]
    return output_list
    
        

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

        
# TEST Cases:

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

"""
OUTPUT:
[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Pass
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
Pass
"""


# In[ ]:




