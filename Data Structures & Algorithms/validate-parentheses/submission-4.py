class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        stack = list()
        for i in s:
            if i in paren:
                stack.append(i)
            elif stack and i == paren[stack.pop()]:
                continue
            else:
                return False
        return not stack

        