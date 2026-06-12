"""
I am really stupid as this problem proves. The solutions appear simple once they are shown.
The idea is no different than any other problem. The solution is not to append the 
answer to be directly index it. 
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for j, ct in enumerate(temperatures):
            while stack and stack[-1][1] < ct:
                i, pt = stack.pop()
                ans[i] = j - i
            stack.append((j, ct))
            print(stack)
        
        return ans
