class Solution:
    def reverseBits(self, n: int) -> int:
        y = 0
        for i in range(32):
            x = (n >> i) & 1
            y += x << (31 - i)
        
        return y
        