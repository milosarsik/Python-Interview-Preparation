"""
------------------------------------------------------------------------------------------------------------------------------------------------
53. Maximum Subarray (Blind)(LeetCode)
------------------------------------------------------------------------------------------------------------------------------------------------

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough
------------------------------------------------------------------------------------------------------------------------------------------------

We will solve this problem by using the MAX() method to get the max of the current sum we calculate, compared to the previous. This is a very similar 
question to best time to buy and sell stocks.
Instantiate two variables, one to hold the current sum and the other to hold the max sum. Use the max built-in function to update the vairables and 
after the loop return the max sum. The current max will be calculated by comparing the current value and the sum of the current sum and the value.

Ex. nums = [5,4,-1,7,8]

currSum  |  maxSum  |  num  |
   5           5      -----  
   9           9        4
   8           9        -1
   15          15       7
   23          23       8    

Return: 23

Time complexity: O(n). We are iterating through every value in the list, which is n elements.
Space complexity: O(1). We are not creating any extra space.
------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            print(num)
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
