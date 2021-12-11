# Python-Interview-Preparation-
This is a repository to store all of the solutions to every Python interview question that I do.

# Table of Contents
* [Elements of Programming Interviews in Python](#elements-of-programming-interviews-in-python)
	* [Primitive Types](#primitive-types) 
		* [Primitive Types Syntax](#primitive-types-syntax)
		* [Primitive Types Problems](#primitive-types-problems)
	* [Arrays](#arrays)
		* [Arrays Syntax](#arrays-syntax)
		* [Arrays Problems](#arrays-problems)
	* [Strings](#strings)
		* [Strings Syntax](#strings-syntax)
		* [Strings Problems](#strings-problems)
	* [Linked Lists](#linked-lists)
		* [Linked Lists Syntax](#linked-lists-syntax)
		* [Linked Lists Problems](#linked-lists-problems)
	* [Stacks and Queues](#stacks-and-queues)
		* [Stacks and Queues Syntax](#stacks-and-queues-syntax)
		* [Stacks and Queues Problems](#stacks-and-queues-problems)
	* [Binary Trees](#binary-trees)
		* [Binary Trees Syntax](#binary-trees-syntax)
		* [Binary Trees Problems](#binary-trees-problems)
	* [Searching](#searching)
		* [Searching Syntax](#searching-syntax)
		* [Searching Problems](#searching-problems)


# Elements of Programming Interviews in Python

## Primitive Types
Be very comfortable with the bitwise operators, particularly XOR.
Understand how to use masks and create them in an machine independent way,
Know fast ways to clear the lowermost set bit (and by extension, set the lowermost 0, get its
index, etc.)
Understand signedness and its implications to shifting.
Consider using a cache to accelerate operations by using it to brute-force small inputs.
Be aware that commutativity and associativity can be used to perform operations in parallel
and reorder operations.

### Primitive Types Syntax
Bitwise operations:
```
Operator 	Example 	Meaning
&		a & b		Bitwise AND (equiv to product)
|		a | b		Bitwise OR
^		a ^ b		Bitwise XOR (exclusive OR)
~		~a		Bitwise NOT (only unary operator)
<<		a << n		Bitwise left shift
>>		a >> n		Bitwise right shift
```
All binary bitwise operators have a corresponding compound operator that performs an augmented assignment:
```
Operator	Example		Equivalent to
&=		a &= b		a = a & b
|=		a |= b		a = a | b
^=		a ^= b		a = a ^ b
<<=		a <<= n		a = a << n
>>=		a >>= n		a = a >> n
```

### Primitive Types Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 4.1     | []() () ⚫ (Unknown) | [Code]() | | |
| 4.7     | [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Primitive%20Types/Medium/Pow(x%2Cn).py) | 🟥 | RECURSION ➡️ Not solved, but it is in the hackathon time frame. Did not solve it using bitwise operators. No clue how. Information is not all included in this question |





## Arrays
Array problems often have simple brute.force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).
Filling an array from the front is slow, so see if it's possible to write values from the back.
Instead of deleting an entry (which requires moving all entries to its left), consider overwriting it.
When dealing with integers encoded by an array consider processing the digits from the backof the array. Alternately, reverse the array so the least-significant digit is the first entry.
Be comfortable with writing code that operates on subarrays
It's incredibly easy to make off-by-l errors when operating on arrays-reading past the last element of an array is a comrnon error which has catastrophic consequences.
Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return.
An array can serve as a good data structure when you know the distribution of the elements inadvance. For example, a Boolean array of length W is a good choice for representing a subset of {0, 1, ..., W - 1}. (When using a Boolean array to represent a subset of {1,2,3, ...,n|, allocate an array of size n+1 to simplify indexing).
When operating on 2D arrays, use parallel logic for rows and for columns.
Sometimes it's easier to simulate the specification, than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an n x n matrix, just compute the output from the beginning.

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

### Arrays Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 5.1     | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SortColors.py) | ✔️ | PARTITION/PIVOT POINT ➡️ Instantiate a left and right pointer and a pivot point i. While i <= r, if nums[i] is zero do a swap with the left and the pivot point, if nums[i] is 2 do a swap with the right and pivot point, but do not increment the pivot point (that is why we decrement the pivot point in the if statment). Simply put we are breaking up the array into 3 section, 0, 1 and 2. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) |
| 5.2     | []() | | &#9744; | |
| 5.3     | []() | | &#9744; | |
| 5.4     | [55. Jump Game](https://leetcode.com/problems/jump-game/) | | &#9744; | |
| 5.5     | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | | &#9744; | |
| 5.6     | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/BestTimeToBuyAndSellStock.py) | :heavy_check_mark: | MAX/MIN ➡️ Keep track of the max profit and the min price. Loop through the prices array, check for the current profit if we sell today, compare the max profit with the current profit, and finally compare the current price to the min price. This can be solved with built in functions, or if statments. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) |
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
| 5.18    | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SpiralMatrix.py) | 🟥 | X ➡️ Not solved, but it is in the hackathon time frame. |
| 5.19    | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | | &#9744; | |
| 5.20    | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | | &#9744; | |
| BLIND   | [1. Two Sum](https://leetcode.com/problems/two-sum/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/TwoSum.py) | :heavy_check_mark: | HASHMAP ➡️ Instantiate a hashmap. Loop through the array. Calculate the complement by subtracting the target by the current value of the index were on. If the complement is in the hashmap, return the current index and the index of the complement as a List. If it is not in the hashmap, add the current value of the index were on, to the hashmap, mapping the current value to the index. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |
| BLIND   | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ContainerWithMostWater.py) | :heavy_check_mark: | |
| BLIND   | [15. 3Sum](https://leetcode.com/problems/3sum/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/3Sum.py) | :heavy_check_mark: | |
| BLIND   | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SearchInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | :heavy_check_mark: | MAX ➡️ Instantiate two variables, one to hold the current sum and the other to hold the max sum. Use the max built-in function to update the vairables and after the loop return the max sum. The current max will be calculated by comparing the current value and the sum of the current sum and the value. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) |
| BLIND   | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/MaximumProductSubarray.py) | :heavy_check_mark: | |
| BLIND   | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/FindMinimumInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/ContainsDuplicate.py) | :heavy_check_mark: | SET ➡️ Instantiate a set. Iterate through the array and check if current num is in the set. If it is, return True because it contains a duplicate. If it is not in the set, add it to the set and the loop continues. If the loop finishes, return False because we have not found a duplicate value. NOTE: There is also a one line solution. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |
| BLIND   | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ProductOfArrayExceptSelf.py) | :heavy_check_mark: | ARRAY ➡️ Instantiate a result array with 1s, it will be the length of the given array. Start from the beginning of res and calculate the prefix (set to 1), set the res with the calculated prefix (prefix multiplied by nums[i]). Start from the end of res and calculate the postfix (set to 1, calculated by postfix multiplied by nums[i]), the res will be given as res multiplied by the postfix. Return the res array. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) if output array doesn't count as memory |

## Strings
### Strings Syntax

### Strings Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 6.1     | [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/StringToIntegerATOI.py) | 🟥 | X ➡️ Not solved, but it is in the hackathon time frame. |
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

### Linked Lists Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 7.1     | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/MergeTwoSortedLists.py) | ✔️ | DUMMY NODE AND COMPARISON ➡️ Instantiate a dummy node. Instantiate a tail node that will hold dummy node. Start a while loop that will continue as long as there is at least one of list1 or list2. Compare the values of list1 and list2 and append them respectively to the tail.next. Once the while loop ends, create an if statement check to see if there are still any nodes in the lists. If there is, append them to the tail.next at the end. Finally, return the dummy.next node. <br/>Time Complexity: O(n + m)<br/>Space Complexity: O(1)  |
| 7.2     | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/ReverseLinkedList.py) | ✔️ | PREVIOUS AND CURRENT POINTERS ➡️ Instantiate a previous and current pointer to None and head respectively. Start a while loop which continues while we have a current. Add current.next to a temp variable. Then set current.next to the previous node. Set the previous node to the current node and then set the current node to the temp next variable. The temp saves the next value, we do the direction change and then shift our previous and current pointers. Once out of the while loop, we can return the previous node and the linked list is changed directionally. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1)  |
| 7.3     | [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Medium/LinkedListCycleII.py) | ✔️ | SET ➡️ You can use a set to keep track of nodes that we have gone through, however this takes up extra memory and is not the most optimal solution. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) <br/><br/> HARE AND TORTOISE ➡️ Create a slow and fast pointer, the slow pointer increments by one and the fast pointer increments by two. Once the two pointers are the same, create a third pointer that starts at head. Take the new pointer and the old fast pointer and increment them by one until they are the same. Once they are the same, return the node. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1)  |
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
| BLIND   | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/LinkedListCycle.py) | ✔️ | SET ➡️ You can use a set to keep track of nodes that we have gone through, however this takes up extra memory and is not the most optimal solution. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) <br/><br/> HARE AND TORTOISE ➡️ Create a slow and fast pointer, the slow pointer increments by one and the fast pointer increments by two. Once the two pointers are the same, return True. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) |
| BLIND   | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard) 🔴 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Hard/MergeKSortedLists.py) | &#9744; | Skipped |
| BLIND   | [143. Reorder List](https://leetcode.com/problems/merge-k-sorted-lists/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Medium/ReorderList.py) | ✔️ | |





## Stacks and Queues
### Stacks and Queues Syntax

### Stacks and Queues Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 8.1     | [165. Min Stack](https://leetcode.com/problems/min-stack/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Stacks/MinStack.py) | ✔️ | IMPLEMENTATION ➡️ This question is just implementation from scratch with an extra function to retrieve the minimum. <br/>Time Complexity: O(1) for all operations |
| 8.6     | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Stacks/MinStack.py) | ✔️ | BFS ➡️ Instantiate a queue, this can be done using the collections library or by simply using .pop(0) to remove from the front. While we have a full queue, we want to for loop in the range of the length of the queue, so that we visit all of the nodes on that level. We pop from the front, add the value to the list and add the left and right child nodes to the queue. After the for loop, if the level array is not empty, we append it to the result array. The while loop restarts, and continues as long as the child nodes get added. Return the result array <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |





## Binary Trees
### Binary Trees Syntax

### Binary Trees Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 9.1     | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Binary%20Trees/Easy/BalancedBinaryTree.py) | ✔️ | RECURSIVE DFS ➡️ Create a recursive DFS function. The base case will be when the node is null, you will return [True, 0] because it has a height of zero and it is balanced, therfore True. Then we will check the left and right child nodes, by calling the DFS function again. This will return the tuple. When we have the left and right tuple, we can check that it is balanced. To be balanced left and right must both be True, and the height must be less than or equal to one. We return a tuple [balanced, 1 + max(left, right)]. After creating the function, we call the DFS function on the root and return the boolean at position 0. Simply put we are recursively traversing to the bottom of the tree to its last nodes and then traversing back up, returning the height and the boolean. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |





## Heaps
### Heaps Syntax

### Heaps Problems


## Searching
### Searching Syntax

### Searching Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 11.4     | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy) 🟢 | [Code]() | ✔️ |  ➡️  <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |
| 11.8     | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) 🟡 | [Code]() | ✔️ |  ➡️  <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |


