tup=(1,2,3,4,5,6,7,8,9)

print(tup)
ele=tup.index(int(input("Enter elemet to be changed:")))

if not ele:
    print("Element does not exist.")
    
else:
    lst=[]
    for i in tup:
        if i == tup[ele]:
            lst.append(int(input("Enetr new element:")))
        else:
            lst.append(i)
            
    tup=tuple(lst)
    print(tup)
