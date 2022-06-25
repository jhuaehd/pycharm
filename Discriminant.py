import math

a = int(input())
b = int(input())
c = int(input())

# calculating  the discriminant
dis = (b ** 2) - (4 * a * c)

if a == 0 and b == 0:
    print("There is not even an unknown in this equation!")

if dis > 0:
    solution_one = (-b + math.sqrt(dis)) / (2 * a)
    solution_two = (-b - math.sqrt(dis)) / (2 * a)
    print(f"There are two solutions , namely {solution_one} and {solution_two}")
    # print("There are two solutions , namely {:.16f} and {:.16f}".format(solution_one, solution_two))
elif dis == 0:
    solution_one = (-b + math.sqrt(dis)) / (2 * a)
    print(f"There is one solution , namely {solution_one}")
else:
    print("There are no solutions")
