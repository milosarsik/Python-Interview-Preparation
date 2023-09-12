"""
------------------------------------------------------------------------------------------------------------------------------------------------
739. Daily Temperatures (NeetCode)

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

We want to keep a result array that holds the amount of days that we need to wait. Keep a stack that 
holds a pair of (temp, index). We want to iterate through the temperature array, looping through the 
temperature and index, using the enumerate() method. 

Use a while loop under the conditions that we have a full stack, and current temperature is greater than
the temp at the top of the stack. If the current temp is less than the top of the stack, we break the loop
and append that temperature to the top of the stack and continue UNTIL the top of the stack is greater
than the current temp were looking at.

Once it is, pop off the stack, and subtract the indices to get the amount of days we have to wait. 
After the loop, append the current temp.

Time complexity: O(n). 
Space complexity: O(n). We are using a result array, and stacks. 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
