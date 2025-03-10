
class Node:
    def __init__(self,id,next:list):
        self.id=id
        self.next=next
    
    def add_con(self,node):
        #adds connections to a new node
        self.next.append(node)
    def remove_con(self,node):
        #removes connections to a node
        self.next.remove(node)

class Graph:
    def __init__(self):
        self.nodes={}
    
    def add_node(self,node):
        self.nodes[node.id]=node

