items={"oil":1200,"Biscuit":30,"Rice":40} #amount

#quantities are in liter, packet, Kg
qty={"oil":2,"Biscuit":2,"Rice":1}

sum=0
for i,j in qty.items():
    sum+=items[i]*j
    
print(qty)
print(f"Total Bill:Rs.{sum}")
