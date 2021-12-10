"""

"""

def myPow(self, x: float, n: int) -> float:
    def myHelper(x, n):
        if x == 0: 
            return 0
        if n == 0:
            return 1

        res = myHelper(x * x, n //2)
        return x * res if n%2 else res

    res = myHelper(x, abs(n))
    return res if n >= 0 else 1/res
