class Node:
    def __init__(self,data= None):
        self.node = data
        self.next = None
        
class stack:
    
    def __init__(self):
        self.head = None
    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            node.next = None
        else:
           node.next = self.head
           self.head = node
           
            
    def pop(self):
        if self.head == None:
            print("stack is empty")
        else:
            self.head.next = self.head.next.next
            print('poped')
    def top(self):
        if self.head == None:
            print('Stack is empty')
        else:
            print(f'Top value is {self.head.node}')

    def delete_stack(self):
        self.head = None
            
        
            
stack = stack()
stack.push(10)
stack.push(22)
stack.push(32)
stack.delete_stack()
stack.pop()
stack.pop()
stack.top()
