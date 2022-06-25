num = int(input())
fact = 1

if num > 10:
    print()
else:
    for i in range(1, num + 1):
        fact = fact * i

    print(fact)