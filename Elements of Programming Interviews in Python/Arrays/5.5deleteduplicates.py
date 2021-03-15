# Advancing Through An Array Problem

# 
def delete_duplicates(A):
    if not A:
        return 0
    
    count = 1
    for i in range(1, len(A)):
        if A[count - 1] != A[i]:
            A[count] = A[i]
            count += 1
    
    return count

   

print("Delete Duplicates from a Sorted Arary")

A = [2,3,5,5,7,11,11,11,13]
print(delete_duplicates(A))
print(A)