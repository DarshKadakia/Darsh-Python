s=input("Enter string:")
i=0
count=0
while(i<len(s)):
    if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u" or s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U"):
        count+=1
    i+=1
print("number of vowels present in string:",count)