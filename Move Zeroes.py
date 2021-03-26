# -*- coding: utf-8 -*-
"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


'''
for a list realted problem. if we wanna speed up 
    1. more than one pointers
    2. expand dimension

'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        while(j<len(nums)):
            if nums[j]==0:
                j+=1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
                i+=1

