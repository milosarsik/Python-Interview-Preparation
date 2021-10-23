"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Time complexity: O(n).
Space complexity: O(1). 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            print(num)
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
