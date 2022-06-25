grade = float(input())
# Check if grade is between 0 and 10
if 0 <= grade <= 10:
    # Check if grade rounded off to the nearest half point
    check = round(grade * 2) / 2
    if grade == check:
        # Grade A
        if grade <= 10 and grade >= 8.5:
            print("Grade A")
        if grade <= 8 and grade >= 7.5:
            print("Grade B")
        if grade <= 7 and grade >= 6.5:
            print("Grade C")
        if grade <= 6 and grade >= 5.5:
            print("Grade D")
        if grade < 5.5 and grade >= 0:
            print("Grade F")

    else:
        print("Grades should be rounded to the nearest half point.")
else:
    print("Grades should be between zero and 10.")