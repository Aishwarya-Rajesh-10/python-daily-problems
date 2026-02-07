N=list(map(int,input("Enter elements of list:").split()))
M=int(input("Enter the value of M:"))
missing=[]
for i in range(1,M+1):
    if i not in N:
        missing.append(i)
print("Missing numbers are:",missing)