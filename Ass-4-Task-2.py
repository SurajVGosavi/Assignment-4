
# Task 2: Write and Append Data to a File
try:
    file1 =  open('output.txt','a')
    text = input("Enter text to write to the file: ")
    writefile = file1.write(text + "\n")
    print("Data successfully written to output.txt.\n")
    file1.close()
except FileNotFoundError:
    print("Error : The file 'sample.txt' was not found")
finally:
    file1 = open('output.txt', 'a')
    text2 = input("Enter additional text to append: ")
    writefile = file1.write(text2)
    print("Data successfully appended.\n")
    file1.close()

    file1 = open('output.txt', 'r')
    readfile = file1.read()
    print("Final Content of output.txt")
    print(readfile)
    file1.close()