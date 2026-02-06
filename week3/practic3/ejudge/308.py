class Account:
    def __init__(self):
        self.owner = "NaN"
        self.balance = -1
    def deposit(self,B):
        self.balance = B
    def withdraw(self,W):
        if self.balance>=W:
            self.balance -= W
            return self.balance
        else:
            return "Insufficient Funds"
m = Account()
s = input().split(' ')
m.deposit(int(s[0]))
print(m.withdraw(int(s[1])))