string=input("Enter String:")
countA=0
countD=0

for chr in string:
    if "A"<=chr<="Z" or "a"<=chr<="z":
        countA+=1
    if "0"<=chr<="9":
        countD+=1

print(f"Number of alphabets present in string is:{countA}")
print(f"Number of digits present in string is:{countD}")