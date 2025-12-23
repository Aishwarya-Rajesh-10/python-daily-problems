def perfect(num):
    if num<0:
        return False
    divisor=0
    for i in range(1,num):
        if num%i==0:
            divisor +=i
    return divisor==num
n=int(input("Enter a number:"))
if perfect(n):
    print("Perfect number")
else:
    print("Its not a perfect number")