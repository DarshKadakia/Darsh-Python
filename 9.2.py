def compute(num,end=4,start=1):
    if start>end:
        return 0
    
    result=int(str(num)*start)
    return result+compute(num,end,start+1)

for i  in range(4,8): 
    print(compute(i))
