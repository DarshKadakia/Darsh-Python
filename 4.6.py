for i in range(0,24):
    
    if 0<i<12:
        print(f"{i} AM")
        
    elif i>12:
        j=i-12
        print(f"{j} PM")
        
    elif i==12:
        print(f"12 PM")
        
    else:
        print(f"12 AM")
        
