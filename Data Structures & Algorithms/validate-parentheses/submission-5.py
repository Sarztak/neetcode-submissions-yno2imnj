class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'[': ']', '{': '}', '(': ')'}
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if stack and d[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0