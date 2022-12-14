class BST:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
def insert(root,value):
    if root.data <= value.data:
        if root.next is None:
            root.next = value
        else:
            insert(root.next,value)
    else:
        if root.prev is None:
            root.prev = value
        else:
            insert(root.prev,value)
        
        

            
one =       BST(1)
two =       BST(2)
three =     BST(3)
four =      BST(4)
five =      BST(5)
six =       BST(6)
seven =     BST(7)
eight =     BST(8)
nine =      BST(9)
ten =       BST(10)
eleven =    BST(11)
tweleve =   BST(12)





insert(five,one)
insert(five,two)
insert(five,three)
insert(five,four)
insert(five,ten)
insert(five,nine)
insert(five,eight)
insert(five,seven)
insert(five,six)


    

def minval(root):
    while root.prev is not None:
        root = root.prev
    # delete(parent,root.data)
    return root 
        
# def search(parent,val):
#     temp = parent
#     if temp.data < val:
#         if temp.next.data == val:
#             return temp
#         return search(temp.next,val)
#     else:
#         if temp.prev.data == val:
#             return temp
#         return search(temp.prev,val) 
     
        
    

# def delete(parent,value):
#     print(f'searching for {value}')
#     root = search(parent,value)
#     print(f'{root.data} goooooothat {parent.data}')
#     if root.prev is None and root.next is None:
#         root = None
#     elif (root.prev is not None) and (root.next is not None):
#         node = minval(parent,root.next)
#         print('min value paise')
#         delete(parent.next,node.data)
#         root.data = node.data
        
#     else:
#         if root.prev is None:
#             root = root.next
#         else:
#             root = root.prev



def delete(parent,value):
    if parent is None:
        return parent
    if parent.data > value:
        parent.prev =  delete(parent.prev,value)
    elif parent.data < value:
        parent.next =  delete(parent.next,value)
    else:
        if parent.next == None:
            temp = parent.prev
            parent = None
            return temp
        elif parent.prev == None:
            temp = parent.next 
            parent = None
            return temp
        
        temp =  minval(parent.next)
        parent.data = temp.data
        parent.next = delete(parent.next,temp.data)
    return parent






print('\n\nInOrder:-')

def inorder(data):
    if not data:
        return 
    
    inorder(data.prev)
    print(data.data)
    inorder(data.next)

inorder(five)

delete(five,5)
print('After Deletion')
inorder(five)

delete(five,4)
print('After Deletion')
inorder(five)