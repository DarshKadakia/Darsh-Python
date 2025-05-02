import random

liste=[]
listo=[]

while len(liste)<4:
    liste.append(random.randrange(2,100,2))
    listo.append(random.randrange(1,100,2))
    
print(f"odd :{listo}")
print(f"even :{liste}")

listo[2]=liste
print(f"without Flattern:{listo}")

listo[2:len(listo)-1]=liste
print(f"Flattern:{listo}")

listo.sort()
print(f"sort:{listo}")
