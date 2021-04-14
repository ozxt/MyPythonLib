#前缀树

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            node = node.trie.setdefault(c,Trie())
        node.is_end = True


    def search_prefix(self, prefix: str) -> "Trie":
        node = self
        for c in prefix:
            node = node.trie.get(c,None)
            if not node:
                break
        return node


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.search_prefix(word)
        return node is not None and node.is_end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return bool(self.search_prefix(prefix))
