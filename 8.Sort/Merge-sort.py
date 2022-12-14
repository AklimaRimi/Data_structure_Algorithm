class mergeSort:
        
    def Merge_Sort(self,data):
        if len(data) <= 1:
            return data
        left, right = self.split(data)
        left_sorted = self.Merge_Sort(left)
        right_sorted = self.Merge_Sort(right)
        
        return self.merge(left_sorted,right_sorted)
    
    def split(self,data):

        half = len(data)//2
        return data[:half] , data[half:]
        
        
    def merge(self,left_data, right_data):
        l = []
        i = 0
        j = 0
        
        while i < len(left_data) and j < len(right_data):
            if left_data[i] < right_data[j]:
                l.append(left_data[i])
                i += 1
            else:
                l.append(right_data[j])
                j+=1
                
            
        while i < len(left_data):
            l.append(left_data[i])
            i += 1
            
        while j < len(right_data):
            l.append(right_data[j])
            j += 1  
        print(l)
        
        return l
    
    
    
li = [5,1,8,2,9,3,5,1,9 ,10 ,44,66,22,1]

m = mergeSort()

print(m.Merge_Sort(li))
            
        
            