lst1=[1,2,3,4,5,6,7,8,9]
lst2=[1,2,3,4,5]
lst3=[]

for i in lst1:
    if i not in lst2:
        lst3.append(i)
        
print(f"list 1:{lst1}")
print(f"list 2:{lst2}")
print(f"list:{lst3}")
