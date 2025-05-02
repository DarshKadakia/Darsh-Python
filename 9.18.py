def avg(lst,ind=0):
    if len(lst)==ind:
        return 0
    return (lst[ind]/len(lst))+avg(lst,ind+1)

print(f"Avarage:{avg([1,2,3,4,5])}")
