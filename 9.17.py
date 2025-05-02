def sanitize(lst,ind=0):
    if ind==len(lst):
        return []
    
    if lst[ind]>=0:
        return [lst[ind]]+sanitize(lst,ind+1)
    
    else:
        return [0]+sanitize(lst,ind+1)
    
print(sanitize([1,2,3,-4,-5]))
