# Check if a string is a palindrome.
a=input("Enter a string :- ")
x=a[::-1]
print(x)
if a==x:
    print("It is in palindrome")
else :
    print("it is not palindrome")