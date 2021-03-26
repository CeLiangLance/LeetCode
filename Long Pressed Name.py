# -*- coding: utf-8 -*-
"""
925. Long Pressed Name

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
"""

'''
this may not a good answer, too much condition to check
'''
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n,m = len(name),len(typed)
        i,j = 0,0
        tmp = name[0]
        while i<n and j <m:

            if name[i]==typed[j]:
                tmp = name[i]
                i+=1
                j+=1
                
            else:
                if typed[j] == tmp: j+=1
                else: return False

            if i!=n and j == m:
                return False
            elif i==n and j == m:
                return True
            elif i==n and j != m:
                for k in range(j,m):
                    if typed[k]!= tmp: return False
                return True