"""
------------------------------------------------------------------------------------------------------------------------------------------------
21. Merge Two Sorted Lists (EPI)(Blind)(LeetCode)
------------------------------------------------------------------------------------------------------------------------------------------------

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough
------------------------------------------------------------------------------------------------------------------------------------------------

To solve this problem we can create an output dummy node, compare the values of "l1" and "l2" and add the lowest value to the output list.
We can iterate through the lists using a while loop, on the condition that the lists are non-empty, when one is empty we stop the loop.

In the while loop we can compare the values of the list and add the lowest node to the output node. We can move our tail through the output list.
Once our loop condition is met, we check which list still contains nodes, and then append that list onto the tail of our output. Then finally return 
"dummy.next"

Ex. list1 = [1,2,4], list2 = [1,3,4]
dummy = None
tail = dummy

Return: [1,1,2,3,4,4]

Time complexity: O(n). 
Space complexity: O(1). 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next
