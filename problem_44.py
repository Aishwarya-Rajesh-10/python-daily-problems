N=list(map(int,input("Enter the elements of list:").split()))
S=[]
for digit in N:
    if digit not in  S:
        S.append(digit)
print(S)