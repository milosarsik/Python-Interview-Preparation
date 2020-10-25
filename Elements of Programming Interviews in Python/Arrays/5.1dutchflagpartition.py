# 5.1 - The Dutch National Flag Problem

# The problem is trivial to solve with O(n) additional space where n is the length of A.
# We form three lists, namely, elements less than the pivot, elements equal to the pivot, and elements
# greater than the pivot. Consequently, we write these values into A. The time complexity is O(n).
# We can avoid using O(n) additional space at the cost of increased time complexity as follows. In
# the first stage, we iterate through A starting from index 0, then index 1, etc. In each iteration, we
# seek an element smaller than the pivot-as soon as we find it, we move it to the subarray of smaller
# elements via an exchange. This moves all the elements less than the pivot to the start of the array.
# The second stage is similar to the first one, the difference being that we move elements greater than
# the pivot to the end of the array. 

# The additional space compllexity is O(1), but the time complexity is O(n^2)
# To improve the time complexity, we can make a single pass and move all the 
# elements less that the pivot to the beginning. In the second pass ew move the larger
# elements to the end. It is easy to perform each pass in a single iteration, moving
# out-of-place elemets as soon as they are discovered
def dutch_flag_partition_1(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for a smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
    # Look for a larger element. Stop when we reach an element less than
    # pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

# The time complexity is O(n) and the space complexity is O(1)
def dutch_flag_partition_2(pivot_index, A) :
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    
    # Second pass; group elements larger than pivot
    larger = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger] , A[i]
            larger -= 1

# The algorithm we now present is similar to the one sketched above. The main difference is that
# it performs classification into elements less than, equal to, and greater than the pivot in a single
# pass. This reduces runtime, at the cost of a trickier implementation. We do this by maintaining four
# subarrays: bottom (elements less than pivot), middle (elements equal to pivot), unclassified, and top
# (elements greater than pivot). Initially, all elements areinunclassified. We iterate through elements
# in unclassified, and move elements into one of bottom, middle, and top groups according to the relative
# order between the incoming unclassified element and the pivot.
# Each iteration decreases the size of unclassified by 1, and the time spent within each iteration is O(1),
# implying the time complexity is O(n). The space complexity is clearly 0(1).

def dutch_flag_partition_3(pivot_index, A) :
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # botton group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element
    while equal < larger:
        # A[equal] is the incoming inclassified element,
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller , equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

# Test code
print("The Dutch National Flag Problem")

list = [3,2,1,5,5,3,1,2,3,5,1]
pivot_index = 0

dutch_flag_partition_3(pivot_index, list)

print(list)