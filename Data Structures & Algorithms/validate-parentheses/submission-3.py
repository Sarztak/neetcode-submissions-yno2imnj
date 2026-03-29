class Solution:
    def isValid(self, s: str) -> bool:
        paren = {'(':')', '{':'}', '[':']'}
        stack = list()
        for i in s:
            if i in paren:
                stack.append(i)
            elif len(stack) != 0 and i == paren[stack.pop()]:
                continue
            else:
                return False
        return len(stack) == 0

        