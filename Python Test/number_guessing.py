#variables
secret=40
c=5

#attempt counter
while c>=1:
    guess=int(input("Guess the number between 1-50: "))
    if guess==secret:
        print("You guessed the secret number! It is",secret)
        break
    else:
        print(guess,"is not the secret number.")
        c=c-1
        print("You have",c,"remaining ❤️ hearts.")


        

