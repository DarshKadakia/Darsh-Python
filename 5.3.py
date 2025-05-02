import random

list=[]

while len(list)<50:
    list.append(random.randrange(1,30))
    
for i in list:
    for j in range(0,list.count(i)-1):
        list.remove(i)
        
print(list)
