# Multiply Two Arbitrary-Precision Integers Problem

# There are m partial products, each with at most n + 1 digits. We perform O(1) 
# operations on each digit in each partial product, so the time complexity is O(nm).
def multiply(num1, num2):
    # Using XOR to set the signs, we set sign = -1 if num1 XOR num2 is true
    # else we set sign equal to 1
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    
    # We set the values to absolute because we already have the sign from above
    num1[0], num2[0] = abs(num1[0]) , abs(num2[0])

    # Instantiate an array that will be the length of the product
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeroes
    result = result[next((i for i, x in enumerate(result)
                            if x != 0), len(result)):] or [0]
    
    return [sign * result[0]] + result[1:]

print("Multiply Two Arbitrary-Precision Integers")

print(multiply([1,0,1],[1,0,1]))