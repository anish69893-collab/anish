# Assignment -1 , Question-4


import json

# Create text file
with open("students.txt", "w") as f:
    f.write("101,Ankit,CSE,85\n")
    f.write("102,Neha,CSE,91\n")
    f.write("103,Rahul,MCA,78\n")

# Convert text file into list of dictionaries
students = []

with open("students.txt", "r") as f:
    for line in f:
        roll, name, course, marks = line.strip().split(",")

        students.append({
            "Roll Number": roll,
            "Name": name,
            "Course": course,
            "Marks": marks
        })

# Store data in JSON file
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

# Read JSON file
with open("students.json", "r") as f:
    students = json.load(f)

# Display records
for student in students:
    print("Roll Number:", student["Roll Number"])
    print("Name:", student["Name"])
    print("Course:", student["Course"])
    print("Marks:", student["Marks"])
    print()