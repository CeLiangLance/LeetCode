# -*- coding: utf-8 -*-
"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

'''
idae: hash table
in another word restore the values we visited to save the time of visiting
'''



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in dic:
                return[i,dic[b]]
            else:
                dic[a] = i