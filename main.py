from graph import Graph

def main():
    g1 = Graph()
    g1.gen_directed_graph()
    g1.show_directed_graph()
    start_node = int(input("start node: "))
    end_node = int(input("end node: "))
    dist,path = g1.dijkstra(start_node,end_node)
    g1.show_directed_graph(dist,path)

if __name__ == "__main__":
    main()