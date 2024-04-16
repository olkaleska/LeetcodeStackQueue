"""
Implement Queue using Stacks
"""
class Queue(object):
    """Наша черга"""
    def __init__(self, elements = None):
        # self.tail = tail
        if elements:
            self.elements = list(elements)
        else:
            self.elements = []

    def pop(self):
        return self.elements.pop(0)

    def push(self, new):
        self.elements.append(new)

class MyStack(object):
    """Наш стак"""
    def __init__(self):
        self.first_q = Queue()
        self.second_q = Queue()

    def pop(self):
        self.second_q = Queue()
        while len(self.first_q.elements) > 1:
            self.second_q.push(self.first_q.pop())
        item = self.first_q.pop()
        self.first_q = Queue(self.second_q.elements)
        return item

    def push(self, new):
        self.first_q.push(new)

    def top(self):
        if not self.empty():
            return self.first_q.elements[-1]
        return None

    def empty(self):
        return not self.first_q.elements
