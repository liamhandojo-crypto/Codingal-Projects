# ask the user which vehicle they want
print("Select from the given choices.\n")
print("Enter 1 for bike\n")
print("Enter 2 for car\n")

# user input
choice=int(input("Enter your choice: "))

# user picks bike
if choice==1:
    print("Please choose a type of bike.\n")
    print("Enter 1 for bicycle.\n")
    print("Enter 2 for scooter.\n")
    print("Enter 3 for motorcycle.\n")
    subchoice=int(input("Enter your choice: "))
    if subchoice==1:
        print("You have chosen bicycle.")
    elif subchoice==2:
        print("You have chosen scooter.")
    elif subchoice==3:
        print("You have chosen motorcycle.")
    else:
        print("Wrong input!")

# user picks car
elif choice==2:
    print("Please choose a type of car.\n")
    print("Enter 1 for SUV.\n")
    print("Enter 2 for sedan.\n")
    print("Enter 3 for van.\n")
    subchoice=int(input("Enter your choice: "))
    if subchoice==1:
        print("You have chosen SUV.")
    elif subchoice==2:
        print("You have chosen sedan.")
    elif subchoice==3:
        print("You have chosen van.")
    else:
        print("Wrong input!")
else:
    print("Wrong choice!")

