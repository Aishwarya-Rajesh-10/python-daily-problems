N=list(map(int,input("Enter the elements of list:").split()))
k=int(input("Enter number of position you want to shift:"))
k=k%len(N)
rotated=N[-k:]+N[:-k]
print("Rotated list:",rotated)