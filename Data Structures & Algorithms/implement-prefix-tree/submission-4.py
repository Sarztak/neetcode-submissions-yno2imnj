class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def idx(self, c):
        return ord(c) - ord('a')

    def insert(self, word: str) -> None:
        n = len(word)
        parent = self.root
        for i, w in enumerate(word):
            child = parent.children[self.idx(w)]

            if not child:
                child = TrieNode()
                parent.children[self.idx(w)] = child
           
            parent = parent.children[self.idx(w)]
        parent.endOfWord = True

    def search(self, word: str) -> bool:
        parent = self.root
        for w in word:
            i = ord(w) - ord('a')
            if not parent.children[i]:
                return False
            parent = parent.children[i]
    
        return parent.endOfWord


    def startsWith(self, prefix: str) -> bool:
        parent = self.root
        for w in prefix:
            i = ord(w) - ord('a')
            if not parent.children[i]:
                return False
            parent = parent.children[i]
            
        return True
        