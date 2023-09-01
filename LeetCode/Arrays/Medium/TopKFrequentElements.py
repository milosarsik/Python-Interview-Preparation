"""
------------------------------------------------------------------------------------------------------------------------------------------------
347. Top K Frequent Elements (NeetCode)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 

This question has a little trick to it, that makes it sort of like bucket sort. What we do first is
create a HashMap and count the frequency of each number. The key will be the integer and the value will
be the frequency of that integer. This is where the trick comes in, we can create a list that is as long
as our list of nums because that is the maximum frequency. The list' indices are what we are going to use
as the frquency count, and the value of the index will be a list of integers that share the same frequency.

We will loop through the HashMap and get the key and value (integer and frequency). In the frequency list
we want to insert the integer into the index that is frequency. Therefore if we go to index 5, we will be
returned values that appear 5 times, because they are stored at index 5. 

Then we create a result array to store the most frequent values. We do a reverse for loop that is the length
of the frequency list because we want the most frequent integers. We create another for loop that will go through
the list at the current index and we append that to the resulting list. We check if the length of the resulting
list is the same as k, and when it is we return the resulting array. 

There is no need for another return, because we know that the length of res will reach the length of k.

Time complexity: O(n).
Space complexity: O(n).
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
