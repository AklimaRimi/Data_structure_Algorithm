from dataclasses import dataclass


class Tree:
    def __init__(self,data,child = []):
        self.data = data
        self.child = child
        
    def add(self,child):
        self.child.append(Tree)
        
    def __str__(self,level = 0):
        ret = '-' * level + str(self.data) + '\n'
        for i in self.child:
            ret += str(i)
        
        return ret
        

tree = Tree('tree',[])
branch = Tree('branch',[])
leaf1 = Tree('leaf1',[])
leaf2 = Tree('leaf2',[])


tree.add(leaf1)
tree.add(leaf2)

print(tree)