# -*- coding: utf-8 -*-
"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

'''
Idea of back tracing

l : # of left bracket
r : # of right bracket

we need to make sure that l<=n, r<=n r<=l  
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def help(A,l,r):
            if len(A)==2*n:
                ans.append(('').join(A))
            else:
                if l<n:
                    A.append('(')
                    help(A,l+1,r)
                    A.pop()
                if r<l:
                    A.append(')')
                    help(A,l,r+1)
                    A.pop()
        help([],0,0)
        return ans