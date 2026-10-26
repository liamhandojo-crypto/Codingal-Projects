units=int(input("Enter the amount of units you used: "))

if units<50:
    surcharge=0
    print("There will be no surcharge on your bill.")

elif units<=100:
    surcharge=35
    
elif units<=200:
    surcharge=50
    
elif units<=300:
    surcharge=75
    
else:
    surcharge=100
    
print("The surcharge is $",surcharge)