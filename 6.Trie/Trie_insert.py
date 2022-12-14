class trieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        
class trie:
    def __init__(self):
        self.node = trieNode()
    
    def insert(self,word):
        root = self.node
        for i in word:
            if root.child.get(i) == None:
                new_child = trieNode()
                root.child.update({i:new_child})
                
        root.end = True
                
        print(f'{word} saved')
        
    def search(self, word):
        root = self.node
        
        for i in word:
            if root.child.get(i) == None:
                return False
            root = root.child.get(i)
            print(root)
            
        
        if root.end == True:
            return True
        else:
            return False
        
Trie = trie()

Trie.insert('Rimi')
Trie.insert('Rimon')
print(Trie.search('Rimi'))
                
        
        