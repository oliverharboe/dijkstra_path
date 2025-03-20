from random import randint
from node import Node
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush,heappop,heapify


class Graph:
    def __init__(self):
        self.nodes={}
    
    def add_node(self,id,node):
        self.nodes[id]=node
        
    def gen_graph(self):
        #add nodes
        node_amount = randint(6,10)
        for idx in range(node_amount):
            newnode = Node(idx)
            self.add_node(idx,newnode)
        # add egdes
        for idx in range(node_amount):
            current_node = self.nodes[idx]
            egde_amount = randint(4,node_amount-(node_amount//2))
            for _ in range(egde_amount):
                random_node = randint(0,node_amount-1) # select random node
                if random_node != current_node.id:
                    random_weight = randint(5,10) # create random weight
                    current_node.add_edge(random_weight,random_node)

    def show_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(range(len(self.nodes)))
        for node in self.nodes.values():
            for verweight, nextnode in node.next:
                G.add_edge(node.id,nextnode,weight=verweight)
        pos = nx.circular_layout(G)  # Layout for grafen
        plt.figure(figsize=(10, 8))  # Størrelse på grafens plot
        nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=12, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')  # Hent vægte på kanterne
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Vis vægtene på kanterne
        plt.title("Graf med korteste sti", fontsize=10)
        plt.show()


    def dijkstra(self,start,end):
        '''
        dijkstra algo
        '''
        heapque = [(0,start,[start])]
        visited_nodes = {start:1} # start id

        while len(heapque) != 0:
            distance, current_id,pathlst = heappop(heapque)
            if current_id == end: # if reach end done
                return distance,pathlst
            
            current_node = self.nodes[current_id]
            for nextweight,nextid in current_node.next:
                if nextid in visited_nodes:
                    continue
                else:
                    visited_nodes[nextid] = 1
                    heappush(heapque,(distance+nextweight,nextid,pathlst + [nextid]))
        return "Not Possible"
            

        





g1 = Graph()
g1.gen_graph()

for node in g1.nodes.values():
    print(f"id: {node.id} next : {[x for x in node.next]}")
g1.show_graph()
print(g1.dijkstra(0,3))


