# dates & times

import datetime

date = datetime.date(2025, 1, 2)
date = datetime.date.today()

time = datetime.time(12, 30)
now = datetime.datetime.now()

now = now.strftime("%I:%M %p")

target_datetime = datetime.datetime(2025, 1, 2, 12, 30)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has not passed")