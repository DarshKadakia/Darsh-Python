lst=[(),(2,),("Jay","Patel")]

print(lst)

for i in lst:
    if isinstance(i,tuple):
        if not i:
            lst.remove(i)
print(lst)
