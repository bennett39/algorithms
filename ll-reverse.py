class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, root_val):
        self.root = Node(root_val)

    def print(self):
        node = self.root
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print()

    def add(self, val):
        node = Node(val)
        node.next = self.root
        self.root = node

    def reverse(self):
        node = self.root
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        self.root = prev

    def middle(self):
        node = fast = self.root
        while fast and fast.next:
            node = node.next
            fast = fast.next.next
        print(f"Middle value is {node.val}")
