N=list(map(int,input("Enter a list:").split()))
largest=second_largest=float('-inf')
for num in N:
    if num>second_largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num!=largest:
        second_largest=num
print("Second largest number is:",second_largest)