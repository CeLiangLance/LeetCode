# -*- coding: utf-8 -*-
"""
429. N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 
Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


'''
BFS
the idea is to make use of the deque data structure, the popleft() function
then we could save the order of nodes of each layer to visit

'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        ans = []
        if root ==None: return ans
        layer = deque()
        layer.append(root)
        
        while layer:
            curr_layer = []
            for _ in range(len(layer)):
                node = layer.popleft()
                for child in node.children:
                    if child: layer.append(child)
                curr_layer.append(node.val)
            ans.append(curr_layer)
        return ans
            