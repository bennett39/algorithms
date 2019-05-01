class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, root=Node()):
        self.root = root

    def insert(self, node):
        node.next = self.root
        self.root = node

    def delete(self, val):
        node = self.root
        try:
            while node.next.val != val:
                node = node.next
        except:
            print("Value not found")
            return
        tmp = node.next.next
        node.next = tmp

    def print(self):
        node = self.root
        while node:
            print(node.val)
            node = node.next

    def reverse(self):
        node = self.root
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        self.root = prev


n = Node(99)
ll = LinkedList(n)
for i in range(10):
    ll.insert(Node(i))
ll.print()
