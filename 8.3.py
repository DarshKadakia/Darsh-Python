names={"jay","vaidik","smit","vrushal"}

while True:
    name=input("enetr name(for exit enter q or Q):")
    if name == "q" or name == "Q":
        break
    
    names.add(name)
mdf=input("enter name to modify:")

for i in names:
    if mdf in names:
            names.remove(mdf)
            names.add(input("enter name to modify:"))
            break
        
print(names)
for i in range(0,2):
    names.pop()
    
print(names)
