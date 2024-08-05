"""10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once
by storing the lines in a list and then working with them outside the with block."""

# Solution - 1
print("Printing the entire file. ")
file = "learning_python.txt"
with open(file) as f:
    content = f.read()
    print(content)


# Solution - 2
print("\nPrinting each line from the file. ")
with open(file) as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# solution - 3
print("\nStoring the lines in a list and working outside the with block.")
with open(file) as fn:
    content = fn.readlines()

for lines in content:
    print(lines)

