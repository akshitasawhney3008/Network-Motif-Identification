# import itertools
# in_list = [1, 2, 3]
# out_list = []
# for i in range(1, len(in_list)+1):
#     out_list.extend(itertools.combinations(in_list, i))
# comb_list = [list(t) for t in out_list]
# print(comb_list)


from itertools import combinations
comb_list =list(combinations([1,2,3,4,5],3))
comb_list = [list(t) for t in comb_list]
print(comb_list)
list3=[]
adj=0
list1=[1,2,3,4,5,6,7]
list2=[5,4,6,7,3,2]
print(sorted(list1)==sorted(list2))
for l in list1:
    for l1 in list2:
        if l==l1:
            list3.append(l1)
            adj+=1
    if adj==0:
        continue
    for l2 in list3:
        print(l2)

