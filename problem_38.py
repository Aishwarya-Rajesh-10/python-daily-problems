N=input("Enter a first word:")
S=input("Enter a second word:")
N=N.lower()
S=S.lower()
N=N.replace(" ","")
S=S.replace(" ","")
if len(N)!=len(S):
    print("Not Anagrams")
else:
    freq1=dict()
    freq2=dict()
    for char in N:
        if char in freq1:
            freq1[char]+=1
        else:
            freq1[char]=1
    for char in S:
        if char in freq2:
            freq2[char]+=1
        else:
            freq2[char]=1
    if freq1==freq2:
        print("Anagrams")
    else:
        print("Not Anagrams")