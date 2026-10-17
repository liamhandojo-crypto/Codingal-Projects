print("Enter marks obtained in 4 subjects\n")
math=int(input("Math= "))
english=int(input("English= "))
science=int(input("Science= "))
chinese=int(input("Chinese= "))

# find the total of all subjects
total=chinese+english+math+science
print("This is the total of 4 subjects:" ,total)

# find the average of marks
avg=total/4
print("This is the average marks:", avg)

percentage=(total/400)*100
print("Your percentage: ", percentage,"%")