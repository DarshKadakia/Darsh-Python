import random

lst=[]
for i in range(31):
    lst.append(random.randint(-100,100))
    
lstp=[]
lstn=[]

for i in lst:
    if i<0:
        lstn.append(i)
        
    else:
        lstp.append(i)
        
print(lstp)
print(lstn)
