class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = ['+', 'D', 'C']
        for o in operations:
            if o not in ops:
                try:
                    stack.append(int(o))
                except:
                    print(f"str: {o} cannot be converted to int")
            else:
                if len(stack) >= 2 and o == '+':
                    b = stack[-1] # order is reverse
                    a = stack[-2]
                    stack.append(a + b)
                elif len(stack) > 0:
                    if o == 'D':
                        a = stack[-1]
                        stack.append(a * 2)
                    elif o == 'C':
                        stack.pop()

        return sum(stack)
