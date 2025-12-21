n=int(input("Enter a number:"))
def fib(n):
    a=0
    b=1
    if n==1:
        print(n)
    else:
        print(0)
        print(1)
        for i in range (2,n):
            c=a+b
            b=a
            a=c
            print(c)
fib(n)