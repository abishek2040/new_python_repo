"""In this chapter we'll learn how to work with files, so that we can analyze a lots of data quickly.
In this chapter, we'll learn to read a file, or a text file, text files can contain a massive amount of data within it.
"""

# Here's how we open an entire file in python.

with open("pi_digits.txt") as pd:
    contents = pd.read()
print(contents)

# Let's breakdown the file, to do any work with a file, even just printing it's contents, you'll need to open the file
# first using the open() function, the open function returns a file, representing a file in this case pd.

# Reading line by line, to read a file line by line. You'll need to use a for loop with the file object. For eg:

with open("text.txt") as txt:
    for lines in txt:
        print(lines)
