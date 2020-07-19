year= int(input("Please write a 4-digit year:"))

a=year%400==0

b=year%100==0

c=year%4==0
if (c and (not b) or a):
    print(year, "is a leap year")
else:
    print(year, 'is not a leap year')