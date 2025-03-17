from random import randint
from node import Node

class Graph:
    def __init__(self):
        self.nodes={}
    
    def add_node(self,id,node):
        self.nodes[id]=node
        
    def gen_graph(self):
        #add nodes
        node_amount = randint(5,10)
        for idx in range(node_amount):
            newnode = Node(idx)
            self.add_node(idx,newnode)
        # add egdes
        for idx in range(node_amount):
            current_node = self.nodes[idx]
            egde_amount = randint(0,(node_amount-1)//2)
            for _ in range(egde_amount):
                random_node = randint(0,node_amount-1) # select random node
                random_weight = randint(5,20) # create random weight
                current_node.add_edge(random_weight,random_node)
                self.nodes[random_node].add_edge(random_weight,current_node.id)

g1 = Graph()
g1.gen_graph()

for node in g1.nodes.values():
    print(f"id: {node.id} next : {[x[1] for x in node.next]}")


