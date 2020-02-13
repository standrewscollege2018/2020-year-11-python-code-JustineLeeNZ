''' displays the appropriate grade for a mark entered by the user '''

# grade boundaries
A_GRADE_BOUNDARY = 90
B_GRADE_BOUNDARY = 70
C_GRADE_BOUNDARY = 50

# max and min marks
MAX_GRADE = 100
MIN_GRADE = 0

# get mark to be checked
mark = int(input("Enter the mark to check:"))

# check if mark with valid range
if mark <= MAX_GRADE and mark >= MIN_GRADE:
    # check what grade matches the mark that was entered
    if mark >= A_GRADE_BOUNDARY:
        print("A")
    elif mark >= B_GRADE_BOUNDARY:
        print("B")
    elif mark >= C_GRADE_BOUNDARY:
        print("C")
    else:
        print("You failed")
else:
    print("Invalid mark")