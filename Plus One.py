# -*- coding: utf-8 -*-
"""
66. Plus One


Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

# convert the data type

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans =0
        for i in range(len(digits)):
            ans = ans + digits[i] * (10** (len(digits)-i-1))
        ans = ans+1
        result=[]

        while (ans>0):
            tmp = ans% 10
            result.insert(0,tmp )
            ans = ans//10
        return result
