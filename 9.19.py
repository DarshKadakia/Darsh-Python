def str_len(String):
    if String=="":
        return 0
    
    else:
        return 1+str_len(String[1:])
    
print(f"Length of String:{str_len("Jay Patel")}")
