"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Time complexity: O(n^2). 
Space complexity: O(1). 
"""

# Solution with function
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        
        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)
            
        return res

    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        return res
   
# Solution without function
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 
        
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res 

