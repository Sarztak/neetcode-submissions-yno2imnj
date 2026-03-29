class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(p):
            count = 0
            for i in range(32):
                if (p >> i) & 1:
                    count += 1
            return count
        
        return [helper(i) for i in range(n + 1)]
