def count_lower_upper(str):
    
    upper=0
    lower=0
    
    for i in str:
        if 'a'<=i<='z':
            lower+=1
            
        if 'A'<=i<='Z':
            upper+=1
            
    return {"number of upper case alphabates:":upper,"number of lower case alphabates:":lower}

print(count_lower_upper("PAtelJay"))
