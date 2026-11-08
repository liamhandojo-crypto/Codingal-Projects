# take user input
word=input("Enter your word: ")
char=input("Enter the character you want to find the number of times it appears: ")

# nested loop
i=0
count=0

while i<len(word):
    if word[i]==char:
        count=count+1
    i=i+1

print(char,"has appeared",count,"times in",word)
