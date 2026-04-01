month = int(input("Enter birth month:"))
day = int(input("Enter birth day:"))

from datetime import date 
today = date.today()
birthday = date(today.year, month, day)

if birthday < today:
    birthday = date(today.year +1, month, day)

num = (birthday - today).days
print(num, "days left till your birthday")