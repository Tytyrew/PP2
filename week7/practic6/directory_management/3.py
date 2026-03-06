import os

for file in os.listdir("C:\\Users\\Acer\\Downloads"):
    if file.endswith(".txt"):
        print(file)