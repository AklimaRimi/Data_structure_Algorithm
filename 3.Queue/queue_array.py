from operator import index


class queue:
    def __init__(self):
        self.q = []
    def enqueue(self, value):
        self.q.append(value)
    def dequeue(self):
        if len(self.q) == 0:
            print('Queue is empty')
        else:
            del self.q[0]
    def top(self):
        if len(self.q) == 0:
            print('Queue is empty')
        else:
            print(f'Top value is {self.q[0]}')
        
queue = queue()

queue.enqueue(10)
queue.top()
queue.enqueue(20)
queue.top()
queue.enqueue(30)
queue.dequeue()
queue.top()
    