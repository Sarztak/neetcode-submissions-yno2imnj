import string
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        stack = []

        while i < n:
            if s[i] in '123456789':
                j = i + 1
                while j < n and s[j] != '[':
                    j += 1
                    continue
                r = s[i:j]
                r = int(r)
                stack.append(r)
                stack.append('[')
                i = j + 1
            elif s[i] == ']':
                x = ''
                while stack:
                    if stack[-1] != '[':
                        x = x + stack.pop()[::-1]
                    else:
                        if len(stack) >= 2:
                            if stack[-1] == '[':
                                stack.pop()
                            r = stack.pop()
                            x = x * r
                            stack.append(x[::-1])
                            break
                print(stack)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        print(stack)  
        return "".join(stack)