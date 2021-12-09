# Python-Interview-Preparation-
This is a repository to store all of the solutions to every Python interview question that I do.

# Table of Contents
* [Elements of Programming Interviews in Python](#elements-of-programming-interviews-in-python)
	* Arrays
		* [Arrays Syntax](#arrays-syntax)
		* [Problems](#problems)
			* [](#)
			* [](#)
			* [](#)

# Elements of Programming Interviews in Python
## Arrays
### Arrays Syntax
#### Instantiation
```
list = [1,2,3,4,5]
list = [1] + [0] * 10
list(range(100))
```
#### Basic Operations
```
len(list)
list.append(42)
list.remove(42)
list.insert(3, 28)
```
#### Value Exists
```
a in list
```
#### Copying (Shallow & Deep)
```
listB = listA
```
This will make listB point to listA. They will have the same values.
##### Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
```
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```
Changes in the old_list, will appear in the new_list. Changes in the new_list will not appear in the old_list.
##### Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
```
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```
In the above program, we use deepcopy() function to create copy which looks similar. However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.
#### Key Methods
Key methods for list include `min(A)`, `max(A)`, binary search for sorted lists (`bisect.bisect(A,6)`, `bisect.bisect-left(A,6)`, and `bisect.bisect_right(A,6)`), `A.reverse()` (in-place), `reversed(A)` (returns an iterator), `A.sort()` (in-place), `sorted(A)` (returns a copy), `del A[i]` (deletes the i-th element), `and del A[i: j]` (removes the slice)
#### Slicing
`A = [1, 6, 3, 4, 5, 2, 77]`. Here are some examples of slicing: `A[2:4]` is [3, 4], `A[2:]` is [3, 4, 5, 2, 77], `A[:4]` is [1, 6, 3, 4], `A[:-1]` is [1, 6, 3, 4, 5, 2], `A[-3:]` is [5, 2, 7], `A[-3:-1]` is [5, 2], `A[1:5:2]` is [6, 4], `A[5:1:-2]` is [2, 4], and `A[::-1]` is [7, 2, 5, 4, 3, 6, 1] (reverses list). Slicing can also be used to rotate a list `A[k:l] + A[:k]` rotates A by k to the left. It can also be used to create a copy: `B = A[:]` does a (shallow) copy of A into B.
#### List Comprehension
Python provides a feature called list comprehension that is a succinct way to create lists. A list comprehension consists of (1.) an input sequence, (2.) an iterator over the input sequence, (3.) a logical condition over the iterator (this is optional), and (4.) an expression that yieldsthe elements of the derived list. For example, `[x**2 for x in range(6)]` yields [0, 1, 4, 9, 16, 25],and `[x**2 for x in range(6) if x%2 == 0]` yields [0, 4, 16].

List comprehension supports multiple levels of looping. This can be used to create the product of sets, e.g., if A = [1, 3, 5] and B = ['d', 'b'], then `[(x, y) for x in A for y in B]` creates [(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]. It can also be used to convert a 2D list to a lD list, e.g., if M = [['a', 'b', 'c'], ['d', 'e',
'f']], x for row in M for x in row creates ['a', 'b', 'c', 'd', 'e', 'f ']. Two levels of looping also allow for iterating over each entry in a 2D list, e.g., lf A = [[1, 2, 3] , [4, 5, 6]] then `[[x**2 for x in row] for row in M]` yields [[1, 4, 9], [16, 25, 36]].

As a general rule, it is best to avoid more than two nested comprehensions, and use conventional nested for loops-the indentation makes it easier to read the program.

### Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 5.1     | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | | &#9744; | |
| 5.2     | []() | | &#9744; | |
| 5.3     | []() | | &#9744; | |
| 5.4     | [55. Jump Game](https://leetcode.com/problems/jump-game/) | | &#9744; | |
| 5.5     | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | | &#9744; | |
| 5.6     | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/BestTimeToBuyAndSellStock.py) | :heavy_check_mark: | |
| 5.7	  | [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | | &#9744; | |
| 5.8     | [280. Wiggle Sort](https://leetcode.com/problems/wiggle-sort) | | &#9744; | |
| 5.9     | [204. Count Primes](https://leetcode.com/problems/count-primes) note: book asks to return a list of the primes | | &#9744; | |
| 5.10    | []() | | &#9744; | |
| 5.11    | [31. Next Permutation](https://leetcode.com/problems/next-permutation/) | | &#9744; | |
| 5.12    | []() | | &#9744; | |
| 5.13    | []() | | &#9744; | |
| 5.14    | [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) | | &#9744; | |
| 5.15    | []() | | &#9744; | |
| 5.16    | []() | | &#9744; | |
| 5.17    | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | | &#9744; | |
| 5.18    | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | | &#9744; | |
| 5.19    | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | | &#9744; | |
| 5.20    | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | | &#9744; | |
| BLIND   | [1. Two Sum](https://leetcode.com/problems/two-sum/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/TwoSum.py) | :heavy_check_mark: | HASHMAP ➡️ Instantiate a hashmap. Loop through the array. Calculate the complement by subtracting the target by the current value of the index were on. If the complement is in the hashmap, return the current index and the index of the complement as a List. If it is not in the hashmap, add the current value of the index were on, to the hashmap, mapping the current value to the index. |
| BLIND   | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ContainerWithMostWater.py) | :heavy_check_mark: | |
| BLIND   | [15. 3Sum](https://leetcode.com/problems/3sum/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/3Sum.py) | :heavy_check_mark: | |
| BLIND   | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SearchInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | :heavy_check_mark: | |
| BLIND   | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/MaximumProductSubarray.py) | :heavy_check_mark: | |
| BLIND   | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/FindMinimumInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/ContainsDuplicate.py) | :heavy_check_mark: | |
| BLIND   | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ProductOfArrayExceptSelf.py) | :heavy_check_mark: | |

## Strings
### String Syntax
#### Instantiation

### Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 6.1     | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) (Medium) | [Code]() | &#9744; | |
| 6.2 	  | []() | [Code]() | &#9744; | |
| 6.3     | [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.4 	  | []() | [Code]() | &#9744; | |
| 6.5 	  | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Easy/ValidPalindrome.py) | ✔️ | Use left and right pointers. Update left and right until each one points at an alphanum. Then compare left and right, continue until left >= right. Don’t distinguish between upper and lowercase. Make own alphanum function |
| 6.6 	  | [186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.7 	  | [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.8     | [38. Count and Say](https://leetcode.com/problems/count-and-say/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.9 	  | [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.10 	  | [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.11 	  | []() | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.12 	  | [443. String Compression](https://leetcode.com/problems/string-compression/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| 6.13 	  | [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/) | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | &#9744; | |
| BLIND   | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/LongestSubstringWithoutRepeatingCharacters.py) | ✔️ | Use the sliding window technique, if we see the same character twice within the current window, shift the start position |
| BLIND   | [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/LongestPalindromicSubstring.py) | ✔️ | |
| BLIND   | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Easy/ValidParentheses.py) | ✔️ | Push opening brace on stack, pop if matching close brace, at the end if the stack is empty, return "True". Use hashmap for the closed to open parentheses |
| BLIND   | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/GroupAnagrams.py) | ✔️ | |
| BLIND   | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) 🔴 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Hard/MinimumWindowSubstring.py) | ✔️ | |
| BLIND   | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Easy/ValidAnagram.py) | ✔️ | Use hashmaps to count each character in both strings, then compare the lengths of each element. One liner solution you sort the strings and compare |
| BLIND   | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/LongestRepeatingCharacterReplacement.py) | ✔️ | |
| BLIND   | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/PalindromicSubstrings.py) | ✔️ | |
| BLIND   | [0. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Unknown) ⚫ | [Code]() | &#9744; | |


## Linked Lists
### Linked Lists Syntax
#### Instantiation

### Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 7.1     | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/MergeTwoSortedLists.py) | ✔️ | |
| 7.2     | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/ReverseLinkedList.py) | ✔️ | |
| 7.3     | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Easy) | [Code]() | &#9744; | |
| 7.4     | [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) (Easy) | [Code]() | &#9744; | |
| 7.5     | []() (Easy) | [Code]() | &#9744; | |
| 7.6     | [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) (Easy) | [Code]() | &#9744; | |
| 7.7     | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Medium/RemoveNthNodeFromEndOfList.py) | ✔️ | |
| 7.8     | [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) (Easy) | [Code]() | &#9744; | |
| 7.9     | [61. Rotate List](https://leetcode.com/problems/rotate-list/) (Easy) | [Code]() | &#9744; | |
| 7.10    | [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) (Easy) | [Code]() | &#9744; | |
| 7.11    | [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) (Easy) | [Code]() | &#9744; | |
| 7.12    | [86. Partition List](https://leetcode.com/problems/partition-list/) (Easy) | [Code]() | &#9744; | |
| 7.13    | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Easy) | [Code]() | &#9744; | |
| BLIND   | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/LinkedListCycle.py) | ✔️ | |
| BLIND   | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) 🔴 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Hard/MergeKSortedLists.py) | &#9744; | Skipped |
| BLIND   | [143. Reorder List](https://leetcode.com/problems/merge-k-sorted-lists/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Medium/ReorderList.py) | ✔️ | |
