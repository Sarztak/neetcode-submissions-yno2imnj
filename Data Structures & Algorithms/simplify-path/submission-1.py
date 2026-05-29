class Solution:
    """
    The problem becomes simple one the string is split by / and then combined
    only toward the end. The stack needs to be used because the decision to keep 
    a folder or not depends on the future .. or . Also splitting help solve the problem
    of having multiple / 
    """
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