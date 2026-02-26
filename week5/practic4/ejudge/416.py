from datetime import datetime, timezone, timedelta

# Read input
start_str = input()
end_str = input()

def parse_utc_time(s):
    # Split into datetime part and UTC offset part
    dt_part, tz_part = s.split(" UTC")
    dt = datetime.strptime(dt_part, "%Y-%m-%d %H:%M:%S")
    # Parse offset ±HH:MM
    sign = 1 if tz_part[0] == '+' else -1
    hours = int(tz_part[1:3])
    minutes = int(tz_part[4:6])
    offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=offset)

start_dt = parse_utc_time(start_str)
end_dt = parse_utc_time(end_str)

# Compute duration in seconds
duration = int((end_dt.astimezone(timezone.utc) - start_dt.astimezone(timezone.utc)).total_seconds())
print(duration)