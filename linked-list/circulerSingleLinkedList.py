class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None
class csl:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def create(self,data):
        node = Node(data)
        self.head = node
        self.tail = node
        node.next = node
        
        
    def add(self,data,loc):
        node = Node(data)

        if self.head is not  None:
            if loc == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif loc == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
                
                
           
                    
    def traverse(self):
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            
            if temp == self.head:
                break
            
CSL = csl()
CSL.add(0,0)
CSL.add(1,0)
CSL.add(2,1)
CSL.add(10,1)
CSL.add(2,1)


CSL.traverse()
               