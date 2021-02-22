class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_connection(self, connection):
        for n in connection.first:
            self.nodes.add(n)
        for n in connection.second:
            self.nodes.add(n)
        
        for a in connection.first:
            for b in connection.second:
                if connection.op == "->" or connection.op == "--":
                    key = (a, b)
                    self.edges[key] = True
                if connection.op == "<-" or connection.op == "--":
                    key = (b, a)
                    self.edges[key] = True
                
         
def make_graph(connection_list):
    graph = Graph()
    for connections in connection_list:
        for connection in connections:
            graph.add_connection(connection)
    return graph
