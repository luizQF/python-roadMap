import datetime
 
date = datetime.date(2026, 1, 22) #year month day
today = datetime.date.today()

time = datetime.time(12, 30, 0) # 12:30:00
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S")
print(today)
print(now)

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = now

if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has not passed")
