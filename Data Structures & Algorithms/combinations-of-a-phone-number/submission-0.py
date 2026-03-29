class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        mapping = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z']
        }
        def dfs(idx, letters):
            if idx == len(digits):
                res.append(letters)
                return
            
            for w in mapping[digits[idx]]:
                letters += w
                dfs(idx + 1, letters)
                letters = letters[:-1]
        dfs(0, '')
        return res
        