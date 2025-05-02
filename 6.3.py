date1=(28,8,2006)
date2=(21,2,2025)

days=0
for i in range(date1[2],date2[2]):
    if i%4==0:
        days+=1
        
days+=(date1[2]-date2[2])*365
days+=(date1[0]-date2[0]**2)**0.5
