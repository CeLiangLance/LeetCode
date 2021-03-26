# -*- coding: utf-8 -*-
"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.


Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
A typical problem of recursion, this is very effcient for tree structure

the terminator is root is not exist
the drill down is the intuitively processing of child nodes
'''

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        def helper(root):
            if root:
                l,r = root.left, root.right
                root.left, root.right = r,l
                helper(root.left)
                helper(root.right)
            return root
        return helper(root)
