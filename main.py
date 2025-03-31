from graph import Graph

def main():
    g1 = Graph()
    g1.gen_directed_graph()

    g1.show_graph()
    dist,path = g1.dijkstra(0,3)
    g1.show_graph(dist,path)

if __name__ == "__main__":
    main()