# reversing a string using loop
word=input("Enter your word: ")

string=('')
for i in word:
    string=i+string

print("The original word is:",word)
print("The reversed word is:",string)
