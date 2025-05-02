import random

lst=[random.randint(-15,15) for i in range (0,10)]
print(lst)

lst_sqr=list(map(lambda n:n*n,lst))
print(lst_sqr)
