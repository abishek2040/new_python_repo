# In this program,we move the bulk of the previously written program into a function, so that it is easy to analyze
# multiple books.

def count_words(filename):
    """A function that takes in a text file and returns number of words in it."""
    try:
        with open(filename) as fn:
            content = fn.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist or may have been deleted.")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {filename} has {num_words} words in it.")

filename = ["words_alpha.txt", "words_alpha2.txt", "words_alpha4.txt", "words_alpha3.txt"]
for files in filename:
    count_words(files)


# Failing silently
# In the previous examples we informed the users what was wrong when the program stopped, but we can also have the
# program to fail silently, without displaying any error messages, by just adding a pass after the except block, which
# will make the program continue running, even if an error is recorded.

# For example:

print("\n\nWe are going to try to open a file that doesn't exist, and fail silently without showing any error: ")

try:
    with open("doesntexist.txt") as fi:
        content = fi.read()
except FileNotFoundError:
    pass
# This gives no output and the program ends.