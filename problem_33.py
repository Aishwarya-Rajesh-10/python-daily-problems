N=input("Enter a sentence:")
vowels="aeiouAEIOU"
vowels_count=0
consonant_count=0
for char in N:
    if N.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonant_count+=1
print("Vowels:",vowels_count)
print("Consonants:",consonant_count)