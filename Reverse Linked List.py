# -*- coding: utf-8 -*-
"""
06. Reverse Linked List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        now = head
        while now:
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp
        return pre