"""
------------------------------------------------------------------------------------------------------------------------------------------------
22. Generate Parentheses (NeetCode)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

Only add open parentheses if open < n.
Only add closing p i closed < open.
Base Case: valid IIF open == closed == n.

.join() = The join in Python takes all the elements of an iterable and joins them into a single string. 
It will return the joined string. 

Time complexity: O(n). 
Space complexity: O(n). We are using a stack 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
