class Node(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self, node=Node()):
        self.root = node

    def add(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_word = True

    def exists(self, string):
        node = self.root
        for c in string:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
