file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')
outfile = open('merged.txt', 'w')

lines1 = file1.readlines()
lines2 = file2.readlines()

max_len = max(len(lines1), len(lines2))
for i in range(max_len):
    if i < len(lines1):
        outfile.write(lines1[i])
    if i < len(lines2):
        outfile.write(lines2[i])

file1.close()
file2.close()
outfile.close()
print("Files merged alternately into 'merged.txt'.")

