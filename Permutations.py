# -*- coding: utf-8 -*-
"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
"""


'''
recursion, backtracking

        A.append(d)
        helper(A)
        A.pop()
    only if len(A)==n: ans.append(list(A))
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(A =[],n=len(nums),ans=[],num_list=nums):
            if len(A)==n:
                ans.append(list(A))
            else:
                for d in num_list:
                    A.append(d)
                    tmp = num_list.copy()
                    tmp.remove(d)
                    helper(A=A,num_list=tmp)
                    A.pop()
            return ans 
        return helper()