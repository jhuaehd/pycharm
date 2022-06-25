
lives = 5
CorrectAns = 24

while lives > 0:
    userAns = int(input("How many hours in one day ? \n"))
    if userAns == 24:
        print("CONGRATS! You won")
        break
    else:
        lives = lives - 1
        print("Remaining lives : " +str(lives))
else:
    print("You lose")