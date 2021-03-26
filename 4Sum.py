# -*- coding: utf-8 -*-
"""
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


'''
add one more cylce to make it the three sum

key:  skip the repetition to make the result correct

sort the list to save time of visiting 
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        result = []
        for idx in range(len(nums) - 3):
            if idx > 0 and nums[idx] == nums[idx - 1]: continue  # skip the repetition
            for i in range(idx+1, len(nums)-2):
                if i > idx+1 and nums[i] == nums[i-1]: continue  # skip the repetition
                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[idx] + nums[i] + nums[j] + nums[k]
                    if s > target:
                        k-=1
                        while j<k and nums[k+1]==nums[k]: k-=1
                    elif s < target:
                        j+=1
                        while j<k and nums[j-1]==nums[j]: j+=1
                    else:
                        result.append([nums[idx], nums[i], nums[j], nums[k]])
                        j+=1
                        k-=1
                        while j < k and nums[j]==nums[j-1]: j+=1  # skip the repetition
                        while j < k and nums[k]==nums[k+1]: k-=1  # skip the repetition
        return result