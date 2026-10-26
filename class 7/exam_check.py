medical_cause=input("Do you have a medical cause? (Y/N) ").strip().upper()

# check eligibility
if medical_cause=='Y':
    print("You are allowed to take the exam.")

else:
    att=int(input("Enter your attendance in percentage. "))
    if (att>75):
        print("You are allowed to take the exam.")
    else:
        print("You are not allowed to take the examination due to your low attendance.")