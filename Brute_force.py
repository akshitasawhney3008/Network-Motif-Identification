from itertools import combinations
from My_Graph import My_Graph
from Read_Data import get_my_graph

my_graph_obj = get_my_graph('yeastinter_st.txt')


def conf_1_1(graph):
    list_of_nodes = my_graph_obj.list_of_nodes
    list_of_edges = my_graph_obj.list_of_edges
    list_of_adjacent_nodes_1 = []
    list_of_adjacent_nodes_2 = []
    list_of_adjacent_nodes_3 = []
    list_of_combinations = []
    comb_list = []
    list_of_conf_3_motifs = []
    list_of_nodes_conf_1_1=[]
    list_of_conf_1_1_motifs=[]
    level = 0
    adj_count_1 = 0
    adj_count_2 = 0
    adj_count_3 = 0
    for n in list_of_nodes:
        level = 0
        adj_count_1 = 0
        adj_count_2 = 0
        adj_count_3 = 0
        list_of_adjacent_nodes_1 = []
        list_of_nodes_conf_1_1 = []
        for e in list_of_edges:
            if n.id==e.source:
                list_of_adjacent_nodes_1.append(e.target)
                adj_count_1+=1
            elif n.id==e.target:
                list_of_adjacent_nodes_1.append(e.source)
                adj_count_1 += 1
        # level += 1
        list_of_adjacent_nodes_1 = list(set(list_of_adjacent_nodes_1))
        for a in list_of_adjacent_nodes_1:
            adj_count_2=0
            level = 1
            list_of_adjacent_nodes_2 = []
            for e in list_of_edges:
                if a == e.source:
                    list_of_adjacent_nodes_2.append(e.target)
                    adj_count_2 += 1
                elif a == e.target:
                    list_of_adjacent_nodes_2.append(e.source)
                    adj_count_2+= 1
            if adj_count_2==0:
                continue
            # level += 1
            list_of_adjacent_nodes_2.remove(n.id)
            list_of_adjacent_nodes_2 = list(set(list_of_adjacent_nodes_2))
            for l in list_of_adjacent_nodes_2:
                level = 2
                list_of_adjacent_nodes_3 = []
                if l == '7':
                    print('Hi')
                for e in list_of_edges:
                    if l == e.source:
                        list_of_adjacent_nodes_3.append(e.target)
                        # adj_count_3 += 1
                    elif l == e.target:
                        list_of_adjacent_nodes_3.append(e.source)
                        # adj_count_3 += 1
                list_of_adjacent_nodes_3.remove(a)
                if len(list_of_adjacent_nodes_3) == 0:
                    continue
                level += 1
                list_of_adjacent_nodes_3 = list(set(list_of_adjacent_nodes_3))
                if (level == 3):
                    for al in list_of_adjacent_nodes_3:
                        list_of_nodes_conf_1_1 = [0] * 4
                        list_of_nodes_conf_1_1[0] = n.id
                        list_of_nodes_conf_1_1[1] = a
                        list_of_nodes_conf_1_1[2] = l
                        list_of_nodes_conf_1_1[3] = al
                        # list_of_nodes_conf_1_1.insert(3,al)
                        flag=0
                        for m in list_of_conf_1_1_motifs:
                            # print(type(m[0]))
                            # print(type(list_of_nodes_conf_1_1[0]))
                            if sorted(m) == sorted(list_of_nodes_conf_1_1):
                                flag=1
                        if flag==0:
                            list_of_conf_1_1_motifs.append(list_of_nodes_conf_1_1)
                else:
                    level = 0
                    adj_count_1 = 0
                    adj_count_2 = 0
                    adj_count_3 = 0
                    list_of_adjacent_nodes_1 = []
                    list_of_adjacent_nodes_2 = []
                    list_of_adjacent_nodes_3 = []
    print(list_of_conf_1_1_motifs)
    print(len(list_of_conf_1_1_motifs))

def conf_2_1(graph):
    list_of_nodes = my_graph_obj.list_of_nodes
    list_of_edges = my_graph_obj.list_of_edges
    list_of_adjacent_nodes_1 = []
    list_of_adjacent_nodes_2 = []
    list_of_adjacent_nodes_3 = []
    list_of_combinations = []
    comb_list = []
    list_of_conf_2_1_motifs = []
    list_of_nodes_conf_2_1 = []
    level = 0
    adj_count_1 = 0
    adj_count_2 = 0
    adj_count_3 = 0
    for n in list_of_nodes:
        level = 0
        adj_count_1 = 0
        adj_count_2 = 0
        list_of_adjacent_nodes_1 = []
        list_of_nodes_conf_2_1 = []
        for e in list_of_edges:
            if n.id == e.source:
                list_of_adjacent_nodes_1.append(e.target)
                adj_count_1 += 1
            elif n.id == e.target:
                list_of_adjacent_nodes_1.append(e.source)
                adj_count_1 += 1
        level += 1
        list_of_adjacent_nodes_1 = list(set(list_of_adjacent_nodes_1))
        if (level == 1 and len(list_of_adjacent_nodes_1) >= 2):
            comb_list = list(combinations(list_of_adjacent_nodes_1, 2))
            list_of_combinations = [list(t) for t in comb_list]
            for al in list_of_combinations:
                list_of_nodes_conf_2_1 = [0] * 4
                list_of_nodes_conf_2_1[0] = n.id
                list_of_nodes_conf_2_1[1]=al[0]
                list_of_nodes_conf_2_1[2]=al[1]
                list_of_adjacent_nodes_2 = []
                for i in range(1,3):
                    for e in list_of_edges:
                        if list_of_nodes_conf_2_1[i] == e.source:
                            list_of_adjacent_nodes_2.append(e.target)
                            # adj_count_3 += 1
                        elif list_of_nodes_conf_2_1[i] == e.target:
                            list_of_adjacent_nodes_2.append(e.source)
                            # adj_count_3 += 1
                    list_of_adjacent_nodes_2.remove(n.id)
                    if len(list_of_adjacent_nodes_2) == 0:
                        continue
                    level += 1
                    list_of_adjacent_nodes_2 = list(set(list_of_adjacent_nodes_2))

                    for l in list_of_adjacent_nodes_2:
                        list_of_nodes_conf_2_1a = [0] * 4
                        list_of_nodes_conf_2_1a[0] = n.id
                        list_of_nodes_conf_2_1a[1] = al[0]
                        list_of_nodes_conf_2_1a[2] = al[1]
                        list_of_nodes_conf_2_1a[3] = l
                        flag=0
                        for m in list_of_conf_2_1_motifs:
                            # print(type(m[0]))
                            # print(type(list_of_nodes_conf_1_1[0]))
                            if sorted(m) == sorted(list_of_nodes_conf_2_1a):
                                flag = 1
                        if flag == 0:
                            list_of_conf_2_1_motifs.append(list_of_nodes_conf_2_1a)
    print(list_of_conf_2_1_motifs)
    print(len(list_of_conf_2_1_motifs))



def conf_1_2(graph):
    list_of_nodes = my_graph_obj.list_of_nodes
    list_of_edges = my_graph_obj.list_of_edges
    list_of_adjacent_nodes_1 = []
    list_of_adjacent_nodes_2 = []
    list_of_adjacent_nodes_3 = []
    list_of_combinations = []
    comb_list = []
    list_of_conf_3_motifs = []
    list_of_nodes_conf_1_2 = []
    list_of_conf_1_2_motifs = []

    level = 0
    adj_count_1 = 0
    adj_count_2 = 0
    adj_count_3 = 0
    for n in list_of_nodes:
        level = 0
        adj_count_1 = 0
        adj_count_2 = 0
        list_of_adjacent_nodes_1 = []
        list_of_nodes_conf_1_2 = []
        for e in list_of_edges:
            if n.id == e.source:
                list_of_adjacent_nodes_1.append(e.target)
                adj_count_1 += 1
            elif n.id == e.target:
                list_of_adjacent_nodes_1.append(e.source)
                adj_count_1 += 1
        #level += 1
        list_of_adjacent_nodes_1 = list(set(list_of_adjacent_nodes_1))
        for a in list_of_adjacent_nodes_1:
            adj_count_2 = 0
            level = 1
            list_of_adjacent_nodes_2 = []
            for e in list_of_edges:
                if a == e.source:
                    list_of_adjacent_nodes_2.append(e.target)
                    adj_count_2 += 1
                elif a == e.target:
                    list_of_adjacent_nodes_2.append(e.source)
                    adj_count_2 += 1
            if adj_count_2 == 0:
                continue
            level += 1
            list_of_adjacent_nodes_2.remove(n.id)
            list_of_adjacent_nodes_2 = list(set(list_of_adjacent_nodes_2))
            if (level==2 and len(list_of_adjacent_nodes_2)>=2):
                comb_list=list(combinations(list_of_adjacent_nodes_2, 2))
                list_of_combinations=[list(t) for t in comb_list]
                # list_of_nodes_conf_1_2.append(n.id)
                # list_of_nodes_conf_1_2.append(a)
                for al in list_of_combinations:
                    list_of_nodes_conf_1_2 = [0] * 2
                    list_of_nodes_conf_1_2[0] = n.id
                    list_of_nodes_conf_1_2[1] = a
                    for c in al:
                        list_of_nodes_conf_1_2.append(c)
                    flag = 0
                    for m in list_of_conf_1_2_motifs:
                        if sorted(m) == sorted(list_of_nodes_conf_1_2):
                            flag = 1
                    if flag == 0:
                        list_of_conf_1_2_motifs.append(list_of_nodes_conf_1_2)
            else:
                level=0
                adj_count_1=0
                adj_count_2=0
                list_of_adjacent_nodes_1=[]
                list_of_adjacent_nodes_2 = []
    print(list_of_conf_1_2_motifs)
    print(len(list_of_conf_1_2_motifs))

def conf_3(graph):
    list_of_nodes = my_graph_obj.list_of_nodes
    list_of_edges = my_graph_obj.list_of_edges
    list_of_adjacent_nodes=[]
    list_of_combinations=[]
    comb_list=[]
    list_of_conf_3_motifs=[]
    level=0
    adj_count=0
    # idx = 0
    for n in list_of_nodes:
        # if n.id==2:
            # print("caught")
        # print(idx)
        list_of_adjacent_nodes = []
        level = 0
        adj_count = 0
        for e in list_of_edges:
            if n.id==e.source:
                list_of_adjacent_nodes.append(e.target)
                adj_count+=1
            elif n.id==e.target:
                list_of_adjacent_nodes.append(e.source)
                adj_count += 1
        # print('Level')
        level += 1

        list_of_adjacent_nodes=list(set(list_of_adjacent_nodes))
        # print('LSL conversion')
        if (level==1 and adj_count>=3):
            # print('If')
            comb_list=list(combinations(list_of_adjacent_nodes, 3))
            list_of_combinations=[list(t) for t in comb_list]
            # print('Before for')
            # print(len(list_of_combinations))
            for c in list_of_combinations:
                # print('Inside for')
                # c.append(n.id)
                c.insert(0,n.id)
                flag = 0
                # print('Before inner for')
                for m in list_of_conf_3_motifs:
                    #print('Before set = set')
                    # if idx == 208:
                        # print('Caught')
                        # print(m)
                        # print(c)
                    if sorted(m)==sorted(c):
                        # if idx == 208:
                        #     print('Caught')

                        flag = 1
                if flag == 0:
                    list_of_conf_3_motifs.append(c)
        else:
            level=0
            adj_count=0
            list_of_adjacent_nodes=[]
        # idx += 1
    print(list_of_conf_3_motifs)
    print(len(list_of_conf_3_motifs))
conf_3(my_graph_obj)
conf_1_1(my_graph_obj)
conf_1_2(my_graph_obj)
conf_2_1(my_graph_obj)