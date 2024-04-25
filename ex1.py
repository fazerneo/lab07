# iterate over lines in a file in read mode, use line.isspace to ignore empty lines.
with open("textfile.txt", "r") as textfile:
    line_number = 1 
    for line in textfile:
        if line.isspace() == False:
            print(f"{line_number}. {line}")
            line_number += 1

