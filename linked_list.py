class Node:

    def __init__(self, elem, _next=None):
        self.data = elem
        self._next = _next

    @property
    def node_data(self):
        return self.data

    @node_data.setter
    def node_data(self, data):
        self.data = data

    @property
    def node_next(self):
        return self._next.data

    @node_next.setter
    def node_next(self, Node):
        self._next = Node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, node):
        nd = Node(node)
        if self.head is None:
            self.head = nd
        else:
            temp = self.head
            while temp._next != None:
                temp = temp._next
            temp._next = nd
        temp = self.head
        while temp != None:
            length += 1
            temp = temp._next
        return length

    def is_empty(self):
        return self.head is None

    def remove(self, node):
        temp = self.head
        if temp.data == node:
            self.head = self.head._next
        else:
            while temp._next._next is not None:
                if temp._next.data == node:
                    temp._next = temp._next._next
                    return
                else:
                    temp = temp._next
            if temp._next.data == node:
                temp._next = None
            else:
                print("Element not found")

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='->')
            temp = temp._next
        print("list ended")

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert(10)
    lst.insert(20)
    lst.insert(333)

    lst.insert(1120)
    lst.insert(11230)
    lst.display()
    lst.remove(11230)
    lst.display()


