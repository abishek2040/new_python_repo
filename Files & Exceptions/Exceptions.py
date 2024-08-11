"""Python uses special objects called exceptions to handle errors that may arise during a program's execution. Whenever
an error occurs that makes python unsure what to do next, it creates an exception object. If you write code that handles
the exception object, the program will continue running. If you don't write a code to handle the exception then it will
halt and show a traceback. Tracebacks are pythons error message, that may be confusing for normal users.

Exceptions in python are handled using the try-except blocks. A try-except block asks python to do something, but it
also tells python what to do if an exception is raised. When you use try-except blocks, your program will continue to
run even things start to go wrong. Instead of tracebacks, which are really confusing for users, we can show friendly
error messages. """

# Here's an example of handling errors in python: The zero divison error.
"""As we know that a number cannot be divided by zero, and results in an error, let's divide a number by zero in python.
"""

#print(5/0) # We get the error, ZeroDivisionError
# Here we are using try-except blocks to handle the error(ZeroDivisionError)

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide a number by 0.")

# Using exceptions to prevent crashes Example :

print("Enter two numbers to divide them \nEnter 'q' to quit. ")

while True:
    first_number = input("Enter the first number: ")
    if first_number == "q":
        print("Thank you")
        break

    second_number = input("Enter the second number: ")
    if second_number == "q":
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# The above program doesn't handle errors in anyways, and it just crashes and stops, when it encounters an error.
# Let's use exceptions so that it can run even though it encounters errors in the program.

"""We are going to create the program in another file named handling_exception.py."""