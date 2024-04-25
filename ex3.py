import os

# get file size using path.getsize and printing it
initial_size = os.path.getsize("textfile.txt")
print(f"initial_size: {initial_size}")

# open a file in append mode so that file is not truncated. 
# read first line and next line, store them in a variable
# write an empty line and the stored line into the end of the file as it is in append mode
# offset to start of file and print line 1, 2, 3
with open("textfile.txt", "a+t") as textfile:
    copyline1 = textfile.readline()
    copyline2 = textfile.readline()

    textfile.write("")
    textfile.write(copyline1)
    textfile.write(copyline2)

    textfile.seek(0)
    print()
    print(f"line 1: {textfile.readline()}")
    print(f"line 2: {textfile.readline()}")
    print(f"line 3: {textfile.readline()}")

# get the new size of the file and print it out    
modified_filesize = os.path.getsize("textfile.txt")
print(f"modified_filesize: {modified_filesize}")