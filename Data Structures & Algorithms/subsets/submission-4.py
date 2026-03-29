class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [[]]
        for n in nums:
            k = len(stack)
            for i in range(k):
                x = stack[i] + [n]
                stack.append(x)
        return stack
        