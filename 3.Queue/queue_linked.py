class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
        
class queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = node
            self.tail.prev = node
            
        else:
            newnode = node
            
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            newnode.prev = None
            
            
    def dequeue(self):
        if self.head == None:
            print('Stack is empty')
        else:
            x = self.tail.prev.prev
            # self.tail.prev = x.prev
            self.tail = x
            
    def top(self):
        if self.head == None:
            print('Stack is empty')
        else: 
            print(f'Next value is {self.tail.data}')
            
            
queue = queue()
queue.top()
queue.enqueue(10)
queue.top()
queue.enqueue(20)
queue.top()
queue.enqueue(30)
queue.enqueue(80)
queue.enqueue(100)
queue.enqueue(7)
queue.dequeue()
queue.top()
queue.dequeue()
queue.top()