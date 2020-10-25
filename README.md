# Python-Interview-Preparation-
This is a repository to store all of the solutions to every Python interview question that I do.

# Table of Contents
* [Elements of Programming Interviews in Python](#elements-of-programming-interviews-in-python)
	* Arrays
		* [Arrays Syntax](#arrays-syntax)
		* [Problems](#problems)
			* [The Dutch National Flag Problem](#the-dutch-national-flag-problem)

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
#### [The Dutch National Flag Problem](https://github.com/milosarsik/Python-Interview-Preparation-/blob/main/Elements%20of%20Programming%20Interviews%20in%20Python/Arrays/5.1dutchflagpartition.py)
