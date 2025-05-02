def binary(num):
    
    def rev_binary(num):
        if num==0:
            return "0"
        if num==1:
            return "1"
        
        return str(num%2)+rev_binary(num//2)
    
    return int(rev_binary(num)[::-1])


print(binary(75))
