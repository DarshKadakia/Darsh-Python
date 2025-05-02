def vowels(String,ind=0):
    if ind==len(String):
        return 0
    
    count=0
    if String[ind] in "a A e E i I o O u U":
        count+=1
    return count+vowels(String,ind+1)

print(f"Number of vowels:{vowels("Pavish")}")
