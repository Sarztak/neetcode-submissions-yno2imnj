class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        letters = set()
        n = len(words)
        for i in range(n):
            for c in words[i]:
                letters.add(c)
            if i < n - 1:
                word1, word2 = words[i], words[i + 1]
                for c in word1 + word2:
                    letters.add(c)
                for j in range(min(len(word1), len(word2))):
                    if word1[j] != word2[j]:
                        adj[word1[j]].add(word2[j])
                        break

                if len(word2) < len(word1) and word1[:len(word2)] == word2:
                    return ""

        visited = {c: 0 for c in letters}
        order = []
        def dfs(c):
            if visited[c] == 1:
                return False # cycle detected
            if visited[c] == 2:
                return True # already processed

            visited[c] = 1

            for w in adj[c]: # post-order traversal
                if not dfs(w):
                    return False
            
            visited[c] = 2
            order.append(c)

            return True
        
        for c in letters:
            if not visited[c]:
                if not dfs(c):
                    return ""
        print(order)
        return "".join(order[::-1]) if len(order) == len(letters) else ""










