class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def alienOrder(words):
            # Step 1: Create a graph and a degree count
            graph = defaultdict(set)
            in_degree = defaultdict(int)
            
            # Initialize the in_degree for each unique character
            for word in words:
                for char in word:
                    in_degree[char] = 0
            
            # Step 2: Build the graph
            for i in range(len(words) - 1):
                word1, word2 = words[i], words[i + 1]
                min_length = min(len(word1), len(word2))
                
                # Find the first different character
                for j in range(min_length):
                    if word1[j] != word2[j]:
                        if word2[j] not in graph[word1[j]]:
                            graph[word1[j]].add(word2[j])
                            in_degree[word2[j]] += 1
                        break
                else:
                    # Check for invalid case where word1 is longer than word2 but they are the same up to min_length
                    if len(word1) > len(word2):
                        return ""
            
            # Step 3: Topological sort using a min-heap
            min_heap = []
            
            # Add all characters with in-degree of 0 to the min-heap
            for char in in_degree:
                if in_degree[char] == 0:
                    heapq.heappush(min_heap, char)
            
            order = []
            
            while min_heap:
                char = heapq.heappop(min_heap)
                order.append(char)
                
                for neighbor in graph[char]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        heapq.heappush(min_heap, neighbor)
            
            # If the order contains all characters, return it as a string
            if len(order) == len(in_degree):
                return ''.join(order)
            else:
                return ""  # Cycle detected or not all characters are included
        return alienOrder(words)


            