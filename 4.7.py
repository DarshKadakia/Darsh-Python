def main():
    n=int(input("Enter n:"))
    r=int(input("Enter r:"))

    if n>r and r!=0:
        print(f"({n} P {r})={npr(n,r)}")
        print(f"({n} C {r})={ncr(n,r)}")
        
    else:
        print("nPr or nCr is not possible.")

def npr(n,r):
    n_fact=1
    for i in range(0,r):
        n_fact*=n
        n-=1
    return n_fact
    
def ncr(n,r):
    r_fact=1
    for i in range(1,r+1):
       r_fact*=i
    return npr(n,r)/r_fact

main()
