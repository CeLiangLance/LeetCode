# -*- coding: utf-8 -*-
"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


'''
a recursion problem

f(n) = f(n-1)+ f(n-2)  => Fibonacci
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(n):
            a,b = 1,2
            i=3
            while i<n+1:
                a,b = b,a+b
                i+=1
            return b

        if n < 3:
            return n
        else:
            return helper(n)