"""
------------------------------------------------------------------------------------------------------------------------------------------------
206. Reverse Linked List (EPI)(Blind)(LeetCode)
------------------------------------------------------------------------------------------------------------------------------------------------

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough
------------------------------------------------------------------------------------------------------------------------------------------------

This problem can be solved using the two pointer technique. We can start with "prev" and "curr" pointers. We will point the current to previous. 
However, now we do not have a pointer to the third node in the list. To account for this, we will save the "curr.next" node
in a temp value. Then at the end we will set the current as the temp that we saved at the beginning.  

Ex. head = [1,2,3,4,5]
dummy = None

dummy -> 1 <- 2  X  3 -> 4 -> 5

Return: [5,4,3,2,1]

Time complexity: O(n). 
Space complexity: O(1). 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
