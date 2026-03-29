class Solution:
    def checkAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        return True if s == t else False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)
        output = []
        flag = [0]*N
        for i in range(N):
            if flag[i] == 0:
                w = [strs[i]]
                flag[i] = 1
                for j in range(i + 1, N):
                    if self.checkAnagram(strs[i], strs[j]):
                        flag[j] = 1
                        w.append(strs[j])
                output.append(w)
        return output
        