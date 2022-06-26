import datetime


# user commands
command = ['Hello Jarvis',
           'Jarvis, what time is it?',
           'Jarvis, how\'s the waether today?',
           'Can you visit google.com?',
           'Jarvis, say HI!'
           ]

# jarvis responses
jarvis_response = ['How may I help you sir?',
                   ''
                   ]

# introduction to system
print("Hello, I am Jarvis you computer assistant.")

# get the user's name
your_name = input('May I know you name sir ?\n')
print("Hello sir",your_name)


print("Jarvis will follow for the selected commands, please type -c , or else jarvis will not execute.")
# for command's list

attempt = 5
while attempt > 0:
    # this is for printing the commands list for jarvis
    command_list = input()
    if command_list == '-c':
        for c in command:
            print(c)
        print("\n")
        print("<====================>")
        # this is for the jarvis response starts
        print(jarvis_response[0])

        # loop starts here
        user_input = input()
        while user_input.lower() != 'exit':
            if user_input in command:
                # this will get the index of the command and that index to retrieve jarvis response..
                print(jarvis_response[command.index(user_input)])
                break
            else:
                print("Invalid command")
        else:
            print("Thank you sir. Good bye !")

    else:
        attempt = attempt - 1
        print("Please type -c")

else:
    print("Jarvis shutting down. . .")






