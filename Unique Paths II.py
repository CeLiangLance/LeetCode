# -*- coding: utf-8 -*-
"""
63. Unique Paths II


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

"""

'''
This is a typical DP peoblem

for the position(i,j),  dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1- obstacleGrid[i][j])


'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 : return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [n*[0] for _ in range(m)]
        dp[0][0] = 1 

        for i in range(1,m): dp[i][0] = dp[i-1][0]  * (1- obstacleGrid[i][0])
        for j in range(1,n): dp[0][j] = dp[0][j-1]  * (1- obstacleGrid[0][j])

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1- obstacleGrid[i][j])
        
        return dp[-1][-1]