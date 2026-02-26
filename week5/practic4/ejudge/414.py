from datetime import datetime, timedelta
import sys

def parse(s):
    date_part, tz_part = s.strip().split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")

    sign = 1 if tz_part[3] == '+' else -1
    hh = int(tz_part[4:6])
    mm = int(tz_part[7:9])

    offset = timedelta(hours=hh, minutes=mm) * sign

    # локальная полночь -> UTC
    utc_time = dt - offset
    return utc_time

t1 = parse(sys.stdin.readline())
t2 = parse(sys.stdin.readline())

diff_seconds = abs((t2 - t1).total_seconds())
days = int(diff_seconds // 86400)

print(days)