def leapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

year = input("Enter a year: ")
if leapYear(int(year)):
    print(str(year), " is a leap year")
else:
    print(str(year), "is not a leap year")