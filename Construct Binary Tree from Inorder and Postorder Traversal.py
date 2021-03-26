# -*- coding: utf-8 -*-
"""
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium


Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
"""

'''
Recursion
def recursion(level,par1,...):
    #1. recursion terminator
    #2. process current level
    #3. drill down

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(inorder,postorder):
            if not inorder or not postorder: return
            node = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            node.left = helper(inorder[:index],postorder[:index])
            node.right = helper(inorder[index+1:],postorder[index :-1])
            return node
        return helper(inorder,postorder)