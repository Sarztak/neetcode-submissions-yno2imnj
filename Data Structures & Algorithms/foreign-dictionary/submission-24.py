from collections import defaultdict
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        letters = set()

        # Step 1: Build Graph
        for i in range(len(words)):
            for c in words[i]:
                letters.add(c)
            if i < len(words) - 1:
                word1, word2 = words[i], words[i + 1]
                for c in word1 + word2:
                    letters.add(c)  # Store unique letters
                
                for j in range(min(len(word1), len(word2))):
                    if word1[j] != word2[j]:
                        if word2[j] not in adj[word1[j]]:
                            adj[word1[j]].add(word2[j])
                        break  # Stop at first different letter
                
                # Edge case: If word2 is a prefix of word1, it's an invalid order
                if len(word2) < len(word1) and word1[:len(word2)] == word2:
                    return ""

        # Step 2: DFS with Cycle Detection
        visited = {c: 0 for c in letters}  # 0 = unvisited, 1 = visiting, 2 = visited
        order = []
        
        def dfs(node):
            if visited[node] == 1:  # Cycle detected
                return False
            if visited[node] == 2:  # Already processed
                return True

            visited[node] = 1  # Mark as visiting
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            
            visited[node] = 2  # Mark as visited
            order.append(node)  # Postorder traversal
            return True

        # Step 3: Call DFS for each letter
        for char in letters:
            if visited[char] == 0:
                if not dfs(char):
                    return ""  # Cycle detected

        # Step 4: Reverse order since it's postorder DFS
        return "".join(order[::-1])





