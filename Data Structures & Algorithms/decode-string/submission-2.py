import string
"""
The approach to the problem is again simple push everything to the stackw
and then pop when a closing bracket is encounter until an opening bracket is found
The only extra work is to convert the string number to integer before storing them
and then reversing the collected letters because stack is popped in reverse order
The crucial observation would be that this is a problem where the resolution 
of the most recent opening bracket is needed first and therefore stack should be used. 
"""
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
                parts = []
                while stack:
                    if stack[-1] != '[':
                        parts.append(stack.pop())
                    else:
                        parts.reverse()
                        x = ''.join(parts)
                        if len(stack) >= 2:
                            if stack[-1] == '[':
                                stack.pop()
                            r = stack.pop()
                            x = x * r
                            stack.append(x)
                            break
                print(stack)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        print(stack)  
        return "".join(stack)