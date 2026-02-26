import datetime
def total_seconds(x):
    return x.second + 60*(x.minute + 60*(x.hour + 24*x.day))
l = datetime.datetime.now()
r = datetime.datetime.now()
print(total_seconds(r)-total_seconds(l))