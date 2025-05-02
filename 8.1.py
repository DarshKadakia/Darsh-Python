lst=["jay","kirit","patel"]

name=set()

def upper_case(strings):
    result=""
    
    for ch in strings:
        if "a"<=ch<="z":
            result+=chr(ord(ch)-32)
            
        else:
            result+=ch
            
    return result

for i in lst:
    name.add(upper_case(i))
    
print(name)
