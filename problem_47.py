N=list(map(int,input("Enter the elements of first list:").split()))
S=list(map(int,input("Enter the elements of second list:").split()))
common=[]
for digit in N and S:
    if digit in N:
        if digit in S:
            common.append(digit)
print("Common elements are:",common)