"""
"""

def mySqrt(self, x: int) -> int:
    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <= x:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1
