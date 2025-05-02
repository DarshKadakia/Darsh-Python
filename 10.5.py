src = "input.txt"
dest = "output.txt"

with open(src, 'r') as f1, open(dest, 'w') as f2:
    for line in f1:
        f2.write(line.upper())

print(f"Contents copied to {dest} in uppercase.")
