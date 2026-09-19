# Assignment-1, question-5

# 1. Create and write to a file using w mode
file = open("demo.txt", "w")
file.write("Hello Python\n")
file.write("File Handling Example\n")
file.writelines(["Apple\n", "Banana\n", "Mango\n"])
file.close()

# 2. Read using read()
file = open("demo.txt", "r")
print("Using read():")
print(file.read())
file.close()

# 3. Read using readline()
file = open("demo.txt", "r")
print("Using readline():")
print(file.readline())
file.close()

# 4. Read using readlines()
file = open("demo.txt", "r")
print("Using readlines():")
print(file.readlines())
file.close()

# 5. Append data using a mode
file = open("demo.txt", "a")
file.write("Orange\n")
file.close()

# 6. r+ mode (read and write)
file = open("demo.txt", "r+")
print("Using r+ mode:")
print(file.read())
file.write("New Line\n")

# 7. tell() - current file position
print("Position:", file.tell())

# 8. seek() - change file position
file.seek(0)
print("After seek(0):")
print(file.readline())

file.close()

# 9. with open() - automatically closes the file
with open("demo.txt", "r") as file:
    print("Using with open():")
    print(file.read())