class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            2 : "a b c".split(),
            3 : "d e f".split(),
            4 : "g h i".split(),
            5 : "j k l".split(),
            6 : "m n o".split(),
            7 : "p q r s".split(),
            8 : "t u v".split(),
            9 : "w x y z".split()
        }
        
        if digits == "":
            return []
        
        res = []
        n = len(digits)

        def dfs(substring, i):
            if len(substring) == n:
                res.append(substring)
                return
            
            for j in range(i, n):
                for w in keypad[int(digits[j])]:
                    dfs(substring + w, j + 1)
        
        dfs("", 0)

        return res


