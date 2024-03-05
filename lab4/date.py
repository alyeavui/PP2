#1
from datetime import datetime, timedelta

current = datetime.now()
new = current - timedelta(days = 5)
print(new.strftime("%d.%m.%Y"))

#2
today = datetime.now()
day = timedelta(days = 1)
yesterday = today - day
tomorrow = today + day
print("Yesterday: ", yesterday.strftime("%d.%m.%Y"))
print("Today: ", today.strftime("%d.%m.%Y"))
print("Tomorrow: ", tomorrow.strftime("%d.%m.%Y"))

#3
noMicroSeconds = current.replace(microsecond = 0)
print(noMicroSeconds)

#4
date1_str = input()
date2_str = input()
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
difference = date1 - date2
inSeconds = abs(difference.total_seconds())
print(inSeconds)

