class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enque(self, element):
        self.stack1.append(element)

    def deque(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)

q = Queue()

q.enque(1)
q.enque(2)
q.enque(3)

for i in range(3):
    print(q.deque())