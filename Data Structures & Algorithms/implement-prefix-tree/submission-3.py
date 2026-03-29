class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        parent = self.root
        for w in word:
            i = ord(w) - ord('a')
            if not parent.children[i]:
                parent.children[i] = TrieNode()
            parent = parent.children[i]
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
        