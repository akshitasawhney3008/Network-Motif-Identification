import random
from My_Graph import *
from Read_Data import get_my_graph
from My_Graph_NX_Graph import Graph_Converter
from networkx import *


def random_num_selection(upper_bound):
    random_number = random.randrange(upper_bound)
    return random_number


def get_node_obj(node_list, nid):
    for n in node_list:
        if n.id == nid:
            return n


def initialization(g_obj):
    edge_list = g_obj.list_of_edges
    node_list = g_obj.list_of_nodes

    sub_graph_edge_list = []
    sub_graph_node_list = []

    r = random_num_selection(len(edge_list))
    selected_edge_object = edge_list[r]
    n1 = selected_edge_object.source
    n2 = selected_edge_object.target

    sub_graph_edge_list.append(selected_edge_object)
    sub_graph_node_list.append(get_node_obj(node_list, n1))
    sub_graph_node_list.append(get_node_obj(node_list, n2))

    sg = My_Graph(sub_graph_node_list, sub_graph_edge_list)
    return sg


def get_valid_incident_edges(g, node, visited_edge):
    list_to_be_returned = []
    edge_list = g.list_of_edges
    for edge in edge_list:
        if edge.source == node.id or edge.target == node.id:
            if check_presence(edge, visited_edge) == 0:
                list_to_be_returned.append(edge)
    return list_to_be_returned


def check_presence(edge, edge_list):
    flag = 0
    for e in edge_list:
        if e.source == edge.source and e.target == edge.target:
            flag = 1
            break
    return flag


def get_neighbour(edge, list_of_visted_nodes):
    flag1 = 0
    flag2 = 0
    s = edge.source
    t = edge.target
    for node in list_of_visted_nodes:
        if node.id == s:
            flag1 = 1
            break
    for node in list_of_visted_nodes:
        if node.id == t:
            flag2 = 1
            break
    if flag1 == 0:
        return s
    if flag2 == 0:
        return t


def remove_from_list(my_list, elt):
    for e in my_list:
        if e.source == elt.source and e.target == elt.target:
            my_list.remove(elt)
    return my_list


def sampling_algo(g, sg, motif_size):
    flag = 0

    list_of_visited_nodes = []
    list_of_visited_edges = []

    sg_node_list = sg.list_of_nodes
    sg_edge_list = sg.list_of_edges

    for sg_node in sg_node_list:
        list_of_visited_nodes.append(sg_node)

    for sg_edge in sg_edge_list:
        list_of_visited_edges.append(sg_edge)

    incident_edge_list = []
    for v_node in list_of_visited_nodes:
        ret_list = get_valid_incident_edges(g, v_node, list_of_visited_edges)
        for ret_edge in ret_list:
            incident_edge_list.append(ret_edge)

    while len(incident_edge_list) == 0:
        sg = initialization(g)

        flag = 0

        list_of_visited_nodes = []
        list_of_visited_edges = []

        sg_node_list = sg.list_of_nodes
        sg_edge_list = sg.list_of_edges

        for sg_node in sg_node_list:
            list_of_visited_nodes.append(sg_node)

        for sg_edge in sg_edge_list:
            list_of_visited_edges.append(sg_edge)

        incident_edge_list = []
        for v_node in list_of_visited_nodes:
            ret_list = get_valid_incident_edges(g, v_node, list_of_visited_edges)
            for ret_edge in ret_list:
                incident_edge_list.append(ret_edge)

    while flag != 1:
        r = random_num_selection(len(incident_edge_list))

        e = incident_edge_list[r]

        n_obj = get_node_obj(g.list_of_nodes, get_neighbour(e, list_of_visited_nodes))

        list_of_visited_nodes.append(n_obj)
        list_of_visited_edges.append(e)

        incident_edge_list = remove_from_list(incident_edge_list, e)

        ret_list = get_valid_incident_edges(g, n_obj, list_of_visited_edges)
        for ret_edge in ret_list:
            incident_edge_list.append(ret_edge)

        sg_node_list.append(n_obj)
        sg_edge_list.append(e)

        if len(list_of_visited_nodes) == motif_size:
            flag = 1
    sg.list_of_nodes = sg_node_list
    sg.list_of_edges = sg_edge_list
    return sg


motif_size = 4
my_graph_obj = get_my_graph('yeastinter_st.txt')
list_of_sub_graphs = []
total_graphs = 100

while len(list_of_sub_graphs) != total_graphs:
    sg_obj = initialization(my_graph_obj)
    sg_obj = sampling_algo(my_graph_obj, sg_obj, motif_size)
    list_of_sub_graphs.append(sg_obj)
    print (len(list_of_sub_graphs))

list_of_nx_bio_graphs = []
for sg in list_of_sub_graphs:
    list_of_nx_bio_graphs.append(Graph_Converter.convert_my_graph_to_nx_graph(sg.list_of_nodes, sg.list_of_edges))

list_of_nx_random_graphs = []
for counter in range(0, total_graphs - 1):
    list_of_nodes = []
    list_of_edges = []
    G = gnm_random_graph(len(list_of_sub_graphs[counter].list_of_nodes), len(list_of_sub_graphs[counter].list_of_edges))
    for e in G.edges:
        list_of_edges.append(Edge(int(e[0]), int(e[1])))
    for n in G.nodes:
        list_of_nodes.append(Node(int(n)))
    my_graph_obj_r = My_Graph(list_of_nodes, list_of_edges)
    list_of_nx_random_graphs.append(my_graph_obj_r)

bio_freq = []
for i in range(0, len(list_of_nx_bio_graphs)):
    counter = 0
    bg1 = list_of_nx_bio_graphs[i]
    for j in range(i + 1, len(list_of_nx_bio_graphs)):
       bg2 = list_of_nx_bio_graphs[j]
       if networkx.is_isomorphic(bg1, bg2) == True:
           counter += 1
    bio_freq.append(counter)

temp_list = []
for counter in range(0, len(list_of_nx_random_graphs)):
    list_of_nodes = []
    list_of_edges = []
    G = list_of_nx_random_graphs[counter]
    for e in G.list_of_edges:
        list_of_edges.append(Edge(int(e.source), int(e.target)))
    for n in G.list_of_nodes:
        list_of_nodes.append(n)
    my_graph_obj = My_Graph(list_of_nodes, list_of_edges)
    temp_list.append(my_graph_obj)

del list_of_nx_random_graphs[:]

for idx in range(0, len(temp_list)):
    list_of_nx_random_graphs.append(Graph_Converter.convert_my_graph_to_nx_graph(temp_list[idx].list_of_nodes, temp_list[idx].list_of_edges))

rand_freq = []
for i in range(0, len(list_of_nx_bio_graphs)):
    counter = 0
    bg1 = list_of_nx_bio_graphs[i]
    for j in range(i + 1, len(list_of_nx_random_graphs)):
       rg2 = list_of_nx_random_graphs[j]
       if networkx.is_isomorphic(bg1, rg2) == True:
           counter += 1
    rand_freq.append(counter)

print (bio_freq)
print (rand_freq)
