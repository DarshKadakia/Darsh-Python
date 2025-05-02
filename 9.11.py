def create_list(lst1,lst2):
    
    set1=set(lst1)
    set2=set(lst2)
    
    intersec=list(set1.intersection(set2))
    return intersec

print(create_list([1,2,3,4,5],[1,2,5]))
