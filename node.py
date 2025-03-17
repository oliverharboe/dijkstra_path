
class Node:
    def __init__(self,id):
        self.id=id
        self.next=[] # tuple (weight,node)
    
    def add_edge(self,weight,node):
        #adds connections to a new node
        self.next.append((weight,node))

    def remove_edge(self,node):
        #removes connections to a node
        self.next.remove(node)