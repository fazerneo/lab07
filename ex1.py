with open("textfile.txt", "r") as textfile:
    line_number = 1 
    for line in textfile:
        if line.isspace() == False:
            print(f"{line_number}. {line}")
            line_number += 1

