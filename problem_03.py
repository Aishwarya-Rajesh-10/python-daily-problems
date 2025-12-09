a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print("Largest number is a",a)
elif b>a and b>c:
    print("Largest number is b",b)
elif c>a and c>b:
    print("Largest number is c",c)
else:
    print("You have entered a invalid number")