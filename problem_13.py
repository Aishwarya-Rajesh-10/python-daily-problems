start=int(input("Enter the starting range:"))
end=int(input("Enter the ending range:"))
print("prime numbers are in range :")
for i in range(start,end+1):
    if i>1:
        for num in range(2,int(i**0.5)+1):
            if i%num==0:
                break
        else:
            print(i,end="")