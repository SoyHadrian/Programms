def divisible4(year):
    if year % 4 == 0:
        return True
    else:
        return False

def divisible100(year):
    if year % 100 ==0:
        return True
    else:
        return False

def divisible400(year):
    if year % 400 == 0:
        return True
    else:
        return False

def leapyear(year):
    if divisible4(year) and divisible100(year) and divisible400(year):
        print(str(year) + ", is a Leap year")
    else:
        print(str(year) + ", is a Leap year")

year = input("Enter a number: ")
leapyear(int(year))