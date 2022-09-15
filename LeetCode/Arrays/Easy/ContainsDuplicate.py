"""
------------------------------------------------------------------------------------------------------------------------------------------------
217. Contains Duplicate (Blind)(LeetCode)

Given an INTEGER ARRAY "nums", return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 

There are two solutions we can code for this problem. There is a simple one line solution, and a longer for loop solution.

The one line solution uses a set. Set's do not contain duplicates. Therefore when we compare the length of the set to the length of the 
original array; if they are the same length, there are no duplicates, if they differ in length, there were duplicates and they were removed 
when we created the set. 

For the longer solution, istantiate a SET. Iterate through the list and check if current "num" is in the SET. 
If it is, return true because it contains a duplicate. If it is not in the set, add it to the set and the loop continues to the next value. 
If the loop finishes, return false because we have not found a duplicate value.

Ex. nums = [1,2,3,1]

hashset = [1,2,3]

num
1
2
3
1

Return: true

Time complexity: O(n). We traverse the list containing n elements only once.
Space complexity: O(n). Worst case we have to create space for every element in the list, therefore it is an O(n) space complexity. 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
