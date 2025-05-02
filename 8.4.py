names={"Amit","Bhargav","Aryan","Brijesh"}

names_A=set()
names_B=set()

for i in names:
    if i[0]=="A":
        names_A.add(i)
        
    elif i[0]=="B":
        names_B.add(i)
        
print(names)
print(names_A)
print(names_B)
