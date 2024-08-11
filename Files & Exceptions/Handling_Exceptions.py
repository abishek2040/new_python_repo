# Here we create a program that uses the try-except block, to handle any errors tha may occur and halt the program.

print("Enter 2 numbers and we'll divide them, \nEnter 'q' to quit. ")
while True:
    first_number = input("Enter a number:")
    if first_number == "q":
        break
    second_number = input("Enter second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide a number by zero.")
    else:
        print(answer)


# Handling the FileNotFoundError Exception:
"""One common issue when working with files is handling missing files. The 
file you’re looking for might be in a different location, the filename may 
be misspelled, or the file may not exist at all. You can handle all of these 
situations in a straightforward way with a try-except block.
Let’s try to read a file that doesn’t exist. The following program tries 
to read in the contents of Alice in Wonderland, but I haven’t saved the file 
alice.txt in the same directory as alice.py"""

"""
filename = "alice.txt"

with open(filename, encoding="utf-8") as f:
    contents = f.read()
""" # The multiline commented piece of code is a program to read the contents of the file alice.txt, which doesn't exist
# Thus we use the try-except block again, to handle if such similar error occurs during the program.

filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry the file {filename} doesn't exist or may  have been deleted.")


# Analysing Text: Let's use exception and analyse the number of words in a text file.

filename = "words_alpha.txt"
try:
    with open(filename) as fn:
        content = fn.read()
except FileNotFoundError:
    print(f"The file {filename} could not be found or may have been deleted.")
else:
    # Count the approx number of words in the text file.
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has {num_words} words in it. ")

