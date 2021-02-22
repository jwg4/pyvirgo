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

    def successors_of(self, node):
        queue = [node]
        s = set()
        while queue:
            n = queue.pop()
            for nn in self.direct_successors_of(n):
                if nn not in s:
                    s.add(nn)
                    queue.append(nn)
            
        return s

    def direct_predecessors_of(self, node):
        for n in self.nodes:
            if node in self.edges[n]:
                yield n

    def predecessors_of(self, node):
        """
            Not an efficient algorithm.
            Not clear if we care about this - do we
            want to use some other graph library?
        """
        for n in self.nodes: 
            if node in self.successors_of(n):
                yield n

    def add_description(self, node, description):
        self.nodes[node] = description

    def roots(self):
        s = set(self.nodes)
        for n in self.nodes:
            for m in self.edges[n]:
                if m in s:
                    s.remove(m)
        return s

    def topological_sort(self):
        total = 0
        count = defaultdict(int) 
        for n in self.nodes:
            for m in self.edges[n]:
                count[m] = count[m] + 1
                total = total + 1

        queue = list(self.roots())

        while queue:
            n = queue.pop()
            yield n
            for m in self.edges[n]:
                count[m] = count[m] - 1
                total = total - 1
                if count[m] == 0:
                    queue.append(m)

        if total > 0:
            raise Exception("Tried to topological sort a graph with a cycle.")


def make_graph(spec):
    connection_list, node_list = spec
    graph = Graph()
    for connections in connection_list:
        for connection in connections:
            graph.add_connection(connection)
    for node, description in node_list:
        graph.add_description(node, description)
    return graph
