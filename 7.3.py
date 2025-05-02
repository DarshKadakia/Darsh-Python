org={
    1:{"epy101":100000,"epy102":70000,"epy103":50000},
    2:{"epy201":50000,"epy202":60000,"epy203":40000},
    3:{"epy301":50000,"epy302":40000,"epy303":30000}
}

for i,j in org.items():
    
    min_salary=min(j.values())
    max_salary=max(j.values())
    
    print(f"Department no:{i} max salary:{max_salary} min salary:{min_salary}")
