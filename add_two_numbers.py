import doctest

class LinkedList:

    class Node:

        def __init__(self, data=None, nxt=None):
            self.data = data
            self.nxt = nxt

        @property
        def node_data(self, data):
            return self.data

        @node_data.setter
        def node_data(self, data):
            self.data = data

        @property
        def node_next(self, nxt):
            return self.nxt

        @node_next.setter
        def node_next(self, nxt):
            self.nxt = nxt

    def __init__(self, head=None):
        self.head = head

    def insert(self, x):
        node = LinkedList.Node(x)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.nxt is not None:
                temp = temp.nxt
            temp.nxt = node

    def display(self):
        temp = self.head
        print(temp.data, end='')
        temp=temp.nxt
        while temp is not None:
            print(" -> {}".format(temp.data), end='')
            temp = temp.nxt
        print()

    def create_list(self):
        temp = self.head
        lst = []
        while temp is not None:
            lst.append(temp.data)
            temp = temp.nxt
        return lst

    def size(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 1
            while temp.nxt is not None:
                temp = temp.nxt
                count += 1
            return count

    def reverse(self):
        if LinkedList.size(self) == 1:
            self.head
        elif LinkedList.size(self) == 2:
            temp = self.head
            next = self.head.nxt
            self.head.nxt = None
            next.nxt = temp
            self.head = next
            return
        elif LinkedList.size(self) > 2:
            head = self.head
            temp_head = head
            temp_mid = head.nxt
            temp_last = head.nxt.nxt
            while temp_last is not None:
                temp_mid.nxt = temp_head
                temp_head = temp_mid
                temp_mid = temp_last
                temp_last = temp_last.nxt
            temp_mid.nxt = temp_head
            head.nxt = None
            self.head = temp_mid

    def __add__(l1, l2):
        carry = 0
        result = LinkedList()
        temp = None
        node = None
        LinkedList.reverse(l1)
        LinkedList.reverse(l2)
        l1 = l1.head
        l2 = l2.head
        while l1 is not None or l2 is not None:
            l1_data = 0 if l1 is None else l1.data
            l2_data = 0 if l2 is None else l2.data
            sum = l1_data + l2_data + carry
            carry = 0 if sum < 10 else 1
            sum = sum if sum < 10 else sum % 10
            result.insert(sum)
            if l1 is not None:
                l1 = l1.nxt
            if l2 is not None:
                l2 = l2.nxt
        if carry > 0:
            result.insert(carry)
        result.reverse()
        return result

if __name__ == '__main__':
    L = LinkedList()
    N = LinkedList()
    l = [9, 9, 9, 9, 9, 9]
    for x in l:
        L.insert(x)
    L.display()
    n = [9, 9, 9]
    for x in n:
        N.insert(x)
    N.display()
    res = L + N
    res.display()
