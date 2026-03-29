class Solution:
    def myPow(self, x: float, n: int) -> float:
        y = 1
        if n > 0:
            for _ in range(n):
                y *= x
        else:
            for _ in range(-n):
                y /= x
        return y
