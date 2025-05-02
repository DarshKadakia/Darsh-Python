tup=(1,2,3,4,5,6,7,8,9)

print(tup)
ele=tup.index(int(input("Enter element to be delete:")))

if not ele:
    print("Element does not exist.")
    
else:
    lst=[]
    for i in tup:
        if i == tup[ele]:
            continue
        else:
            lst.append(i)
            
    tup=tuple(lst)
    print(tup)
