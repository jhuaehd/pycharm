
athleteOne = int(input())
athleteTwo = int(input())
athleteThree = int(input())

total = (athleteOne + athleteTwo + athleteThree) / 60

minutes = total*60
minutes, seconds = divmod(minutes, 60)

print("%2d:%02d"%(minutes, seconds))
