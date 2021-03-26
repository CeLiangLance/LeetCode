# -*- coding: utf-8 -*-
"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2: return len(s)
        window = []
        ans = 0
        window.append(s[0])
        
        for i in range(1,len(s)):
            while s[i] in window:
                del window[0]
            window.append(s[i])
            ans = max(ans,len(window))
             
        return ans