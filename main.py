from graph import Graph

def main():
    g1 = Graph()
    while(True):
        ans = input("(d)irected graph or (u)ndirected graph (d/u): ")
        if ans  == "d": 
            g1.gen_directed_graph()
            g1.show_undirected_graph()
        elif ans == "u": 
            g1.gen_undirected_graph()
            g1.show_undirected_graph()
        else:
            continue
        
        start_node = int(input("start node: "))
        end_node = int(input("end node: "))
        dist,path = g1.dijkstra(start_node,end_node)

        if ans == "d":
            g1.show_directed_graph(dist,path)
        else:
            g1.show_undirected_graph(dist,path)

        if input("continue? (y/n): ") == "n":
            exit()

if __name__ == "__main__":
    main()