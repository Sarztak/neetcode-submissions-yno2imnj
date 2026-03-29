class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for word in words:
            for c in word:
                in_degree[c] = 0
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            for j in range(min_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
    
        minHeap = []
        for c, i in in_degree.items():
                if i == 0:
                    heapq.heappush(minHeap, c)
        order = []
        while minHeap:
            node = heapq.heappop(minHeap)
            order.append(node)
            for n in graph[node]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    heapq.heappush(minHeap, n)
        
        if len(order) == len(in_degree):
            return ''.join(order)
        else:
            return ""

            