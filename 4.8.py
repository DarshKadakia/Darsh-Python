def main():
    number=int(input("Enter Number:"))
    
    if isPrime(number):
        print("number is prime number")
        
    if isArmstrong(number):
        print("number is Armstrong number")
        
    if isPalindrome(number):
        print("number is Palindrome number")
        
    if isPerfect(number):
        print("number is Perfect number")
        
    if isAutomorphic(number):
        print("number is Automorphic number")
    
    
def isPrime(num):
    for i in range(2,num):
        
        if num%i==0 and num>2:
            return False
        
        elif num==2:
            return True
        
        elif num<2:
            return False
        
        else:
            i+=1
    return True
        
def isPalindrome(num):
    copy=num
    
    rev=0
    while(num>0):
        remainder=num%10
        rev=rev*10+remainder
        num//=10
    return rev==copy
    
def isPerfect(num):
    new=0
    for i in range(1,num//2+1):
        if num%i==0:
            new+=i
    return new==num
        
def isArmstrong(num):
    copy=num
    
    new=0
    while(num>0):
        remainder=num%10
        new=new+pow(remainder,3)
        num//=10
    return new==copy

def isAutomorphic(num):
    sqr=pow(num,2)
    
    count=0
    copy=num
    new=0
    new_num=0
    while(num>0):
        num//=10
        count+=1
        
    for i in range(0,count):
        remainder=sqr%10
        new=new*10+remainder
        sqr//=10
        remainder_num=copy%10
        new_num=new_num*10+remainder_num
        copy//=10
    return new==new_num

main()
