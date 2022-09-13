"""
------------------------------------------------------------------------------------------------------------------------------------------------
1. Two Sum (Blind)(LeetCode)

Given an ARRAY OF INTEGERS "nums" and an INTEGER "target", return INDICES of the two numbers such that they add up to "target".
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough

This solution will require a HASHMAP to be solved, and it can be done in one pass. The hashmap will carry the integer from the 
array as the key, and the indice of that integer as the value. Therefore, when we look up the integer (our complement), the hashmap
will return the index of that integer. While we are iterating and inserting elements into the hash table, we also look back to 
check if current element's complement already exists in the hash table. If it exists, we have found a solution and then return 
the indices immediately.

Ex. nums = [3,2,4], target = 6

  HASHMAP
k   |   v   |   complement  |   target  |   i   |
                    3             6         0
3       0
                    4                       1
2       1       
                                            2
                    2

Return: [2, 1]

Time complexity: O(n). We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.
Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.
------------------------------------------------------------------------------------------------------------------------------------------------
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
