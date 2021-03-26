# -*- coding: utf-8 -*-
"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
'''
BFS 
shrink the island at each layer of dill down
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] =='1': 
                    layer =deque()
                    layer.append([i,j])
                    ans = ans+ 1
                    while layer:
                        for _ in range(len(layer)):
                            x,y = layer.popleft()
                            grid[x][y] ='0'
                            for new_x,new_y in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[i]) and grid[new_x][new_y] == '1':
                                    layer.append([new_x,new_y]) 
                                    grid[new_x][new_y] = '0'

                    
        return ans