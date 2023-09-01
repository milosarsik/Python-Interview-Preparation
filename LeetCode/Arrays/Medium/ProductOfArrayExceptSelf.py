"""
------------------------------------------------------------------------------------------------------------------------------------------------
238. Product of Array Except Self (NeetCode)

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 

We want to create a result array that will hold the product of all the values at the index. Instantiate
an array of the length of nums and make every index hold a value of one.

What will do first is calculate the prefix, the product of every value before the current index. Add the
prefix to the result array and then multiply the prefix by the current num. 

Next we will calculate the post fix, therefore we will go backwards from the nums array. Set the postfix 
to a value of 1. Multiply the current res value by the postfix and add it to the array, what we basically
did was multiply the prefix and postfix. Then the next postfix is the current postfix multiplied by
the num[i].

Return the resulting array.

Time complexity: O(n). We are passing once.
Space complexity: O(1). Because the output array does not count as space
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

