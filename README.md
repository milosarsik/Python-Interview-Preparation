# Python-Interview-Preparation-
This is a repository to store all of the solutions to every Python interview question that I do aswell as contains the basics of Python and algorithms.

# Table of Contents
* [Algorithms and Data Structures for Beginners](#algorithms-and-data-structures-for-beginners)	
* [Advanced Algorithms](#advanced-algorithms)
 	* [Advanced Arrays](#advanced-arrays)
 	 	* [Kadane's Algorithm](#kadanes-algorithm)
 	 	* [Sliding Window Fixed Size](#sliding-window-fixed-size)
 	 	* [Sliding Window Variable Size](#sliding-window-variable-size)
 	 	* [Two Pointers](#two-pointers)
 	 	* [Prefix Sums](#prefix-sums)
	* [Advanced Linked Lists](#advanced-linked-lists)
	 	* [Fast and Slow Pointers](#fast-and-slow-pointers)
	* [Advanced Trees](#advanced-trees)
		* [Trie](#trie)
		* [Union Find](#union-find)
		* [Segment Tree](#segment-tree)
		* [Iterative DFS](#iterative-dfs)
	* [Heaps](#aheaps)
		* [Two Heaps](#two-heaps)
	* [Backtracking](#backtracking)
		* [Subsets](#subsets)
		* [Combination](#combination)
		* [Permutations](#permutations)
	* [Advanced Graphs](#advanced-graphs)	
		* [Dijkstra's](#dijkstra's)
		* [Prim's](#prim's)
		* [Kruskal's](#kruskal's)
		* [Topological Sort](#topological-sort)
	* [Advanced Dynamic Programming](#advanced-dynamic-programming)
		* [0/1 Knapsack](#0/1-knapsack)
		* [Unbounded Knapsack](#unbounded-knapsack)
		* [LCS](#lcs)
		* [Palindromes](#palindromes) 	 	 	 
* [Python Basics](#python-basics)
	* [Variables](#variables)
	* [Math](#math)
	* [If Statements](#if-statements)
	* [Loops](#loops)
	* [](#)
* [Elements of Programming Interviews in Python](#elements-of-programming-interviews-in-python)
	* [Arrays](#arrays)
		* [Arrays Syntax](#arrays-syntax)
		* [Arrays Problems](#arrays-problems)
	* [Strings](#strings)
		* [Strings Syntax](#strings-syntax)
		* [Strings Problems](#strings-problems)
	* [Linked Lists](#linked-lists)
		* [Linked Lists Implementations](#linked-lists-implementations)
		* [Linked Lists Problems](#linked-lists-problems)
	* [Stacks and Queues](#stacks-and-queues)
		* [Stack Implementation](#stack-implementation)
		* [Queue Implementation](#queue-implementation)
		* [Stacks and Queues Problems](#stacks-and-queues-problems)
	* [Binary Trees](#binary-trees)
		* [Binary Trees Syntax](#binary-trees-syntax)
		* [Binary Trees Problems](#binary-trees-problems)
	* [Searching](#searching)
		* [Searching Syntax](#searching-syntax)
		* [Searching Problems](#searching-problems)
	* [Primitive Types](#primitive-types) 
		* [Primitive Types Syntax](#primitive-types-syntax)
		* [Primitive Types Problems](#primitive-types-problems)

# Algorithms and Data Structures for Beginners
## Arrays ()
### RAM
Ram is measured in bytes. Byte is 8 bits. A bit is the position that can store a digit, the restriction is that it can be a zero or a one. 
RAM stores the values, but every value is stored at a distint location called an address. Arrays are going to be contiguous, meaning that the values stored in RAM are going to be next to eachother. THe address will increment by 4 because intergers are 4 bytes. However, if we store ASCII values, they will increment by 1, because it is 1 byte.
Increment the address by the size of the value.

### Static Arrays
Static arrays are fixed size arrays. Python doesnt offer static, it has dynamic arrays as default. 
Inserting at the end is efficient, but adding at the front or the middle, is not efficient at all. We must shift all of the values to the right. If we add a the front, this is a O(n) time complexity because we are shifting all of the elements to the right.

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| r/w i-th element 	| O(1)  	  |
| Insert/Remove end 	| O(1) 		  |
| Insert middle 	| O(n) 		  |	
| Remove middle		| O(n) 		  |

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|      ✔️      | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=DEJAZBq0FDA&t=1s&ab_channel=NeetCode) |
|      ✔️      | [27. Remove Element](https://leetcode.com/problems/remove-element/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=Pcd1ii9P9ZI&ab_channel=NeetCode) |

### Dynamic Arrays
Dynamic arrays resize themselves when more space is requested, for example if we wish to add to the end middle or beginning of the array, but we do not have enough space in the current array.

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| r/w i-th element 	| O(1)  	  |
| Insert/Remove end 	| O(1) 		  |
| Insert middle 	| O(n) 		  |	
| Remove middle		| O(n) 		  | 

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|      ✔️      | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) 🟢 | [Add Code]() | | [Add Video]() |

### Stacks
The stack is nothing but an array. LIFO - last in, first out data structure. 

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| Push			| O(1)  	  |
| Pop		 	| O(1) 		  |
| Peek/Top	 	| O(1) 		  |

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|      ✔️      | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode) |
|      ✔️      | [155. Min Stack](https://leetcode.com/problems/min-stack/) 🟡 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=qkLl7nAwDPo&ab_channel=NeetCode) |
|      ✔️      | [682. Baseball Game](https://leetcode.com/problems/baseball-game/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=Id_tqGdsZQI&ab_channel=NeetCode) |

## Linked Lists
### Singly Linked Lists
A linked list is made up of a chain of nodes. These nodes contain a value and pointer to the next node. A chain of nodes is called a singly linked list becaue every next pointer points to the address of the next node. 

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| r/w i-th element 	| O(n)  	  |
| Insert/Remove end	| O(1)  	  |
| Insert/Remove middle	| O(n)/O(1) 	  |

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|      ✔️      | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode) |
|      ✔️      | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=G0_I-ZF0S38&ab_channel=NeetCode) |

### Doubly Linked Lists
Exact same as singly linked lists but, now a node also stores a refrence to the previous node aswell as the next node. 

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| r/w i-th element 	| O(n)  	  |
| Insert/Remove end	| O(1)  	  |
| Insert/Remove middle	| O(n)/O(1) 	  |

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|     ❌      | [707. Design Linked List](https://leetcode.com/problems/design-linked-list/) 🟡 | [Add Code]() | | [Add Video]() |
|     ❌      | [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/) 🟡 | [Add Code]() | | [Add Video]() |

### Queues
Queues are similar to stacks. FIFO - first in, first out data structure. Supports two operations, enqueue and dequeue. Elements are added from the end and removed from the front.

| 	Operation 	| Time Complexity |
|-----------------------|:---------------:|
| Enqueue	 	| O(1)  	  |
| Dequeue 		| O(1)  	  |

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|     ❌      | [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=rW4vm0-DLYc&ab_channel=NeetCode) |
|     ❌      | [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) 🟢 | [Add Code]() | | [Add Video]() |

## Recursion
### Factorial
A factorial, would be a good introduction to recursion. This is called a one-branch recursion. To notice a recursion problem, we have to find if there are sub-problems. The equation for a factorial is as follows: `n! = n * (n - 1)!`. </br>
There is no benefit to using recursion for a factorial problem. However it gives you a good visualization of how recursion works. Here is the code solution for a factorial and the decision tree:
```python
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)
    
5!	
  \		24	->	120	
   4!		|-
     \		6
      3!	|-
        \	2
	 2!	|-
	   \	1
	    1!
```

Recursion is not recommended because we are using O(n) memory, and we can do this in constant memory using a while loop like so:
```python
int res = 1

while n < 1:
    res = res * n
    n -= 1
	
return res
```

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|     ❌      | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=G0_I-ZF0S38&ab_channel=NeetCode) |

### Fibonacci
This is an example of two-branch recursion. Here is the implementation:
```python
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 1)
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|      ❌     | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) 🟢 | [Add Code]() | | [Video](https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=2s&ab_channel=NeetCode) |
|      ❌     | [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) 🟢 | [Add Code]() | | [Video]() |




























# Advanced Algorithms
## Advanced Arrays
### Kadane's Algorithm
...
#### Suggested Problems
|  Completed  | Problem |  Solution   | Notes |  Video Walkthrough  | 
|:-----------:|---------|:-----------:|-------|:-------------------:|
|     ❌      | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 🟡 | [Code]() | | [Video]() |
|     ❌      | [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) 🟡 | [Code]() | | [Video]() |
|     ❌      | [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) 🟡 | [Code]() | | [Video]() |




































# Python Basics
## Variables
### Dynamically Typed 
Python variables are dynamically typed. This means that the interpreter assigns variables a type at **runtime** based on the variable's value at the time.
`None` is equivalent to `null`, there is no value when a variable is set to `None`.
```python
n = 0
print('n =', n)
>>> n = 0

n = "abc"
print('n =', n)
>>> n = abc

n = 4
n = None
print("n =", n)
>>> n = None
```

### Multiple Assignments
Use this shorthand notation to assign multiple variables, it makes the look code cleaner.
```python
n, m = 0, "abc"
n, m, z = 0.125, "abc", False
```

### Incrementing 
There is no `++` incrementing in Python!
```python
n = n + 1 # good
n += 1    # good
n++       # bad
```

If you wish to know more about Pythons built-in types, visit the documentation page [here](https://docs.python.org/3/library/stdtypes.html#)

## Math
### Division
Division is python is decimal by default. Notice that we can use a double slash to round down. Division with negative numbers will result in rounding down, whereas in most languages it will be rounded closer to zero. If you want to round closer to zero, use decimal division and then convert the value 
to an integer
```python
print(5 / 2)
>>> 2.5

print(5 // 2)
>>> 2

# Careful here with negative division
print(-3 // 2)
>>> -2

# Workaround to round closer to zero
print(int(-3 / 2))
>>> -1
```

### Modulo
Modding is similar to most languages, expect when we are modding negative values. To be consistent with other languages modulo, use a module. 
```python
print(10 % 3)
>>> 1

print(-10 % 3)
>>> 2

# To be consistent with other languages modulo
import math
from multiprocessing import heap
print(math.fmod(-10, 3))
>>> -1
```

### More Math 
#### Useful Functions
```python
print(math.floor(3 / 2))
>>> 1

print(math.ceil(3 / 2))
>>> 2

print(math.sqrt(2))
>>> 1.4142135623730951

print(math.pow(2, 3))
>>> 8
```

#### +/- Infinity
First two functions create max/min integers. Python numbers are infinite, so they never overflow. However, they will always be less that infinity!
```python
float("inf")
float("-inf")

print(math.pow(2, 200))
>>> 1.6069380442589903e+60

print(math.pow(2, 200) < float("inf"))
>>> True
```

## If Statements
If-statements do not need parentheses or curly braces.
```python
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2
```
Parentheses are only needed for multi-line conditions.
```python
n, m = 1, 2
if ((n > 2 and 
    n != m) or n == m):
    n += 1
```

## Loops
Remember that loops are inclusive, if you `range(5)` it will print from 0 to 5. 
### While Loops
```python
n = 0
while n < 5:
    print(n)
    n += 1
>>> 0 1 2 3 4
```

### For Loop
#### Looping from `i = 0` to `i = 4`
```python
for i in range(5):
    print(i)
>>> 0 1 2 3 4
```
#### Looping from `i = 2` to `i = 5`
```python
for i in range(2, 6):
    print(i)
>>> 2 3 4 5
```
#### Looping from `i = 5` to `i = 2` 
```python
for i in range(5, 1, -1):
    print(i)
>>> 5 4 3 2
```

If you wish you wish to know more about Pythons control flow, visit the documentation page [here](https://docs.python.org/3/tutorial/controlflow.html)





# Elements of Programming Interviews in Python
## Arrays

Array problems often have simple brute force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity to O(1).
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
```python
list = [1, 2, 3, 4, 5]

print(list)
>>> [1, 2, 3, 4, 5]

# Initialize a list of size n with default value of 1
n = 5
list = [1] * n

print(list)
>>> [1, 1, 1, 1, 1]

print(len(list))
>>> 5

list = [i for i in range(5)]

print(list)
>>> [0, 1, 2, 3, 4]
```

#### Indexing
```python
list[0] = 0
list[3] = 0
print(list)
>>> [0, 2, 3, 0, 5]

# Careful: -1 is not out of bounds, it's the last value
list = [1, 2, 3]

print(list[-1])
>>> 3

print(arr[-2])
>>> 2
```

#### Slicing
If we have `A = [1, 6, 3, 4, 5, 2, 77]`, these are the following slicing operations we can perform. <br/>
* `A[2:4]` is [3, 4]
* `A[2:]` is [3, 4, 5, 2, 77] 
* `A[:4]` is [1, 6, 3, 4] 
* `A[:-1]` is [1, 6, 3, 4, 5, 2] 
* `A[-3:]` is [5, 2, 7] 
* `A[-3:-1]` is [5, 2] 
* `A[1:5:2]` is [6, 4] 
* `A[5:1:-2]` is [2, 4]
* `A[::-1]` is [7, 2, 5, 4, 3, 6, 1] (reverses list) 

Slicing can also be used to rotate a list `A[k:l] + A[:k]` rotates A by k to the left. It can also be used to create a copy: `B = A[:]` does a (shallow) copy of A into B.
```python
arr = [1, 2, 3, 4]
print(arr[1:3])
>>> [2, 3]

# Similar to for-loop ranges, last index is non-inclusive, but no out of bounds error
print(arr[0:4])
>>> [1, 2, 3, 4]

print(arr[0:10])
>>> [1, 2, 3, 4]
```

#### Basic Operations
```python
len(list)
list.append(42)
list.remove(42)
list.insert(3, 28)
list.reverse()
list.sort()
list.sort(reverse=True)

list = ["bob", "alice", "jane", "doe"]
list.sort()

print(list)
>>> ["alice", "bob", "doe", "jane"]

# Custom sort (by length of string)
list.sort(key=lambda x: len(x))

print(list)
>>> ["bob", "doe", "jane", "alice"]
```

#### Looping Through Array
```python
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(nums[i])
>>> 1 2 3

# Without index
for n in nums:
    print(n)
>>> 1 2 3

# With index and value
for i, n in enumerate(nums):
    print(i, n)
>>> 0 1
>>> 1 2
>>> 2 3

# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
>>> 1 2
>>> 3 4
>>> 5 6
```

#### 2-D Lists
```python
list = [[0] * 4 for i in range(4)]

print(list)
print(arr[0][0], arr[3][3])
>>> [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# This won't work as you expect it to
arr = [[0] * 4] * 4
```

#### Value Exists
```python
a in list
```

#### Copying (Shallow & Deep)
```python
listB = listA
```
This will make listB point to listA. They will have the same values.

##### Shallow Copy
A shallow copy creates a new object which stores the reference of the original elements. <br/>
So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.
```python
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```
Changes in the old_list, will appear in the new_list. Changes in the new_list will not appear in the old_list.

##### Deep Copy
A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.
```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```
In the above program, we use deepcopy() function to create copy which looks similar. However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.

#### Key Methods
* `min(A)`, 
* `max(A)`, 
* binary search for sorted lists (`bisect.bisect(A,6)`, `bisect.bisect-left(A,6)`, and `bisect.bisect_right(A,6)`), 
* `A.reverse()` (in-place)
* `reversed(A)` (returns an iterator), 
* `A.sort()` (in-place), 
* `sorted(A)` (returns a copy), 
* `del A[i]` (deletes the i-th element), `and 
* del A[i: j]` (removes the slice)

#### List Comprehension
Python provides a feature called list comprehension that is a succinct way to create lists. A list comprehension consists of:
1. an input sequence 
2. an iterator over the input sequence
3. a logical condition over the iterator (this is optional)
4. an expression that yields the elements of the derived list. 

`[x**2 for x in range(6)]` yields `[0, 1, 4, 9, 16, 25]` <br/>
`[x**2 for x in range(6) if x%2 == 0]` yields `[0, 4, 16]` <br/>

List comprehension supports multiple levels of looping. This can be used to create the product of sets, e.g., if `A = [1, 3, 5]` and `B = ['d', 'b']`, then `[(x, y) for x in A for y in B]` creates `[(1, 'a'), (1, 'b'), (3, 'a'), (3, 'b'), (5, 'a'), (5, 'b')]`. <br/>

It can also be used to convert a 2D list to a 1D list, e.g., if `M = [['a', 'b', 'c'], ['d', 'e','f']]`, `x for row in M for x in row` creates `['a', 'b', 'c', 'd', 'e', 'f ']`. <br/>

Two levels of looping also allow for iterating over each entry in a 2D list, e.g., lf A = [[1, 2, 3] , [4, 5, 6]] then `[[x**2 for x in row] for row in M]` yields [[1, 4, 9], [16, 25, 36]]. <br/>

As a general rule, it is best to avoid more than two nested comprehensions, and use conventional nested for loops-the indentation makes it easier to read the program.

### Arrays Problems
|  Problem  | LeetCode |  Solution   |  Completed  | Notes |  Video Walkthrough  | 
|:---------:|----------|:-----------:|:-----------:|-------|:-------------------:|
| 5.1     | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SortColors.py) | ✔️ | PARTITION/PIVOT POINT ➡️ Instantiate a left and right pointer and a pivot point i. While i <= r, if nums[i] is zero do a swap with the left and the pivot point, if nums[i] is 2 do a swap with the right and pivot point, but do not increment the pivot point (that is why we decrement the pivot point in the if statment). Simply put we are breaking up the array into 3 section, 0, 1 and 2. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1)
| 5.2     | []() | | &#9744; | |
| 5.3     | []() | | &#9744; | |
| 5.4     | [55. Jump Game](https://leetcode.com/problems/jump-game/) | | &#9744; | |
| 5.5     | [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | | &#9744; | |
| 5.6     | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/121.%20BestTimeToBuyAndSellStock.py) | :heavy_check_mark: | Use a sliding window technique, have a left and right pointer beginning next to eachother. Window size depends on if right is less than left. Keep track of the maximum profit. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) | [Video](https://www.youtube.com/watch?v=1pkOgXD63yU&ab_channel=NeetCode) |
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
| 5.18    | [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SpiralMatrix.py) | 🟥 | X ➡️ Not solved, but it is in the hackathon time frame. |
| 5.19    | [48. Rotate Image](https://leetcode.com/problems/rotate-image/) | | &#9744; | |
| 5.20    | [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | | &#9744; | |
| BLIND   | [1. Two Sum](https://leetcode.com/problems/two-sum/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/1.%20TwoSum.py) | :heavy_check_mark: | Use a **hashmap** data structure to keep track of the value and indice. Calculate the complement and check if it exists in the **hashmap**. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) | [Video](https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode) |
| BLIND   | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ContainerWithMostWater.py) | :heavy_check_mark: | |
| BLIND   | [15. 3Sum](https://leetcode.com/problems/3sum/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/3Sum.py) | :heavy_check_mark: | |
| NC.io   | [27. Remove Element](https://leetcode.com/problems/remove-element/) 🟢 | [Code](//) | :heavy_check_mark: | Max <br/>Time Complexity: //<br/>Space Complexity: // |
| BLIND   | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/SearchInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/MaximumSubarray.py) | :heavy_check_mark: | Max <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) |
| BLIND   | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/125.%20ValidPalindrome.py) | :heavy_check_mark: | Use **left and right pointer** technique. Update left and right until each one points at an alphanum. A global while loop is needed to ensure that the two pointers do not cross. Then compare left and right, continue until left >= right. There are upper and lower case letters, therefore use a **.lower()** method to take care of that. There are two more solutions to this problem in the code. Make sure to make your own alphanum function, or write an algorithm using built-in methods. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) | [Video](https://www.youtube.com/watch?v=jJXJ16kPFWg&ab_channel=NeetCode) |
| BLIND   | [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/MaximumProductSubarray.py) | :heavy_check_mark: | |
| BLIND   | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/FindMinimumInRotatedSortedArray.py) | :heavy_check_mark: | |
| BLIND   | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/217.%20ContainsDuplicate.py) | :heavy_check_mark: | Use a **set()** data structure to solve this problem. It is a built-in data type in Python used to store collections of data. <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) | [Video](https://www.youtube.com/watch?v=3OamzN90kPg&t=342s&ab_channel=NeetCode)|
| BLIND   | [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Medium/ProductOfArrayExceptSelf.py) | :heavy_check_mark: | ARRAY ➡️ Instantiate a result array with 1s, it will be the length of the given array. Start from the beginning of res and calculate the prefix (set to 1), set the res with the calculated prefix (prefix multiplied by nums[i]). Start from the end of res and calculate the postfix (set to 1, calculated by postfix multiplied by nums[i]), the res will be given as res multiplied by the postfix. Return the res array. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) if output array doesn't count as memory |
| BLIND   | [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Arrays/Easy/242.%20ValidAnagram.py) | ✔️ | Use the **hashmap** data structure to count each character in both strings, then compare the lengths of each element, or just compare the hashmaps. One liner solution is to sort the strings and compare, or use a **Counter()** and then compare. Go to the code to view the time and space complexities. | [Video](https://www.youtube.com/watch?v=9UtInBqnCgA&ab_channel=NeetCode) |

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
| BLIND   | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/GroupAnagrams.py) | ✔️ | |
| BLIND   | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) 🔴 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Hard/MinimumWindowSubstring.py) | ✔️ | |
| BLIND   | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/LongestRepeatingCharacterReplacement.py) | ✔️ | |
| BLIND   | [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Strings/Medium/PalindromicSubstrings.py) | ✔️ | |
| BLIND   | [0. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Unknown) ⚫ | [Code]() | &#9744; | |


## Linked Lists
### Linked Lists Implementations
In a **Singly Linked List** implementation, each node only points to one other node ahead of it. Below is the implementation of a linked list:
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Initialize the list with a 'dummy' node which makes removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()
```

In a **Doubly Linked List** implementation, each node points to the next node and the previous node. Below is the implementation of a duobly linked list:
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()
```

### Linked Lists Problems
|  Problem  | LeetCode |  Solution   |  Completed  | Notes |  Video Walkthrough  |
|:---------:|----------|:-----------:|:-----------:|-------|:-------------------:|
| 7.1     | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/21.%20MergeTwoSortedLists.py) | ✔️ | Instantiate a dummy and a tail node that will hold dummy node at the start. Use a while loop that will continue as long as there is at least one of list1 or list2. Compare the values of list1 and list2 and append them respectively to the tail.next. Once the while loop ends, create an if statement check to see if there are still any nodes in the lists. If there is, append them to the tail.next at the end. Finally, return the dummy.next node. <br/>Time Complexity: O(n + m)<br/>Space Complexity: O(1) | [Video](https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode) |
| 7.2     | [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Linked%20Lists/Easy/206.%20ReverseLinkedList.py) | ✔️ | Use the **two pointer** technique. Instantiate a previous and current pointer to None and head respectively. Start a while loop which continues while we have a current. Add current.next to a temp variable. Then set current.next to the previous node. Set the previous node to the current node and then set the current node to the temp variable. The temp saves the next value, we do the direction change and then shift our previous and current pointers. Once out of the while loop, we can return the previous node and the linked list is changed directionally. <br/>Time Complexity: O(n)<br/>Space Complexity: O(1) | [Video](https://www.youtube.com/watch?v=G0_I-ZF0S38&t=2s&ab_channel=NeetCode) |
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
### Stack Implementation
```python
# Implementing a stack is trivial using a dynamic array
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()
```
### Queue Implementation 
```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    # Implementing this with dummy nodes would be easier!
    def __init__(self):
        self.left = self.right = None
    
    def enqueue(self, val):
        newNode = ListNode(val)

        # Queue is non-empty
        if self.right:
            self.right.next = newNode
            self.right = self.right.next
        # Queue is empty
        else:
            self.left = self.right = newNode

    def dequeue(self):
        # Queue is empty
        if not self.left:
            return None
        
        # Remove left node and return value
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = None
        return val

    def print(self):
        cur = self.left
        while cur:
            print(cur.val, ' -> ', end ="")
            cur = cur.next
        print() # new line
```

### Stacks and Queues Problems
|  Problem  | LeetCode |  Solution   |  Completed  | Notes | Video Walkthrough |
|:---------:|----------|:-----------:|:-----------:|-------|-------------------|
| 8.1     | [165. Min Stack](https://leetcode.com/problems/min-stack/) (Medium) 🟡 | [Code](https://www.youtube.com/watch?v=qkLl7nAwDPo&ab_channel=NeetCode) | ✔️ | Use two **stacks** one to store the values, the other one to store the minimum value at every new value added. <br/>Time Complexity: O(1) for all operations | [Video](https://www.youtube.com/watch?v=qkLl7nAwDPo&ab_channel=NeetCode) |
| 8.6     | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium) 🟡 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Stacks/MinStack.py) | ✔️ | BFS ➡️ Instantiate a queue, this can be done using the collections library or by simply using .pop(0) to remove from the front. While we have a full queue, we want to for loop in the range of the length of the queue, so that we visit all of the nodes on that level. We pop from the front, add the value to the list and add the left and right child nodes to the queue. After the for loop, if the level array is not empty, we append it to the result array. The while loop restarts, and continues as long as the child nodes get added. Return the result array <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |
| BLIND   | [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Stacks/Easy/20.%20ValidParentheses.py) | ✔️ | Push opening brace on stack, pop if matching close brace by checking the hashmap, at the end if the stack is empty, return true. Use hashmap for the closed to open parentheses <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) | [Video](https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode) |





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
| 11.4     | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Searching/Easy/Sqrt(x).py) | ✔️ | BINARY SEARCH ➡️ Use a binary searchy, find the mid point, square it and compare it to the k. <br/>Time Complexity: O(log(n))<br/>Space Complexity: O(1) |
| 11.8     | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) 🟡 | [Code]() | &#9744; |  ➡️  <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |






## Hash Tables

### Hash Tables Syntax

### Hash Tables Problems
| Problem | LeetCode | Solution  | Completed | Notes |
|---------|----------|-----------|-----------|-------|
| 12.2     | [383. Ransom Note](https://leetcode.com/problems/ransom-note/) (Easy) 🟢 | [Code](https://github.com/milosarsik/Python-Interview-Preparation/blob/main/LeetCode/Hash%20Tables/Easy/RansomNote.py) | ✔️ | HASH TABLE ➡️ First solution using two hashtables <br/>Time Complexity: O(n + m)<br/>Space Complexity: O(n + m) <br/><br/> HASH TABLE ➡️ Second solution using one hashtable and updating frequencies <br/>Time Complexity: O(n)<br/>Space Complexity: O(n)|
| 12.X     | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) (Easy) 🟢 | [Code]() | ✔️ |  ➡️  <br/>Time Complexity: O(n)<br/>Space Complexity: O(n) |





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
```python
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
