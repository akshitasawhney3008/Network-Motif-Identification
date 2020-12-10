class Node:
    def __init__(self, id):
        self.id = id


class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target


class My_Graph:
    def __init__(self, list_of_nodes, list_of_edges):
        self.list_of_nodes = list_of_nodes
        self.list_of_edges = list_of_edges
