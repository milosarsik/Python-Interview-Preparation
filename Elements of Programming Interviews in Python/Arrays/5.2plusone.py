# 5.2 Increment an Arbitrary-Precision Integer Problem

# The time complexity is O(n), where n is the length of A. The space complexity is O(1)

def plus_one(A):
    # Instead of len(A)-1
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i], A[i-1] = 0 , A[i-1] + 1
        elif A[i] != 10:
            break
    # There is a carry-out, so we need one more digit to store the result
    # A slick way to do this is to append a 0 at the end of the array,
    # and update the first entry to 1.
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    
    return A

# Test code
print("Increment an Arbitrary-Precision Integer")

list = [9, 9, 9, 9]

print(plus_one(list))
