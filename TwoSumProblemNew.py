# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 08:57:28 2018

@author: ahany
"""

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i!=j:
                stindex = i
                ndindex = j
    indecies = [stindex,ndindex]        
    return indecies