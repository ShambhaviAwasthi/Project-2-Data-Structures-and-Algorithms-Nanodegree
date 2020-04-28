#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Shambhavi Awasthi
# Data Structures and Algorithms Nanodegree
# Project 2 - Problems vs Algorithms
# Problem 1: Finding the Square Root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
   
    if number<0:   # base cases
        return None
    elif number==1 or number==0:
        return number
    else:   
        start_index=0
        end_index=number//2  # dividing the number in the middle
        while start_index <= end_index:   # till we find the single number
            mid_val=(start_index+end_index)//2    # middle value is found for the given number i.e 16/2=8
            mid_square=mid_val*mid_val            # using this mid val find square i.e 8*8=64
            if mid_square==number:                # check if square is equal to original number, if yes return the number
                return mid_val
            elif mid_square<number:               # if the square is less than the number , mid val gives floor value
                start_index=mid_val+1             # now we search for second half
                floor_val=mid_val
            else:                                 # if square is greater than number, then we search further in first half
                end_index=mid_val-1
        return floor_val
    
# TEST CASES:

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (13 == sqrt(169)) else "Fail")
print ("Pass" if  (None == sqrt(-27)) else "Fail")
print ("Pass" if  (12 == sqrt(144)) else "Fail")


# In[ ]:




