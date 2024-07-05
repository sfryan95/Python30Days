# Day 16: 30 Days of python programming

from datetime import datetime, date
now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                
minute = now.minute             
second = now.second

# print(day)
# print(month)
# print(year)
# print(hour)
# print(minute)
# print(second)

# %m/%d/%Y, %H:%M:%S

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

print(time_one)
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

past = date(year=1970, month=1, day=1)
today = date(year=2024, month=7, day=5)
time_left_for_newyear = today - past 
print(time_left_for_newyear)