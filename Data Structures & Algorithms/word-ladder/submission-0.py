class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        wordList = set(wordList)
        q.append([beginWord, 1])
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        while q:
            word, n = q.popleft()
            for i in range(len(word)):
                for letter in alphabet:
                    new_word = word[:i] + letter + word[i+1:]
                    if new_word == endWord:
                        return n + 1
                    if new_word in wordList:
                        q.append([new_word, n+1])
                        wordList.remove(new_word)
        return 0        
        