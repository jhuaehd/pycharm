

username = ['Josh', 'Anjo', 'Wendell']
passwords = ['coreuser11', 'gamer', 'offlane']

print("====================\n\tLOGIN")


attempt_username = 3
while attempt_username > 0:
    attempt = 3
    userInput = input("Please input your username: ")
    if userInput in  username:
        passInput = input("Please input your password: ")
        match = username.index(userInput)
        if passInput == passwords[match]:
            print("Successfully login !", userInput)
        else:
            attempt = attempt - 1
            print("Wrong password or username")
            print("Attempts: ", attempt)

    else:
        attempt_username = attempt_username - 1
        print("Wrong password or username")
        print("Attempts: ", attempt_username)
else:
    print("Try again later ")