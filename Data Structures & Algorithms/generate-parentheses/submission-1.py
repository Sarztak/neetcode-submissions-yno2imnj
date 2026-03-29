class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validParen = []
        def backtrack(paren, opening, closing):
            if len(paren) == 2*n:
                validParen.append(paren)
                return
            if opening < n:
                backtrack(paren + '(', opening + 1, closing)
            if closing < opening:
                backtrack(paren + ')', opening, closing + 1)
        backtrack("", 0, 0)
        return validParen
        