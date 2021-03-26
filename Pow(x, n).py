# -*- coding: utf-8 -*-
"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def hepler(x, n):
            if n==0:
                return 1.0
            else:
                y = hepler(x, n//2)
                if n%2 ==0:
                    return y*y
                else:
                    return y*y*x

        if n <0:
            return 1/hepler(x, -n)
        else:
            return hepler(x, n)
        