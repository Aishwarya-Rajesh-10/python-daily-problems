N=input("Enter a string:")
words=N.split()
largest_word=words[0]
for word in words:
    if len(word) > len(largest_word):
        largest_word=word
print("Largest word:",largest_word)