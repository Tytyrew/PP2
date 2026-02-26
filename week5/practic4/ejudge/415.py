from datetime import datetime, timezone, timedelta

def parse_utc_date(s):
    date_part, tz_part = s.split(" UTC")
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if tz_part[0] == '+' else -1
    hours = int(tz_part[1:3])
    minutes = int(tz_part[4:6])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=offset)

def next_birthday(birth_dt, current_dt):
    month, day = birth_dt.month, birth_dt.day
    current_utc = current_dt.astimezone(timezone.utc)
    
    def birthday_utc(year):
        # Handle Feb 29 birthdays
        try:
            bd = datetime(year, month, day, tzinfo=birth_dt.tzinfo)
        except ValueError:
            bd = datetime(year, 2, 28, tzinfo=birth_dt.tzinfo)
        return bd.astimezone(timezone.utc)
    
    bd_this_year = birthday_utc(current_dt.year)
    
    # Move to next year only if birthday has already passed in UTC
    if bd_this_year < current_utc:
        bd_this_year = birthday_utc(current_dt.year + 1)
    
    delta_seconds = int((bd_this_year - current_utc).total_seconds())
    return (delta_seconds + 86399) // 86400  # ceil division for partial days

birth = parse_utc_date(input())
current = parse_utc_date(input())
print(next_birthday(birth, current))