amount=int(input("Enter the total amount of money:"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10

print("100 rupees:", note_1)
print("50 rupees:", note_2)
print("10 rupees:", note_3)