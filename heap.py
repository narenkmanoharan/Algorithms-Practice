class Node:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    @property
    def node_data(self):
        return self.data

    @property
    def node_left(self):
        return self.left.data

    @property
    def node_right(self):
        return self.right.data

    @node_data.setter
    def node_data(self, data):
        self.data = data

    @node_left.setter
    def node_left(self, left):
        self.left.data = left

    @node_right.setter
    def node_right(self, right):
        self.right.data = right

class Heap:

    def __init__(self, root=None):
        self.root = root

    def heapify():
        pass

