# -*- coding: utf-8 -*-
"""
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 
Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
BFS method 
the deque data structure

a templete of BFS
'''

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        from collections import deque
        layer = deque()
        ans = []
        layer.append(root)
        while layer:
            cur_layer = []
            for _ in range(len(layer)):
                node = layer.popleft()
                if not node:
                    continue
                cur_layer.append(node.val)
                layer.append(node.left)
                layer.append(node.right)
            if cur_layer:
                ans.append(max(cur_layer))
        return ans