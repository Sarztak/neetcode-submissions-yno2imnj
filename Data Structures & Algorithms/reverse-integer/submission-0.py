class Solution:
    def reverse(self, x: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        min_int = 0x8FFFFFFF
        r = str(x)
        r = r[::-1]
        r = int(r) if r[-1] != '-' else -int(r[:-1])
        return r if -2**31 <= r <= (2**31 - 1) else 0 