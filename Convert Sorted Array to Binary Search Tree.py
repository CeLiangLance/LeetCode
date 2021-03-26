# -*- coding: utf-8 -*-
"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
A example of using recursion to deal with tree structure

the array has sorted,so the middle one is the root and the left ones are left child
and right ones are right child


'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(l,r):
            if l<=r:
                root_index = int((l + r) // 2)
                root = TreeNode(nums[root_index])

                root.left = helper(l,root_index-1)
                root.right = helper(root_index+1,r)
            else:
                return None
            return root
        return helper(0,len(nums)-1)