import csv

data_dict = {}
with open('students.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rollno = row['rollno']
        total = int(row['subject1']) + int(row['subject2']) + int(row['subject3'])
        data_dict[rollno] = {
            'name': row['name'],
            'subject1': int(row['subject1']),
            'subject2': int(row['subject2']),
            'subject3': int(row['subject3']),
            'total': total
        }

print("Student Records:")
for rollno, details in data_dict.items():
    print(f"Roll No: {rollno}, Data: {details}")

