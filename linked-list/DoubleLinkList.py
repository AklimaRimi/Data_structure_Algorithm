from tokenize import Double


class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class double:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, data, loc):
        newnode = Node(data)
        
        if self.head == None:            
            self.head = newnode
            self.tail = newnode
        else:
            if loc == 1:
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
                newnode.prev = None
            elif loc == -1:
                
                newnode.prev = self.tail
                self.tail = newnode
                newnode.next = None
            else:
                temp = self.head
                
                index = 0
                while index < loc -1:
                    temp = temp.next
                    index += 1
                
                newnode.next = temp.next
                newnode.prev = temp
                newnode.next.prev = newnode
                temp.next = newnode
        
    def iter(self):
        temp = self.head
        
        while temp:
            print(temp.data)
            temp = temp.next
                    
                    
dll = double()

dll.add(20,1)
dll.add(10,1)
dll.add(30,-1)



dll.iter()

