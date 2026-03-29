class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", 0, 0)]
        validParen = []
        while stack:
            paren, opening, closing = stack.pop()
            if len(paren) == 2*n:
                validParen.append(paren)
            if opening < n:
                stack.append((paren + '(', opening + 1, closing))
            if closing < opening:
                stack.append((paren + ')', opening, closing + 1))
        return validParen
        