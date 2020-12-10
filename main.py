import random
from My_Graph import My_Graph
from Read_Data import get_my_graph

my_graph_obj = get_my_graph('sample_yeastinter_st.txt')


# print ('Hi')


def random_num_selection(number_of_edges):
    # print(number_of_edges)
    random_number = random.randrange(number_of_edges)
    # print(random_number)
    return random_number


edge_list = my_graph_obj.list_of_edges
node_list = my_graph_obj.list_of_nodes

def node_is_visited(nodelist,e):
    flag = 0
    for n in nodelist:
        if n.id == e:
            flag=1
    if flag == 0:
        return False
    else:
        return True

def sampling_algo(edge_list, node_list, size_of_motif):
    # Ensure parallel operations bw 4 lists
    subgraph_edge_list = []  #sampled graph


    subgraph_node_list = []

    # visited_edge_list
    visited_node_list = []
    visited_edge_list= []

    list_of_incident_edges = []


    random_number = random_num_selection(len(edge_list))
    edge = edge_list[random_number]
    subgraph_edge_list.append(edge)
    visited_edge_list.append(edge)


    # Update other lists as well
    for node in node_list:
        if node.id == edge.source or node.id == edge.target:
            #node.is_visited = 1
            visited_node_list.append(node)
            subgraph_node_list.append(node)

    for e in edge_list:
        if e.source == edge.source or e.target == edge.source or e.source == edge.target or e.target == edge.target:
            list_of_incident_edges.append(e)

    for ie in list_of_incident_edges:
        if (ie.source == edge.source and ie.target == edge.target):
            list_of_incident_edges.remove(ie)
            # Choose between the concept of node.is_visited or visited node list to maintain the list of visited nodes
    while (len(subgraph_node_list) < size_of_motif):

        random_number = random_num_selection(len(list_of_incident_edges))
        edge = list_of_incident_edges[random_number]
        subgraph_edge_list.append(edge)
        visited_edge_list.append(edge)

        for node in node_list:
            if node.id == edge.source or node.id == edge.target:
               # node.is_visited = 1
                visited_node_list.append(node)
                subgraph_node_list.append(node)
        visited_node_list = list(set(visited_node_list))
        subgraph_node_list = list(set(subgraph_node_list))


        # The node should be unvisited and then only it should be added to the incident list - write a method to perform this sanity check and check that the
        # other node should not be present in visited node list
        for e in edge_list:
            flag1 = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            if e.source == edge.source:
                flag1 = 1
            elif e.target == edge.source:
                flag2 = 1
            elif e.source == edge.target:
                flag3 = 1
            elif e.target == edge.target:
                flag4 = 1

            if flag1 == 1 or flag3 == 1 :
                bool=node_is_visited(visited_node_list, e.target)
                if bool == False:
                    list_of_incident_edges.append(e)
            elif flag2 == 1 or flag4 == 1:
                bool=node_is_visited(visited_node_list,e.source)
                if bool == False:
                    list_of_incident_edges.append(e)



        # for ie in list_of_incident_edges:
        #     if (ie.source == edge.source and ie.target == edge.target):
        #         list_of_incident_edges.remove(ie)



        # Update other lists as well

    subgraph = My_Graph(subgraph_node_list, subgraph_edge_list)
    return subgraph

subgraph_list = []

subgraph_node_list = []
for i in range(10): # Create a list of subgraph motifs and append for 1000 such sub graphs using a loop
# size_of_motif=int(input())
    subgraph_list.append(sampling_algo(edge_list, node_list, 4))
print(len(subgraph_list))
for sub in subgraph_list:
    subgraph_nodes = []
    for n in sub.list_of_nodes:
        subgraph_nodes.append(n.id)
    subgraph_node_list.append(subgraph_nodes)
print(subgraph_node_list)