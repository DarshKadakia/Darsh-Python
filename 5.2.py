import random

list=[]
while len(list)<20:
    list.append(random.randrange(1,100))
    
print(list)    
num=int(input("Enter number:"))

if num in list:
    print(f"{num} exist on index {list.index(num)}")
    
else:
    print(f"{num} does non exist in list")
