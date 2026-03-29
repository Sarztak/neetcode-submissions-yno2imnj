class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_s1 = dict()
        window = dict()
        k = len(s1)

        if len(s2) < k:
            return False
        for s in s1:
            char_s1[s] = char_s1.get(s, 0) + 1
        for i in range(k):
            window[s2[i]] = window.get(s2[i], 0) + 1

        def check(dic):
            for key, value in char_s1.items():
                if dic.get(key, 0) != value:
                    return False
            return True
        
        if check(window):
            return True
        
        for i in range(len(s2) - k):
            window[s2[i]] -=  1
            window[s2[i + k]] = window.get(s2[i + k], 0) + 1
            if not check(window):
                continue
            else:
                return True
        return False

        