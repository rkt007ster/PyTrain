
#Task 1: Read a File and Handle Errors

try:
    with open('sample.txt', 'r') as file:
        print('Line 1: ',file.readline())
        print('Line 2: ',file.readline())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")

