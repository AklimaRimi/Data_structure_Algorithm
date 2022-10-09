
class Node:
    def __init__(self, d=None, n= None):
        self.data = d
        self.next = n
        
    def get_next(self):
        return self.next
    def set_next(self,n):
        self.next = n
    def get_data(self):
        return self.data
    def set_data(self,d):
        self.data = d
        
class LinkedList:
    def __init__(self, r = None):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node   # returns node value and location
            node = node.next
        
    def add(self,d,n):
        newnode = Node(d)
        
        if self.head  == None:
            self.head = newnode
            self.tail = newnode
        else:
            if n == 0:
                newnode.next = self.head
                self.head = newnode
            elif n == -1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < n-1:
                    tempnode = tempnode.next
                    index += 1
                    
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
    def traverse(self):
        temp =  self.head
        
        if temp is None:
            print('Linked list is empty')
        else:
            
            while temp:
                print(temp.data)
                temp = temp.next
    def search(self, value):
        temp =  self.head
        
        if temp is None:
            print(f"{value} doesn'e exit")
        else:
            found = 0
            
            index = 0
            while temp:
                if temp.data == value:
                    print(f'{value} is found at {index}')
                    found = 1
                    
                    break
                else:
                    temp = temp.next
                    index += 1
            if found == 0:
                print('value not found')
    def delete(self, value):
        temp = self.head
        prev = self.head
        
        if temp == None:
            print(f"{value} not found")
        else:
            while temp:
                if temp.data == value:
                    prev.next = temp.next 
                    break    
                else:
                    prev = temp
                    temp = temp.next
                
            
Llist = LinkedList()

Llist.add(10,0)
Llist.add(20,-1)
Llist.add(30,1)
Llist.add(50,0)
Llist.add(90,-1)
# for node in Llist:
#     print(node.data)

Llist.traverse()

Llist.search(30)
# print([x.data for x in Llist])

Llist.delete(20)
print("After")
Llist.traverse()