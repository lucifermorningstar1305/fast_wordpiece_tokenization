
class TrieNode:
    def __init__(self, char: str):

        self.char = char
        self.children = {}
        self.F = list()
        self.f = None
        self.chiv = ""

        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def build(self, vocab):
        r = self.root
        r_hash = None

        for key in vocab:

            start = self.root
            for c in key:
                isFound = False

                if c in start.children:
                    start = start.children[c]
                    isFound = True
                    continue

                if not isFound:
                    parent_chiv = start.chiv
                    start.children[c] = TrieNode(c)
                    start = start.children[c]
                    start.chiv = parent_chiv + c
                    if c == "#":
                        r_hash = start
            
            start.isEndOfWord = True

        return r, r_hash
