import re
with open("C:\\Users\\Acer\\Documents\\MyProects\\Python projects\\PP2\\week6\\practic5\\raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
name = re.findall("[А-ЯA-Z].+\n[0-9,]+ x [0-9,]+",text)
amount = []
price = []
sum = 0.0
#task 1,2
for i in range(len(name)):
    proc = re.search("\n[0-9,]+ x [0-9,]+",name[i]).group().split(' x ')
    amount.append(float(re.sub(",",".",proc[0])))
    price.append(float(re.sub(",",".",proc[1])))
    name[i]=re.search("[A-Za-zА-Яа-я ]+",name[i]).group()
#task 3
for i in range(len(price)): sum += (price[i]*amount[i])
#task 4
d = re.findall("[0-9:.]+",re.search("Время:[^\n]+",text).group())
dicd = {"products" : {},"datetime": d}
for i in range(len(name)): dicd["products"][name[i]] = [price[i],amount[i]]
print(dicd)