# Try It Yourself Exercise File for Files & Exceptions py:

# Addition : 10.6

number_1 = input("Enter the 1st number : ")
number_2 = input("Enter the 2nd number: ")

try:
    sum = int(number_1) + int(number_2)
except ValueError:
    print("You entered the wrong value.")
else:
    print(sum)


# Addition Calculator:
while True:
    number_1 = input("Enter the 1st number : ")
    if number_1 == "q":
        break
    number_2 = input("Enter the 2nd number: ")
    if number_2 == "q":
        break

    try:
        sum = int(number_1) + int(number_2)
    except ValueError:
        print("You entered the wrong value.")
    else:
        print(sum)


# 10.8 Cats & Dogs
def read_file(file):
    """A function that takes in a file and readout the contents of that file."""
    try:
        with open(file) as fn:
            content = fn.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\n{content}\n")

filename = ["cats.txt", "rats.txt", "dogs.txt"]
for files in filename:
    read_file(files)


filename = "nepal.txt"

with open(filename, encoding="utf-8") as np:
    content = np.read()
    words = content.count("Nepal")
    print(f"The text file contains {words} number of 'Nepal' in it. ")


