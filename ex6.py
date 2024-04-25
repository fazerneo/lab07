import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("lab07")
print(os.listdir("."))