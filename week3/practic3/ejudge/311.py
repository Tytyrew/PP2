class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        return self.first+self.second
inp = input().split()
a = Pair(int(inp[0]),int(inp[2]))
b = Pair(int(inp[1]),int(inp[3]))
print("Result: ",a.sum(),b.sum())