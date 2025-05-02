import csv

data = [
    ['rollno', 'name', 'subject1', 'subject2', 'subject3'],
    [101, 'Alice', 85, 90, 88],
    [102, 'Bob', 78, 82, 80],
    [103, 'Charlie', 92, 87, 85]
]

with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV file 'students.csv' created successfully.")
