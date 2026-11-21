#define 2 functions
def add(A,B):
    return A+B
def sub(A,B):
    return A-B

#user input
print("Please select an operation.")
print("a. Addition")
print("b. Subtraction")

choice=input("Please enter your choice: ")
num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))

#if statement
if choice=="a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice=="b":
    print(num_1,"-",num_2,"=",sub(num_1,num_2))
