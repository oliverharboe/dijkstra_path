from random import randint
from node import Node
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappush,heappop


class Graph:
    def __init__(self):
        self.nodes={}
    
    def add_node(self,id,node):
        self.nodes[id]=node
        
    def gen_directed_graph(self):
        """
        generates random directed graph
        """
        #add nodes
        node_amount = randint(7,10)
        for idx in range(node_amount):
            newnode = Node(idx)
            self.add_node(idx,newnode)
        # add egdes
        for idx in range(node_amount):
            current_node = self.nodes[idx]
            egde_amount = randint(2,3)
            for _ in range(egde_amount):
                random_node = randint(0,node_amount-1) # select random node
                if random_node != current_node.id:
                    random_weight = randint(5,10) # create random weight
                    current_node.add_edge(random_weight,random_node)
    
    def gen_undirected_graph(self):
        """
        generates random undirected graph
        """
        #add nodes
        node_amount = randint(7,10)
        for idx in range(node_amount):
            newnode = Node(idx)
            self.add_node(idx,newnode)
        # add egdes
        for idx in range(node_amount):
            current_node = self.nodes[idx]
            egde_amount = randint(2,3)
            for _ in range(egde_amount):
                random_node = randint(0,node_amount-1) # select random node
                if random_node != current_node.id:
                    random_weight = randint(5,10) # create random weight
                    current_node.add_edge(random_weight,random_node)
                    self.nodes[random_node].add_edge(current_node.id,random_weight)


    def show_di_graph(self,dist=None,path=[]):
        nxgraph = nx.MultiDiGraph(directed=True)
        plt.figure(figsize=(21, 10))  # Størrelse på grafens plot
        for node in self.nodes.values():
            for verweight, nextnode in node.next:
                nxgraph.add_edge(node.id,nextnode,weight=verweight)
        pos = nx.circular_layout(nxgraph)
        nx.draw_networkx_nodes(nxgraph,pos,node_color="lightblue",label=True)
        nx.draw_networkx_labels(nxgraph, pos, font_size=12, font_weight="bold", font_color="black")
        # Bøjningsværdier til flere kanter
        rad_count = {}

        # Gennemgå og tegn hver kant med label
        for u, v, key, data in nxgraph.edges(keys=True, data=True):
            edge = tuple(sorted((u, v))) # key in dic
            count = rad_count.get(edge, 0)
            if count%2 == 0: rad = 0.15*count
            else: rad = -0.15*count
            rad_count[edge] = count + 1

            if (u,v,data['weight']) in path:
                farve = 'red'
            else:
                farve = 'gray'
            nx.draw_networkx_edges(nxgraph, pos, edgelist=[(u, v)],edge_color=farve, width=2,connectionstyle=f"arc3,rad={rad}")

            # Beregn label-position manuelt
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            label_x = (x1 + x2) / 2 + rad * 0.5 * (y2 - y1)
            label_y = (y1 + y2) / 2 + rad * 0.5 * (x1 - x2)

            # Skriv vægten med plt.text
            weight = data.get("weight", "")
            plt.text(label_x, label_y, str(weight), fontsize=12, color="blue", ha="center", va="center")
        

        if dist: # create title
            plt.title(f"Graf med korteste sti : {dist}", fontsize=10)
        else:
            plt.title("plot over graf", fontsize=10)
        plt.show()
    

    def show_undi_graph(self,dist=None,path=[]):
        G = nx.Graph()
        G.add_nodes_from(range(len(self.nodes)))
        for node in self.nodes.values():
            for verweight, nextnode in node.next:
                G.add_edge(node.id,nextnode,weight=verweight)
        pos = nx.circular_layout(G)  # Layout for grafen
        plt.figure(figsize=(10, 8))  # Størrelse på grafens plot
        nx.draw(G, pos, with_labels=True, node_color="lightblue", font_size=12, font_weight="bold")
        nx.draw_networkx_edges(G, pos)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color="red")

        if path:
            edges_in_path = list(zip(path, path[1:]))  # Opret kanter fra stien
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='r', width=2,connectionstyle="arc3,rad=0.3")
        plt.title(f"Graf med korteste sti : {dist}", fontsize=10)
        plt.show()

    
    def dijkstra(self,start,end):
        '''
        dijkstra algo
        '''
        heapque = [(0,start,[])]
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
                    heappush(heapque,(distance+nextweight,nextid,pathlst + [(current_id,nextid,nextweight)]))
        return None, None

if __name__ == '__main__':
    g1 = Graph()
    g1.gen_directed_graph()

    g1.show_di_graph()
    dist,path = g1.dijkstra(0,3)
    g1.show_di_graph(dist,path)


            
