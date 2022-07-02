

username = ['Josh', 'Anjo', 'Wendell']
passwords = ['coreuser11', 'gamer', 'offlane']

print("====================\n\tLOGIN")


attempt = 3
while attempt > 0:
    userInput = input("Please input your username: ")
    passInput = input("Please input your password:")
    if userInput in  username:
        match = username.index(userInput)
        if passInput == passwords[match]:
            print("Successfully login !", userInput)
        else:
            attempt = attempt - 1
            print("Wrong password or username")
            print("Attempts: ", attempt)

    else:
        attempt = attempt - 1
        print("Wrong password or username")
        print("Attempts: ", attempt)

else:
    print("Try again later ")