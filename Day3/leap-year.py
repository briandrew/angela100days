'''
Write a program that works out whether a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 

Leap Year Rules:

1. every year that is evenly divisible by 4 

2. **except** every year that is evenly divisible by 100 

3. **unless** the year is also evenly divisible by 400

e.g. The year 2000: 2000 ÷ 4 = 500 (Leap) -> 2000 ÷ 100 = 20 (Not Leap) -> 2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap) -> 2100 ÷ 100 = 21 (Not Leap) -> 2100 ÷ 400 = 5.25 (Not Leap)

'''
year = int(input("Please enter a year: "))
div_by_4 = year % 4
div_by_100 = year % 100
div_by_400 = year % 400

if div_by_4 == 0:
    if div_by_100 != 0:
        print("Leap year.")
    else:
        if div_by_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
else:
    print("Not leap year.")
