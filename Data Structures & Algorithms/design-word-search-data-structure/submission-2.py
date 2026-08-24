class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            n = ord(c)-ord("a")
            if not curr.children[n]:
                curr.children[n] = TrieNode()
            curr = curr.children[n]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        return self.searchFrom(word, self.root)
    
    def searchFrom(self, word, curr):
        if not word:
            return curr.endOfWord
        for i in range(len(word)):
            if word[i] == ".":
                for j in curr.children:
                    if j:
                        tmp = self.searchFrom(word[i+1:], j)
                        if tmp:
                            return True
                return False
            n = ord(word[i])-ord("a")
            if not curr.children[n]:
                return False
            curr = curr.children[n]
        
        return curr.endOfWord == True