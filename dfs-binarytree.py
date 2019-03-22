class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_tree(inorder, preorder):
    if inorder:
        node = Node(preorder[0])
        index = inorder.index(preorder.pop(0))
        node.left = create_tree(inorder[:index], preorder)
        node.right = create_tree(inorder[index+1:], preorder)

        return node


def dfs_print(root):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val, end='\t')
        node = node.right
    print()


def main():
    inorder = [3, 1, 4, 0, 5, 2, 6]
    preorder = [0, 1, 3, 4, 2, 5, 6]
    t = create_tree(inorder, preorder)
    dfs_print(t)


if __name__ == "__main__":
    main()
