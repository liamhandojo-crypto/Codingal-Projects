# take user input to find out weight and height
weight=float(input("Enter your weight in kg: "))
height=float(input("Enter your height in cm : "))

# calculate BMI
bmi= weight/(height/100)**2
print("Your BMI is", bmi)

# make a chart
if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are severely overweight.")
elif bmi <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese. Do some exercise.")