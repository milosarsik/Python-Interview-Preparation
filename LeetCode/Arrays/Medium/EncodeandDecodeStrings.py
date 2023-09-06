"""
------------------------------------------------------------------------------------------------------------------------------------------------
659. Encode and Decode Strings (NeetCode)

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode


Example 1:

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example 2:

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]

Explanation:
One possible encode method is: "we:;say:;:::;yes"

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough



Time complexity: O(n). We are passing once.
Space complexity: O(1).
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res, i = [], 0
        while i < len(str):
            j = i 
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # up until index j, but not including
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res

class Codec:
    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
