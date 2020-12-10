from My_Graph import My_Graph, Node, Edge


list_of_nodes = []
def get_my_graph(fname):
    list_of_nodes_as_int = []
    list_of_edges = []
    my_file = open(fname, 'r')
    lines = my_file.readlines()
    for line in lines:
        temp_list = line.strip().split()
        source = int(temp_list[0])
        target = int(temp_list[1])
        e = Edge(source, target)
        list_of_nodes_as_int.append(source)
        list_of_nodes_as_int.append(target)
        list_of_edges.append(e)
    list_of_nodes_as_int = list(set(list_of_nodes_as_int))
    for n in list_of_nodes_as_int:
        list_of_nodes.append(Node(n, 0))
    g = My_Graph(list_of_nodes, list_of_edges)
    return g
