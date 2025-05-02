string=input("Enter string:")

dict1={}

for i in string:
    dict1.update({i:string.count(i)})
    
print(dict1)
