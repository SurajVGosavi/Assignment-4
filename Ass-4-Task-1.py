# Task 1: Read a File and Handle Errors
try:
    file1 =  open('sample.txt','r')
    readfile = file1.readlines()
    print("Reading The File Content:")
    print("Line 1:",readfile[0])
    print("Line 2:",readfile[1])
    file1.close()
except FileNotFoundError:
    print("Error :: The file 'sample.txt' was not found")