import doctest
class Stack:
    
    def __init__(self):
        self.list = []

    def push(self, elem):
        self.list.append(elem)
        return self.list

    def pop(self):
        self.list.pop()
        return self.list

    def is_empty(self):
        return self.list == []

    def peek(self):
        return self.list[len(self.list)-1]

    def size(self):
        return len(self.list)

if __name__ == '__main__':
    stk = Stack()
    print(stk.push(1))
    print(stk.peek())
    print(stk.push(10))
    print(stk.push(12))
    print(stk.pop())
    print(stk.size())
    print(stk.push(121))
    print(stk.push(12134))
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())
    print(stk.is_empty())
