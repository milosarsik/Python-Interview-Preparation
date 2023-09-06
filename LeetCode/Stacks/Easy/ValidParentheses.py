"""
------------------------------------------------------------------------------------------------------------------------------------------------
20. Valid Parentheses (NeetCode)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

In order for two parentheses to be valid, there must be an opening and it must be followed by a closing. We can use a STACK data structure
in order to peek and pop at/from the top. This will give us the ability to check the next parentheses. We are going to create a HASHMAP to find the 
mappings of valid parentheses. We will loop through the list and check the top of the stack, if we have a closing, we check whether the parenthese
on the top of the stack is valid. If it is not, we return false, if it is, we pop from the stack and continue. If it is an open parenthese, we will
add it to the top of our stack and continue the loop in order to find a closing parenthese for it.

Ex. s = "()[]{}"
stack = []

stack   |
(

Return: true

Time complexity: O(n). 
Space complexity: O(n). We are using a stack 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

def isValid(self, s: str) -> bool:
    stack = []
    closeToOpen = {")" : "(", 
                   "]" : "[", 
                   "}" : "{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False 

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
