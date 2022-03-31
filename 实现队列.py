from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def append(self,val):
        return self.items.append(val)

    def pop(self):
        return self.items.popleft()

    def empty(self):
        return len(self.items) == 0

def test_queue():
    q = Queue()
    q.append(0)
    q.append(1)
    q.append(2)
    print(q.pop())
    print(q.pop())
    print(q.pop())

test_queue()


#实现栈
class Stack(object):
    def __init__(self):
        self.deque = deque()

    def push(self,value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()