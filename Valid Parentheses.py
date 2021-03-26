# -*- coding: utf-8 -*-
"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true
"""

'''
use a dictionary to checking the matching situation
use the feature of stack to store the visited Parentheses
'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}','[':']','(':')'}
        stack = []
        #if len(s)%2 !=0 or s ==[]: return False
        for b in s:
            if b in ['{','[','(']:
                stack.append(b)
            elif len(stack)==0 or b!= dic[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        