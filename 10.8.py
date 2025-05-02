with open('textfile.txt', 'r') as infile, open('cleaned.txt', 'w') as outfile:
    for line in infile:
        words = line.split()
        filtered_words = [word for word in words if word.lower() not in ['a', 'an', 'the']]
        outfile.write(' '.join(filtered_words) + '\n')

print("Filtered content written to 'cleaned.txt'.")
