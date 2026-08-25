import os

# Directory to list (current directory)
directory = "."

try:
    contents = os.listdir(directory)

    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("Permission denied.")