
class heap:
    def __init__(self, size):
        self.array = (size) * [None]
        self.current = 0
        
        
    
        
def heapify(node, current, data):
    parent = int(current/2)
    
    if parent >=1:
        if node.array[parent] < node.array[current]:
            temp =  node.array[current]
            node.array[current] = node.array[parent]
            node.array[parent] = temp
        heapify(node,parent,data)
    else:
        return
        
def insert(node, data):
    node.current += 1
    node.array[node.current] = data
    
    
    heapify(node, node.current,data)
    return 
        
def show(node):
    print(node.array)
    
    
def sort(self):
    for i in range(self.current,0,-1):
        if self.array[i] < self.array[1]:
            self.array[i],self.array[1] = self.array[1],self.array[i]
        
        heapidown(self,1,i-1)
    
            
    
def heapidown(self,index , i):
    left = 2*index
    right = 2*index + 1
    min = index
    # print(f'{index} ----{self.array}')
  
    if left < i and self.array[left] > self.array[index]:
        min = left
    if right < i and self.array[right] > self.array[min]:
        min = right  

    if min != index:
        self.array[index],self.array[min] = self.array[min],self.array[index]
        heapidown(self,min, i) 
    else:
        return
    return

def remove(self,value):
    for i in range(1,len(self.array)):
        if self.array[i] == value:
            self.array[i] = self.array[self.current]
            self.array[self.current] = None
            self.current -= 1
            heapify(self,self.current,value)
            return 
    
    return 
            
        

    
        
h = heap(7)
insert(h,2)
insert(h,1)
insert(h,10)
insert(h,3)
insert(h,40)


print('After inserting')
show(h)


remove(h,10)
print(f'After Removeing  {h.current}')
show(h)


sort(h)
print('After sorting')
show(h)
print('After Inserting')
insert(h,80)
show(h)
sort(h)

print('After Sorting')
show(h)