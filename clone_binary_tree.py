class Node(object):

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        self.random = None

class CloneTree(object):

    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            if root.random:
                print(root.data + " : " + root.random.data)
            else:
                print(root.data + " : " + root.random)
            self.in_order_traversal(root.right)    

    def clone_tree(self, root):
        if root is None:
            return root
        newRoot = Node(root.data)
        newRoot.left = clone_tree(root.left)
        newRoot.right = clone_tree(root.right)
        newRoot.random = root.random
        root.random = newRoot
        return newRoot

    def restore_random(self, root):
        if root is None:
            return root
        cloned_root_random = root.random
        orig_random = cloned_root_random.random
        if (orig_random == null)
            cloned_root_random.random = null
        else
            cloned_root_random.random = orig_random.random
        root.random = orig_random
        restore_random(root.left)
        restore_random(root.right)
