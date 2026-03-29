class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(operator, a, b):
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '*':
                return a * b
            else:
                return int(a / b)
        stack = []
        operators = ['+', '-', '*', '/']
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operation(t, a, b)
                stack.append(result)
        return stack[0]

        