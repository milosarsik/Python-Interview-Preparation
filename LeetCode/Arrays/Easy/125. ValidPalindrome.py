"""
------------------------------------------------------------------------------------------------------------------------------------------------
125. Valid Palindrome (Blind)(LeetCode)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, 
it is a palindrome.

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 



Ex. 

Return: true

-----------
Solution #1
Time complexity: O(n). 
Space complexity: O(n). We are using extra memory when reversing the string at the end

-----------
Solution #2
Time complexity: O(n). 
Space complexity: O(1). No extra space needed 

-----------
Solution #3
Time complexity: O(n).
Space complexity: O(1). 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Solution #1
def isPalindrome(self, s: str) -> bool:
    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()

    return newStr == newStr[::-1]
      
# Solution #2
def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not self.alphaNum(s[l]):
            l += 1
        while r > l and not self.alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True

def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))
    
# Solution #3 when we dont have unwanted characters
def isPalindrome(self, s: str) -> bool:
    for i in range(0, int(len(s) // 2)):
        if s[i] != s[len(s)-i-1]:
            return False
    return True
