"""
------------------------------------------------------------------------------------------------------------------------------------------------
128. Longest Consecutive Sequence (NeetCode)

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

Add all of the nums to a set, then iterate through the list of nums. Check if the num is the start of a 
sequence by seeing if nums - 1, aka the value before it, exists in the set. If it does exist, continue to
the next num. 

If it doesnt exist, that means that it is the start of sequence. Continue incrementing the value, and 
checking if it exists in the set. Increment the length as long as the next value exists. Once a value
is not found in the set, get the max of the longest and length values. 

Return the longest value. 

Time complexity: O(n). 
Space complexity: O(n). 
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
