N=input("Enter a string:")
vowels="aeiouAEIOU"
for v in vowels:
    N=N.replace(v,"*")
print("clean text",N)