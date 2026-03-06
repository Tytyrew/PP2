import os
def deleteuwu(s):
    if os.path.exists(s):os.remove(s)
    else: return "The file does not exist"
p1 = "C:\\Users\\Acer\\Documents\\MyProects\\Python projects\\PP2\\week7\\practic6\\file_handling\\67.txt"
p2 = "C:\\Users\\Acer\\Documents\\MyProects\\Python projects\\PP2\\week7\\practic6\\file_handling\\69.txt"
deleteuwu(p1)
deleteuwu(p2)