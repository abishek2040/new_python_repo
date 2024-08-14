from name_function import get_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")

    # Above we checked that the program works as expected, takes in first and last name and provides a neatly formatted output. Now we will add a test case to make sure the program handles names correctly.
    # But testing a code manually can be very daunting, and we can automate this using tests in python.


    # The unittest module in python provides various tools in pth