class Node:

    def __init__(self, val):
        self.val = val

    def pr(self, root):
        if self == root:
            print(self.val)


if __name__ == '__main__':
    node = Node(10)
    node.pr(node)
    
