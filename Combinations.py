# -*- coding: utf-8 -*-
"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

'''
Backtrace
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num_list = []
        for i in range(1,n+1):
            num_list.append(int(i))
        ans = []
        def hepler(A, k, num_list):
            if len(A) == k:
                ans.append(list(A))
            else:
                for i in range(len(num_list)):
                    A.append(num_list[i])
                    hepler(A,k,num_list[i+1:])
                    A.pop()
            return ans
        return hepler([],  k, num_list)