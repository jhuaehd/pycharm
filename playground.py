def myFunc(x, y = 20):  # Now we must always pass x
    print(x + y)

myFunc(12)  # Prints 18
myFunc(10,10)  # Prints 20
