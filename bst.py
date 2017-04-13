class Node(object):

    def __init__(self, data = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            current = self.root
            while True:
                if data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                elif data <= current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break

    def search(root, data):
        if not root:
            return "Not Found"
        elif root.data is data:
            return "Found"
        elif root.data > data:
            return self.search(root.right, data)
        elif root.data < data:
            return self.search(root.left, data)
        else:
            return "Not found"

def invert_tree(root):
    if not root:
        return 
    root.right, root.left = root.left, root.right
    invert_tree(root.left)
    invert_tree(root.right)
    return root

def max_depth(root):
    if not root:
        return
    return max(max_depth(root.left), max_depth(root.right)) + 1

def lowestCommonAncestor(root, p, q):
    if root.data < min(p.data, q.data):
        return lowestCommonAncestor(root.right, p, q)
    elif root.data > max(p.data, q.data):
        return lowestCommonAncestor(root.right, p.data, q.data)
    return root

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = math.floor(len(nums) / 2)
    root = Node(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def level_order_traversal(root):
    if not root:
        return
    queue = [root]
    while queue:
        nextlevel = list()
        printLevel = []
        for node in queue:
            printLevel.append(node.data)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)
        print(printLevel)
        queue = nextlevel

if __name__ == '__main__':
    x = BST(10)
    x.insert(20)
    x.insert(5)
    x.insert(50)
    x.insert(1)
    x.insert(4)
    x.insert(4)
    x.insert(8)
    x.insert(8)
    x.insert(2)
    x.insert(3)
    x.insert(41)
    x.insert(75)
    level_order_traversal(x.root)
