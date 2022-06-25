grade = float(input())
# Check if grade is between 0 and 10
if 0 <= grade <= 10:
    # Check if grade rounded off to the nearest half point
    check = round(grade * 2) / 2
    if grade == check:
        # Grade A
        if 10 >= grade >= 8.5:
            print("Grade A")
        if 8 >= grade >= 7.5:
            print("Grade B")
        if 7 >= grade >= 6.5:
            print("Grade C")
        if 6 >= grade >= 5.5:
            print("Grade D")
        if 5.5 > grade >= 0:
            print("Grade F")

    else:
        print("Grades should be rounded to the nearest half point.")
else:
    print("Grades should be between zero and 10.")