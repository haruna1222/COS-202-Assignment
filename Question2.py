print("=" * 55)
print("      STUDENT CGPA CALCULATOR")
print("=" * 55)

while True:

    total_courses = int(input("\nEnter Total Number of Courses: "))

    total_credit = 0
    total_grade = 0

    for item in range(total_courses):

        print(f"\nCourse {item + 1}")

        credit = int(input("Credit Unit: "))
        score = int(input("Score Obtained: "))

        match score:

            case x if 70 <= x <= 100:
                gp = 5
                grade = "A"

            case x if 60 <= x <= 69:
                gp = 4
                grade = "B"

            case x if 50 <= x <= 59:
                gp = 3
                grade = "C"

            case x if 45 <= x <= 49:
                gp = 2
                grade = "D"

            case x if 40 <= x <= 44:
                gp = 1
                grade = "E"

            case x if 0 <= x <= 39:
                gp = 0
                grade = "F"

            case _:
                print("Score is not valid.")
                continue

        weighted_point = credit * gp

        total_credit += credit
        total_grade += weighted_point

        print("Letter Grade :", grade)
        print("Weighted Point :", weighted_point)

    cgpa = total_grade / total_credit

    print("\n******** FINAL RESULT ********")
    print("Total Credit Units :", total_credit)
    print("Total Weighted Points :", total_grade)
    print("Calculated CGPA :", round(cgpa, 2))
    print("******************************")

    response = input("\nWould you like to calculate again? (Y/N): ").upper()

    match response:
        case "Y":
            continue
        case "N":
            print("\nGoodbye!")
            break
        case _:
            print("\nInvalid option. Program terminated.")
            break