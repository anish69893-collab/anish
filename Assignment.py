# Assinment-1, Question-2


# Create input file
with open("input.txt", "w") as f:
    f.write("Python is easy to learn\n")
    f.write("Python is a programming language")

# Read the text file
with open("input.txt", "r") as f:
    text = f.read()

# Count lines, words and characters
lines = text.splitlines()
words = text.split()
characters = len(text)

print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Number of Characters:", characters)

# Count particular word
word = input("Enter a word to search: ")
count = words.count(word)
print("Occurrence of", word, ":", count)

# Find longest and shortest words
longest = max(words, key=len)
shortest = min(words, key=len)

print("Longest Word:", longest)
print("Shortest Word:", shortest)

# Store results
with open("analysis.txt", "w") as f:
    f.write("Number of Lines: " + str(len(lines)) + "\n")
    f.write("Number of Words: " + str(len(words)) + "\n")
    f.write("Number of Characters: " + str(characters) + "\n")
    f.write("Occurrence of " + word + ": " + str(count) + "\n")
    f.write("Longest Word: " + longest + "\n")
    f.write("Shortest Word: " + shortest + "\n")

print("Analysis saved in analysis.txt")