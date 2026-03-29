class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            sum_ = a^b
            carry = (a&b) << 1
            a = sum_ & mask
            b = carry & mask
        return  a if a <= max_int else ~(a ^ mask)

        

        