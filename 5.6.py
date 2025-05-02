lst=[212,-40,0]

for i in lst:
    lst[lst.index(i)]=(i-32)*5/9
    
print(lst)
