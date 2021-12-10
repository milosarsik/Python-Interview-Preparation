"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) space complexity
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    listSet = set()

    while curr:
        if curr in listSet:
            return curr
        listSet.add(curr)
        curr = curr.next

    return None

# O(1) space complexity
def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    pointer = head
    while pointer != fast:
        pointer = pointer.next
        fast = fast.next

    return pointer
