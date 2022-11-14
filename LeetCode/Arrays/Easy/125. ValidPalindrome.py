"""
------------------------------------------------------------------------------------------------------------------------------------------------
125. Valid Palindrome (Blind)(LeetCode)

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it 
reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a STRING "s", return true if it is a palindrome, or false otherwise.

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

We must note that we are only considering alphanumeric characters.

The first way to solve this question is to build a new string and filter out all the characters that are not numebrs and letters. We can do this 
by instantiating a variable, looping through the string and adding to the new string the alpha numeric characters. Once we have the new string,
we can reverse it and compare it to the original. Note that this solution uses extra mememory and also uses built-in methods, like .isalnum().

The second solution, does not require any extra memory. We will be using a left and a right pointer set to the beginning and the end of the array,
respectively. We will increment/decrement both pointers until we have reached an alphanumeric character. Once left and right are at a proper character, 
we compare the two, if they are not the same, we return false showing that it is not a palindrome. 
We must make sure that the left and the right pointer do not cross, to do this we will use a while loop.

The third solution is for when we do not have any unwanted characters, therefore we dont need to make any checks. We will loop through half of 
the string comparing the left with the right. The right side index will be calculated by subtracting the current index - 1, from the length of the
string. This will decrement from the right without us needing to use pointers. 

Ex. s = "A man, a plan, a canal: Panama"

l   | r
A     a
        
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
