def listRev(lst,ind=-1):
    if ind==-(len(lst)+1):
        return []
    return [lst[ind]]+listRev(lst,ind-1)

print(listRev([1,2,3,4,5]))
