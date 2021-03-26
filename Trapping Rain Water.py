# -*- coding: utf-8 -*-
"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

'''
two pointers to go through left and right part of current position

two extra values 

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        #dict={}
        ans =0

        for i in range(1,len(height)-1):
            l_max = max(height[0:i])
            r_max = max(height[i+1:])
            min_height = min(l_max, r_max)
            if min_height>height[i]:
                ans = ans+min_height-height[i]

        return ans