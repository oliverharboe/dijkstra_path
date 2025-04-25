from graph import Graph

def main():
    g = Graph()
    while(True):
        ans = input("(d)irected graph or (u)ndirected graph (d/u): ")
        min_node, max_node= int(input("min amount of nodes: ")), int(input("max amount of nodes: "))
        node_input = (min_node,max_node)
        if ans  == "d": 
            g.gen_directed_graph(node_input)
            g.show_directed_graph()
        elif ans == "u": 
            g.gen_undirected_graph(node_input)
            g.show_undirected_graph()
        else:
            continue
        
        start_node = int(input("start node: "))
        end_node = int(input("end node: "))
        dist,path = g.dijkstra(start_node,end_node)

        if ans == "d":
            g.show_directed_graph(dist,path)
        else:
            g.show_undirected_graph(dist,path)

        if input("continue? (y/n): ") == "n":
            exit()

if __name__ == "__main__":
    main()