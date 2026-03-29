class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        parent = self.root
        for w in word:
            i = ord(w) - ord('a')
            if parent.children[i] == None:
                parent.children[i] = TrieNode()
            parent = parent.children[i]
        parent.endOfWord = True

    def find(self, parent, word: str) -> bool:
        for k, w in enumerate(word):
            i = ord(w) - ord('a')
            if w == '.':
                found = False
                for j in range(26):
                    if found:
                        break
                    if parent.children[j] != None:
                        found = self.find(parent.children[j], word[k+1:])
                return found
            else:
                if parent.children[i] == None:
                    return False
            parent = parent.children[i]   

        return parent.endOfWord

    def search(self, word: str) -> bool:
        return self.find(self.root, word)

