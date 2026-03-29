class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        wordDict = defaultdict(list)
        l = len(wordList[0])
        for word in wordList:
            for i in range(l):
                parentWord = word[:i] + '*' + word[i + 1:]
                wordDict[parentWord].append(word)

        que = deque([beginWord])
        minLen = 0
        visited = set(beginWord)
        while que:
            minLen += 1
            for _ in range(len(que)):
                word = que.popleft()
                for i in range(l):
                    pattern = word[:i] + '*' + word[i + 1: ]
                    for neighbor in wordDict[pattern]:
                        if neighbor not in visited:
                            if neighbor == endWord:
                                return minLen + 1
                            visited.add(word)
                            que.append(neighbor)
        
        return 0
        