# def isPangram(String):
#     alpha={chr(i) for i in range(ord("A"),ord("Z")+1)}
#     if alpha-set(String.upper()) == set():
#         return "String is Pangram"  
#     else:
#         return "String is not Pangram"


def isPangram(String, ind=0, found=[]):
    if len(String) == ind:
        return "Is Pangram" if len(found) == 26 else "Is not Pangram"
    
    sample = list(chr(i) for i in range(ord("a"), ord("z"))) + [" "]
    ch = String[ind].lower()
    
    if ch in sample and ch not in found and ch != " ":
        found.append(ch)
        
    return isPangram(String, ind + 1, found)

print(isPangram("The quick brown fox jumps over the lazy dog"))
print(isPangram("Crazy Fredrick bought many very exquisite opal jewels"))
