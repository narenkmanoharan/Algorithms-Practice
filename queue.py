class Queue:

    def __init__(self):
        self._list = []

    def enqueue(self, elem):
        self._list.append(elem)
        return self._list

    def dequeue(self):
        self._list.pop(0)
        return self._list

    def size(self):
        return len(self._list)

    def is_empty(self):
        return self._list == []

if __name__ == '__main__':
    que = Queue()
    print(que.enqueue(1))
    print(que.dequeue())
    print(que.enqueue(1231))
    print(que.enqueue(2341))
    print(que.enqueue(143))
    print(que.dequeue())
    print(que.dequeue())
    print(que.enqueue(123121))
    print(que.size())
    print(que.is_empty())
