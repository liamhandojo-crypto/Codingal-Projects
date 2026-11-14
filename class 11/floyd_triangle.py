#take user input
row=int(input("Enter the number of rows you want: "))
num=1

#print the triangle
for i in range(1,row+1):
    for a in range(1,i+1):
        print(num, end=" ")
        num=num+1

    print()
