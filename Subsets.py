# -*- coding: utf-8 -*-
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def helper(index,ele):
            ans.append(ele)
            for i in range(index,len(nums)):
                helper(i+1,ele+[nums[i]])
        helper(0,[])
        return ans
    
    
# Solution 2
class Solution_2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ele in nums:
            ans += [[ele] + tmp for tmp in ans]
        return ans