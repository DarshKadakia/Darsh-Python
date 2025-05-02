def sum_avg(*marks):
    
    sum=0
    for i in marks:
        sum+=i
    avg=sum/len(marks)
    return sum,avg

print(sum_avg(90,90,90,90,90))
