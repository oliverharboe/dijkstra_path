

class Path:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end

    def dijkstra(self):
