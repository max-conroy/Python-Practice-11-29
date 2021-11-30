# Simple Python functions for the Per Scholas Cloud DevOps program and uploaded from Git
# Written by Maximilian Conroy
# 11/29/2021

import monday_assignments


def main():
    while True:
        inp = input("Enter 1 for ASCII characters program, 2 for math study tool, 3 for BMI calculator program, "
                    "4 for leap year program, 5 for chinese zodiac program, 6 for number guessing program, "
                    "7 for multiplication table, 8 for tuition calculator, or anything else to exit: ")
        print("")
        if inp == '1':
            print(monday_assignments.gen_letter())
        elif inp == '2':
            monday_assignments.math_tool()
        elif inp == '3':
            monday_assignments.bmi_calc()
        elif inp == '4':
            monday_assignments.is_leap_year()
        elif inp == '5':
            monday_assignments.chinese_zodiac()
        elif inp == '6':
            monday_assignments.guess_num()
        elif inp == '7':
            monday_assignments.multiplication_table()
        elif inp == '8':
            monday_assignments.tuition_calc()
        else:
            print("Exiting...")
            break
        print("")


# Run main function
if __name__ == '__main__':
    main()
