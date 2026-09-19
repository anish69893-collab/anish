# Assignment-1 question-3

import json

file = "employees.json"

def load():
    try:
        return json.load(open(file))
    except:
        return []

def save(data):
    json.dump(data, open(file, "w"), indent=4)

def add():
    data = load()
    emp = {
        "ID": input("ID: "),
        "Name": input("Name: "),
        "Department": input("Department: "),
        "Designation": input("Designation: "),
        "Salary": input("Salary: ")
    }
    data.append(emp)
    save(data)

def display():
    for e in load():
        print(e)

def search():
    id = input("Enter ID: ")
    for e in load():
        if e["ID"] == id:
            print(e)

def delete():
    id = input("Enter ID: ")
    data = [e for e in load() if e["ID"] != id]
    save(data)

add()
display()
search()
delete()