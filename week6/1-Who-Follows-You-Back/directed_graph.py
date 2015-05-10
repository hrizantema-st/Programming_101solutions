class DirectedGraph:

    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph.keys():
            self.graph[node] = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph.keys():
            self.add_node(node_a)
        if node_b not in self.graph.keys():
            self.add_node(node_b)
        if node_b not in self.graph[node_a]:
            self.graph[node_a].append(node_b)

    def get_neighbours_for(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            raise ValueError

    def path_between(self, node_a, node_b):
        if node_b in self.graph[node_a]:
            return True
        neighbours = self.get_neighbours_for(node_a)
        for node in neighbours:
            return self.path_between(node, node_b)
