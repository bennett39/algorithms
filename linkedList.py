class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = Node()

    def add(self, node):
        node.next = self.head
        self.head = node

    def print(self):
        node = self.head
        while node:
            print(node.val, end="->")
            node = node.next
        print()

l = LinkedList()
