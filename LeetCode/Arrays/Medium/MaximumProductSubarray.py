"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Time complexity: O(n). We are passing once.
Space complexity: O(1). We are not using an array, we are just storing in single variables
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
         
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
                
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            res = max(res, curMax)
        
        return res
