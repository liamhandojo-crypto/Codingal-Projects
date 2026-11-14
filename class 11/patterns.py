#take user input
print("Half pyramid pattern")
r=int(input("Enter the number of rows you want:"))

#print the pattern using nested loops
for i in range(r):
    for a in range(i+1):
       print("*",end=" ")

    print()