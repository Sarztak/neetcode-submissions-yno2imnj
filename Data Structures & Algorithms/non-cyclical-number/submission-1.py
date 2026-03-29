class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(num):
            sum_ = 0
            while num: 
                sum_ += (num % 10)**2
                num = num // 10
            return sum_
        
        nums = []
        while True:
            n = get_sum(n)
            if n == 1:
                return True
            if n not in nums:
                nums.append(n)
            else:
                return False


