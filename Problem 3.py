#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree
# Project 2 - Problems vs Algorithms
# Problem 3: Rearrange Array Elements

# sorting using merge sort
def mergesort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)
    
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

# function to convert list to number
def convert(list): 
    return int("".join(map(str,list[::1])))

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list)==0:
        return None
    else:
        merged_list=mergesort(input_list)
        num1=[]
        num2=[]
        for i in range(0,len(merged_list)):
            if i%2==0:
                num1.append(merged_list[len(merged_list)-1-i])
            else:
                num2.append(merged_list[len(merged_list)-i-1])
        
        number1=convert(num1)
        number2=convert(num2)
        
        return (number1,number2)        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

        
# Test Cases:
test_case=test_function([[1, 2, 3, 4, 5], [531, 42]])
test_case = test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_case=test_function([[i for i in range(0,101)], [int("".join(map(str,range(100,-1,-2)))), int("".join(map(str,range(99,-1,-2))))]])
test_case=test_function([[0,0,0,0,0,0],[]])
# In[ ]:




