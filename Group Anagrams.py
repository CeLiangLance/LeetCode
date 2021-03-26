# -*- coding: utf-8 -*-
"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


'''
make use of the inbulit sort function
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict ={}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in dict:
                dict[key] = [strs[i]]
            else:
                dict[key].append(strs[i])
        return list(dict.values())