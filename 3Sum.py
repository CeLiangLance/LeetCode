# -*- coding: utf-8 -*-
"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

'''
sort the list to save time of visiting

be careful with the repeation skip
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:break
            if i>0 and nums[i-1]==nums[i]: continue
            
            j = i+1
            k = len(nums)-1
            
            while j <k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp ==0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j-1]==nums[j]: j+=1
                    while j<k and nums[k+1]==nums[k]: k-=1
                elif tmp >0:
                    k-=1
                    while j<k and nums[k+1]==nums[k]: k-=1
                else:
                    j+=1
                    while j<k and nums[j-1]==nums[j]: j+=1
        return ans

