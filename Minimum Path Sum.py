# -*- coding: utf-8 -*-
"""
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""

'''
DP problem
grid[j][i] = grid[j][i] + min(grid[j-1][i],grid[j][i-1])

'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i-1] + grid[0][i]
        for j in range(1,m):
            grid[j][0] = grid[j-1][0] + grid[j][0]

        for i in range(1,n):
            for j in range(1,m):
                grid[j][i] = grid[j][i] + min(grid[j-1][i],grid[j][i-1])

        return grid[-1][-1]