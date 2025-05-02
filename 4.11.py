import math

def main():
    deg=int(input("Enter degree between 0 to 360:"))
    
    if 0<=deg<=360:
        print(f"Sine({deg})={sine(deg)}")
        
    else:
        print("Please enter degree between 0 to 360")
    
    
def fact(num):
    ans=1
    for i in range(1,num+1):
        ans*=i
    return ans
    
def sine(deg):
    rad=deg*math.pi/180
    ans=0
    for i in range(1,51):
        ans+=pow(-1,i-1)*pow(rad,2*i-1)/fact(2*i-1)
    return ans

main()
