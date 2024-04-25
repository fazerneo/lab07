# Copyting text from foo.txt to bar.txt
with open("foo.txt", "r") as textfile1, open("bar.txt", "w+") as textfile2:
    copyline = textfile1.read()
    textfile2.write(copyline)
