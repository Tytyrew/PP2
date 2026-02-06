class Employee:
    def __init__(self,type,name,base_salary,bonus_percent):
        self.type = type
        self.name = name
        self.base_salary = base_salary
        self.bonus_percent = bonus_percent
    def out(self):
        res = float(0)
        if self.type=='Manager':
            res = self.base_salary*(1 + self.bonus_percent/100)
        else:
            res = self.base_salary + self.bonus_percent*500
        print('Name: ',self.name,', Total: ',f"{res:.2f}",sep='')
s = input().split(' ')
if len(s)==3: s.append(0.00)
p = Employee(s[0],s[1],float(s[2]),float(s[3]))
p.out()
