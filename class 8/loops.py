# adding numbers using loop
num=int(input("Enter a number whose sum you want: "))

sum=0
for a in range(num):
    sum=a+sum
    print(sum)