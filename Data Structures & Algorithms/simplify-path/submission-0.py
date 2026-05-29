class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        x = [y for y in path.split('/') if y not in ["/", ""]]
        stack = []

        for i in x:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '.':
                continue
            else:
                stack.append(i)

        return "/" + "/".join(stack)