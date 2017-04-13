class Node(object):

    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
    
class LinkedList(object):

    def __init__(self, head):
        self.head = Node(head)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        if data == None:
            return
        node = Node(data)
        head = self.head
        while head.next:
            head = head.next
        head.next = node
        return

    def search(self, data):
        if self.head == None:
            return "Not found"
        else:
            head = self.head
            while head:
                if head.data == data:
                    print("Found")
                    return
                head = head.next
            return "Not found"

    def is_empty(self):
        return self.head is None

    def remove(self, data):
        if self.head == None:
            return "Empty list"
        else:
            head = self.head
            prev = head
            curr = head.next
            while curr:
                if curr.data == data:
                    prev.next = curr.next
                    return
                prev = prev.next
                curr = curr.next
            return "Element not found"

    def reverse(self):
        if self.head:
            self.reverse_util(self.head)
        else:
            print("No head!!!")

    def reverse_util(self, node, prev=None):
        if not node:
            self.head = prev
            return prev
        next_node = node.next
        node.next = prev
        return self.reverse_util(next_node, node)
    
    def display(self):
        if self.head == None:
            return "Empty List"
        else:
            head = self.head
            while head:
                print(str(head.data))
                head = head.next
            return

if __name__ == '__main__':
    x = LinkedList(1)
    x.insert(10)
    x.insert(20)
    x.insert(30)
    x.insert(40)
    x.display()
    x.search(10)
    x.remove(10)
    x.reverse()
    x.display()