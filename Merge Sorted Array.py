# -*- coding: utf-8 -*-
"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            nums1=nums1[0:m]
        if m==0:
            nums1[:] = nums2[:]    
        elif m!=0 and n!=0:
            nums1[-n:]=nums2
        nums1.sort()