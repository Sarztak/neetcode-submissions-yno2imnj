class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            x = (n >> i) & 1
            res = res + (x << (31 - i))
        return res