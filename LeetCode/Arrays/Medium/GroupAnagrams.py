"""
------------------------------------------------------------------------------------------------------------------------------------------------
49. Group Anagrams (NeetCode)

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Time complexity: O(m * n). 
Space complexity: O(n). We are only taking up space for how long each word is. Im actually unsure of this time and space complexity 

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 

We can solve this problem by using HashMap. However, the key will actually be a list that
holds the count of the letters that we are searching for, and the value will be a list of 
the words that contain those letters. Once we have gone through every string, we are going 
to return the resulting array, which is an array of arrays containg the griouped anagrams.

In the count array, the index will be calculated by subtraction the ord(character) by ord("a").

Go over what the ordinal values are quickly if that doesnt make sense above.

Time complexity: O(m * n).
Space complexity: O(1).
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping charCount to list of Anagrams
        
        for s in strs:
            count = [0] * 26    # a ... z
            
            for c in s: 
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()
