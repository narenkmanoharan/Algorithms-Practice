class TreeNode:

    def __init__(self, data, left=None, right= None):
        self.data = data
        self.left = left
        self.right = right

    @property
    def node_data(self):
        return self.data

    @property
    def node_left(self):
        return self.left

    @property
    def node_right(self):
        return self.right

    @node_data.setter
    def node_data(self, data):
        self.data = data

    @node_left.setter
    def node_left(self, left):
        self.left.data = left

    @node_right.setter
    def node_right(self, right):
        self.right.data = right

class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            current = self.root
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
                else:
                    break

    def search(self, val, root):
        if not root:
            return None
        elif root.data is val:
            return root
        elif val < root.data:
            return self.search(val, root.left)
        elif val > root.data:
            return self.search(val, root.right)
        else:
            return None


    def __contains__(self, val):
        return bool(self.search(val, self.root))

    def inorder(self, val):
        if val is not None:
            self.inorder(val.left)
            print(val.data)
            self.inorder(val.right)

if __name__ == '__main__':
    tree = BinarySearchTree()
    inp = [1,4,23,56,12,657,213,56,32,577,234,68]
    for x in inp:
        tree.insert(x)
    tree.inorder(tree.root)
    if 5 in tree:
        print("True")
    else:
        print("Not found")


