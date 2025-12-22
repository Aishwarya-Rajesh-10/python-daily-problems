a=int(input("Enter a number:"))
order=len(str(a))
sum_of_powers=sum(int(digit)**order for digit in str(a))
if a==sum_of_powers:
    print(a,"is a amstrong number")
else:
    print(a,"is not a amstrong number")