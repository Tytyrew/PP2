class StringHandler:
    def getString(self):
        self.mystring = input()
    def printString(self):
        print(self.mystring.upper())
s = StringHandler()
s.getString()
s.printString()