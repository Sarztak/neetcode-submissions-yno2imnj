class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False
        
        def dfs(currStr, i, j):
            print(currStr, i, j, len(s3))

            if i == m and j < n:
                return s3 == currStr + s2[j:]
            if i < m and j == n:
                return s3 == currStr + s1[i:]
            if i + j > len(s3):
                return False

            if i == m and j == n:
                return True
            
            find = False
            if s2[j] == s3[i + j]:
                find = find or dfs(currStr + s2[j], i, j + 1)
            
            if find:
                return True
                
            if s1[i] == s3[i + j]:
                find = find or dfs(currStr + s1[i], i + 1, j)

            if find:
                return True
            
            return False

        
        return dfs("", 0, 0)