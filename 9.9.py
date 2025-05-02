def count_alpha_digit(string):
    
    calpha=0
    cdigit=0
    for ch in string:
        if "A"<=ch<="Z" or "a"<=ch<="z":
            calpha+=1
            
        elif "0"<=ch<="9":
            cdigit+=1
            
    return {"Number of alphabets":calpha,"Number of digits":cdigit}

print(count_alpha_digit("jAy6022"))
