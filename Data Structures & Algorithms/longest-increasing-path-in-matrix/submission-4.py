from collections import deque
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        in_degree = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 1: Compute in-degrees (count how many smaller neighbors each cell has)
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        in_degree[x][y] += 1

        # Step 2: Start from all cells with in-degree 0 (smallest values)
        queue = deque([(i, j) for i in range(m) for j in range(n) if in_degree[i][j] == 0])
        level = 0  # This represents the longest path

        # Step 3: Process the queue layer by layer
        while queue:
            level += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        in_degree[x][y] -= 1
                        if in_degree[x][y] == 0:
                            queue.append((x, y))

        return level
