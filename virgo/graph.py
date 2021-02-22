from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.nodes = dict()
        self.edges = defaultdict(set)

    def add_connection(self, connection):
        for n in connection.first:
            self.nodes[n] = n
        for n in connection.second:
            self.nodes[n] = n
        
        for a in connection.first:
            for b in connection.second:
                if connection.op == "->" or connection.op == "--":
                    self.edges[a].add(b)
                if connection.op == "<-" or connection.op == "--":
                    self.edges[b].add(a)

    def direct_successors_of(self, node):
        return self.edges[node]

    def direct_predecessors_of(self, node):
        for n in self.nodes:
            if node in self.edges[n]:
                yield n
        
                
         
def make_graph(connection_list):
    graph = Graph()
    for connections in connection_list:
        for connection in connections:
            graph.add_connection(connection)
    return graph
