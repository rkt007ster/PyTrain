
#Task 2: Write and Append Data to a File

try:
    with open('output.txt','w') as file:
        file.write(input('Enter text to write to the file: ') + '\n')
        print('Data successfully written to the output.txt')
        file.close()
    with open('output.txt', 'a') as file:
        file.write(input('Enter additional text to append to the file: '))
        print('Data successfully appended to the output.txt')
        file.close()
    with open('output.txt', 'r') as file:
        print('Final Content of output.txt:\n',file.read())
        file.close()
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found")