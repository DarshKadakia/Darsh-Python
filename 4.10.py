num=int(input("Enter number of Fibonacchi elements to be printed:"))

a=0
b=1

if num==1:
    print(a,end=" ")
    
elif num==2:
    print(f"{a} {b}",end=" ",sep=",")
    
else:
    print(f"{a} {b}",end=" ",sep=",")  
    for i in range(3,num+1):
        c=a+b
        print(c ,end=" ",sep=",")
        a=b                 
        b=c
