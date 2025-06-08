# Check if a year is a leap year.
a=(int(input("Enter a year u want to search :- ")))
if (a%4==0 and a%100==0) or a%400==0:
    print('It is a leap year')