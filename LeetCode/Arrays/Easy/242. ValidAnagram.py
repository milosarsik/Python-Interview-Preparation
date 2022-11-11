"""
------------------------------------------------------------------------------------------------------------------------------------------------
242. Valid Anagram (Blind)(LeetCode)

Given two STRINGS "s" and "t", return true if "t" is an anagram of "s", and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

------------------------------------------------------------------------------------------------------------------------------------------------
Solution Walkthrough 

There are two solutions to this problem. We will mainly be discussing the first, as the second solution is very straight forward.

Two words must have the same number of letters in order to be anagrams. Therefore, we can use this towards our solution, if we count each letter
in each word and the count values are the same for each letter, the words are anagrams of eachother. 

How can we keep track of how many times each letter appears? We can use a HASHMAP, store the letter as the key and then increment the value, when
the letter appears again. One case we have to watch out for is, if the letter does not exist in the HASHMAP, we have to add it to the HASHMAP with
a value of one. If the letter already exists as the key, we add one to the current value. If we try to access a key that doesn't exist, we will get
an error, therefore we can use the .get() method to search for the key, but if it does exist, we can instantiate it with a default value. .get(),
takes two parameters as shown in the solution. 

The second solution requires us to sort the strings, then compare them. If they are equal, they are anagrams. The time complexity depends on the 
type of sorting algorithm that we apply. 

The third solution is to use the Counter() data structures, that counts stuff automatically for you. It creates a HASHMAP and iterates over iterable 
objects. 

Ex. s = "anagram", t = "nagaram"

countS = {}
countT = {}

countS     | countT
a               n       
n               a
a               g
g               a
r               r
a               a
m               m    

Return: true

-----------
Solution #1
Time complexity: O(n). We traverse the string containing n elements only once.
Space complexity: O(n) or O(2n). 

-----------
Solution #2
Time complexity: O(n). We traverse the string containing n elements only once.
Space complexity: O(1). Maybe, all depends on the sort function.

-----------
Solution #3
Time complexity: O(n).
Space complexity: O(n) or O(2n). 
------------------------------------------------------------------------------------------------------------------------------------------------
"""

# Solution #1
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    return countS == countT
      
# Solution #2
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

#Solution #3
def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
