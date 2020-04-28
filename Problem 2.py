#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree
# Project 2- Problems vs Algorithms
# Problem 2: Search in a Rotated Sorted Array

def binary_search(input_list,number, start, end): # recursive binary search function
    if start > end:
        return -1

    mid_index = (start + end) // 2      # finding the mid element of the list
    mid_element = input_list[mid_index]

    if mid_element == number:
        return mid_index

    index_left_side = binary_search(input_list,number, start, mid_index - 1) # searching left side
    index_right_side = binary_search(input_list,number, mid_index + 1, end)  # searching right side

    return max(index_left_side, index_right_side)  # returning max of both
    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search(input_list,number, start=0, end=len(input_list)-1) # calling binay serach function for input_list
        
            

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# TEST CASES:
print("Test cases : ")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[1], 0])


# In[ ]:




