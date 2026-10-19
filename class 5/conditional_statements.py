
battery=int(input("Enter your battery percentage."))
if battery<10:
    print("Charge your device.")

else:
    print("Use accordingly.")


# calculate the profit and loss

cost_price=float(input("Enter the actual price: "))
selling_price=float(input("Enter the selling price: "))

if (selling_price>cost_price):
    amount=selling_price-cost_price
    print("Total profit= ", amount)

else:
    print("No profit!")

# even and odd

number=int(input("Enter a whole number: "))

if number%2 == 0:
    print("This number is even.")

else:
    print("This number is odd.")

# diet plan

weight=int(input("Enter your weight: "))

if weight>80:
    print("Eat meals with less calories and do more exercise.")

if weight<30:
    print("Eat meals with more calories.")

else:
    print("Your weight is normal, you are healthy.")