class min_heap:
    def __init__(self,size):
        self.array = (size+2) *[None]
        self.current = 0
        
    def heapify(self,current,data):
        parent = int(current/2)
        if parent >= 1:
            if self.array[parent] > self.array[current]:
                temp = self.array[current]
                self.array[current] = self.array[parent]
                self.array[parent] = temp
            self.heapify(parent,data)
        else:
            return
    
    def insert(self, data):
        self.current += 1
        self.array[self.current] = data
        self.heapify(self.current,data)
    def show(self):
        print(self.array)
        
   

        
            
        
        
h = min_heap(10)

h.insert(388)
h.insert(231)
h.insert(1000)
h.insert(3)
h.insert(2)
h.insert(1)
h.show()

h.sort()

h.show()