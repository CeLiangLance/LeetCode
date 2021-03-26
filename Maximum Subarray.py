# -*- coding: utf-8 -*-
"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

'''
DP 
nums[i] = nums[i] + max(0,nums[i-1])
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i] = nums[i] + max(0,nums[i-1])
        return max(nums)