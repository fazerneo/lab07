with open("foo.txt", "r+") as textfile1, open("bar.txt", "a+") as textfile2:
    for line in textfile1:
        copyline = textfile1.read()
        for space in textfile2:
            space.write(copyline)