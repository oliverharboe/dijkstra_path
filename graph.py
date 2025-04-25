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
        node_amount = randint(5,6)
        for idx in range(node_amount):
            newnode = Node(idx)
            self.add_node(idx,newnode)
        # add egdes
        for idx in range(node_amount):
            current_node = self.nodes[idx]
            egde_amount = randint(2,4)
            for _ in range(egde_amount):
                random_node = randint(0,node_amount-1) # select random node
                if random_node != current_node.id:
                    random_weight = randint(3,10) # create random weight
                    current_node.add_edge(random_weight,random_node)
    
    def gen_undirected_graph(self):
        """
        generates random undirected graph
        """
        #add nodes
        node_amount = randint(5,6)
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
                    random_weight = randint(3,10) # create random weight
                    current_node.add_edge(random_weight,random_node)
                    self.nodes[random_node].add_edge(random_weight,current_node.id)


    def show_directed_graph(self,dist=None,path=[]):
        nxgraph = nx.MultiDiGraph(directed=True)
        plt.figure(figsize=(21, 10))  # Størrelse på grafens plot
        for node in self.nodes.values():
            for verweight, nextnode in node.next:
                nxgraph.add_edge(node.id,nextnode,weight=verweight)
        pos = nx.spring_layout(nxgraph,seed=12)
        nx.draw_networkx_nodes(nxgraph,pos,node_color="lightblue",label=True)
        nx.draw_networkx_labels(nxgraph, pos, font_size=12, font_weight="bold", font_color="black")
        # Bøjningsværdier til flere kanter
        rad_count = {}
        edge_seen = set()

        # Gennemgå og tegn hver kant med label
        for u, v, data in nxgraph.edges(data=True):
            edge = tuple(sorted((u, v))) # key in dic
            count = rad_count.get(edge, 0)
            if count%2 == 0: rad = 0.15*count
            else: rad = -0.15*count
            rad_count[edge] = count + 1

            if ((u,v,data['weight']) in path) and (u,v,data['weight']) not in edge_seen:
                edge_seen.add((u,v,data['weight']))
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
        

        if dist != None: # create title
            plt.title(f"Graf med korteste sti : {dist}", fontsize=10)
        else:
            plt.title("plot over graf", fontsize=10)
        plt.show()
    

    def show_undirected_graph(self,dist=None,path=[]):
        nxgraph = nx.MultiGraph()
        for node in self.nodes.values():
            for verweight, nextnode in node.next:
                    nxgraph.add_edge(node.id,nextnode,weight=verweight)

        # Tilføj kanter — nogle har duplikater (modsatrettede) med samme vægt
        # Her definerer du path som en liste af (u, v, vægt)

        pos = nx.spring_layout(nxgraph,seed=12)
        plt.figure(figsize=(8,6))
        nx.draw_networkx_nodes(nxgraph, pos, node_color="lightblue", node_size=700)
        nx.draw_networkx_labels(nxgraph, pos, font_weight="bold")

        edge_dic = {}  # Bruges til at filtrere duplikerede kanter
        rad_counter = {}  # Til at styre bøjning
        edge_seen = set()

        for u, v, data in nxgraph.edges(data=True):
            node_a = min(u, v)
            node_b = max(u, v)

            # Fjern duplikater: hvis vi allerede har tegnet denne vægt mellem disse to noder
            if (node_a, node_b, data['weight']) in edge_dic and edge_dic[(node_a, node_b, data['weight'])] == 1:
                edge_dic[(node_a, node_b, data['weight'])] = 0
                continue

            edge_dic[(node_a, node_b, data['weight'])] = 1  # Marker som set

            # Beregn bøjning
            count = rad_counter.get((node_a, node_b), 0)
            rad = 0.15 * count if count % 2 == 0 else -0.15 * count
            rad_counter[(node_a, node_b)] = count + 1

            # Farve: hvis den er i path, rød ellers grå
            if ((u, v, data['weight']) in path or (v, u, data['weight']) in path) and ((node_a,node_b) not in edge_seen):
                edge_seen.add((node_a,node_b))
                farve = 'red'
            else:
                farve = 'gray'

            # Tegn kanten
            nx.draw_networkx_edges(
                nxgraph, pos, edgelist=[(u, v)],
                connectionstyle=f"arc3,rad={rad}",
                edge_color=farve, width=2
            )

            # Label placering for vægt
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            label_x = (x1 + x2) / 2 + (rad * 0.7) * (y2 - y1)
            label_y = (y1 + y2) / 2 + (rad * 0.7) * (x1 - x2)

            plt.text(label_x, label_y, str(data.get("weight", "")), fontsize=12, color="blue", ha="center", va="center")

        if dist != None: # create title
            plt.title(f"Graf med korteste sti : {dist}", fontsize=10)
        else:
            plt.title("plot over graf", fontsize=10)
        plt.show()

    
    def dijkstra(self,start,end):
        '''
        dijkstra algo
        '''
        heapque = [(0,start,[])]
        visited_nodes = set() # start id

        while len(heapque) != 0:
            distance, current_id,pathlst = heappop(heapque)
            if current_id == end: # if reach end done
                return distance,pathlst
            
            if current_id in visited_nodes:
                continue
            
            visited_nodes.add(current_id)
            
            current_node = self.nodes[current_id]
            for nextweight,nextid in current_node.next:
                if nextid not in visited_nodes:
                    heappush(heapque,(distance+nextweight,nextid,pathlst + [(current_id,nextid,nextweight)]))
        return None, []
    



            
