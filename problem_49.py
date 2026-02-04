N=list(map(int,input("Enter elements of list:").split()))
freq={}
for item in N:
    if item in freq:
        freq[item]+=1
    else:
        freq[item]=1
print(freq)