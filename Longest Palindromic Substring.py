# -*- coding: utf-8 -*-
"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"

"""

# this is a DP question
'''
the optimal substructure:
    
    if  s[i]==s[j] then dp[i][j] = dp[i+1][j-1]
    
    mind the index to make sure that j-1>i+1  => j-i>(=)2
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2 : return s
        if size ==2 and len(set(s))==2: return s[0]
        if size ==2 and len(set(s))!=2: return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = True

        start = 0
        maxlen = 1

        for j in range(1,size):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i < 2:
                        dp[i][j] =True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j]:
                    if j-i + 1> maxlen:
                        start = i
                        maxlen = j-i +1
        return s[start:start+maxlen]