class node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None
        self.nodecount = 0 

# class BT:
#     def __init__(self):
#         self.tail = None
#         self.head = None
#     def add(self,data,parent):
#         node = node(data)
#         if self.head == None:
#             self.head = node
#             self.prev = None
#             self.next = node
#         else:
#             temp = self.head
            
#             while temp.data == parent:
#                 temp = temp.next
#         temp.next = node
        
tree = node('tree')
branch = node('branch')
leaf = node('leaf')
stick1 = node('stick1')
stick2 = node('stick2')

tree.prev = branch
tree.next = leaf
branch.prev = stick1
branch.next = stick2

print('PreOrder')
def preorder(data):
    if not data:
        return 
    print(data.data)
    preorder(data.prev)
    preorder(data.next)

preorder(tree)

print('\n\nInOrder:-')

def inorder(data):
    if not data:
        return 
    
    inorder(data.prev)
    print(data.data)
    inorder(data.next)

inorder(tree)  



print('\n\nPostorder:==>')

def post(data):
    if not data:
        return 
    
    post(data.prev)
    post(data.next)
    print(data.data)


post(tree)  