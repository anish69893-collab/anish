# Assignment-1 , Question-1


FILE = "students.txt"

def add_record():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a") as f:
        f.write(f"{roll},{name},{course},{marks}\n")

    print("Record added successfully!")


def display_records():
    try:
        with open(FILE, "r") as f:
            for record in f:
                print(record.strip())
    except FileNotFoundError:
        print("No records found.")


def search_student():
    roll = input("Enter Roll Number to search: ")

    try:
        with open(FILE, "r") as f:
            for record in f:
                data = record.strip().split(",")

                if data[0] == roll:
                    print("Student Found:", record.strip())
                    return

        print("Student not found")

    except FileNotFoundError:
        print("No records found.")


def update_marks():
    roll = input("Enter Roll Number: ")
    new_marks = input("Enter New Marks: ")

    try:
        with open(FILE, "r") as f:
            records = f.readlines()

        with open(FILE, "w") as f:
            found = False

            for record in records:
                data = record.strip().split(",")

                if data[0] == roll:
                    data[3] = new_marks
                    f.write(",".join(data) + "\n")
                    found = True
                else:
                    f.write(record)

        if found:
            print("Marks updated successfully!")
        else:
            print("Student not found")

    except FileNotFoundError:
        print("No records found.")


while True:
    print("\n--- Student Record Management ---")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice!")

