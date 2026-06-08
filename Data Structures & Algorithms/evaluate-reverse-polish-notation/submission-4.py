class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        operators = ['+', '-', '*', '/']

        for t in tokens:
            if t in operators:
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    if t == '+':
                        stack.append(a + b)
                    elif t == '-':
                        stack.append(a - b)
                    elif t == '*':
                        stack.append(a * b)
                    elif t == '/':
                        if b == 0: # if b is zero division is undefined, but I am setting it to zero
                            stack.append(0)
                        stack.append(int(a / b)) # int return
            else:
                stack.append(int(t))

        return stack[-1]
