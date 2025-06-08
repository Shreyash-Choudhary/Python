# Write a simple calculator using if-else. 
a=(int(input("Enter a 1st number :- ")))
b=(int(input("Enter a 2nd number :- ")))
x=(input("Enter a operation which we want to perform like we have (*,+,-,/) :- "))

if x== "+" :
    print(a+b)

elif x== "-" :
    print(a-b)

elif x=="*":
    print(a*b)

elif x== "/ ":
    print(a/b)

else:
    print("plz enter a valid input")
