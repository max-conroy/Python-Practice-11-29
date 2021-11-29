# Simple Python functions for the Per Scholas Cloud DevOps program and uploaded from Git
# Written by Maximilian Conroy
# 11/29/2021

import random


# Generate a random character between given set of ASCII characters
def gen_letter():
    print("This program will generate a random lowercase letter between given set of ASCII characters.")
    start = input("Enter starting character: ")
    end = input("Enter ending character: ")
    return chr(random.randint(ord(start), ord(end)))


# The program randomly generates two single-digit
# integers number1 and number2. User can answer the sum
# and program will return whether user's answer was true/false.
# If user's answer is false, loop until answer is correct or user exits.
def math_tool():
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    while True:
        inp = input(f"What is {a} + {b}? ")
        ans = a + b
        if int(inp) == ans:
            print("Correct!")
            break
        else:
            print(f"Sorry, please try again: ")


# Calculate BMI by taking user's weight in pounds and dividing by the square of your height in inches.
# Program then outputs BMI category based on the following chart:
# BMI < 18.5 Underweight
# 18.5 <= BMI < 25.0 Normal
# 25.0 <= BMI < 30.0 Overweight
# 30.0 <= BMI Obese
def bmi_calc():
    print("This program will calculate BMI based on your weight and height.")
    height = int(input("Please enter your height in inches: "))
    weight = int(input("Please enter your weight in pounds: "))
    bmi = 703 * (weight / (height ** 2))
    bmi = round(bmi, 2)
    print(f"Your BMI is {bmi}")
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25.0:
        category = "Normal"
    elif 25.0 <= bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Your BMI category is {category}")


# Prompt for a year and output if it is a leap year
def is_leap_year():
    print("This program determines whether a given year is a leap year.")
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


# Prompt for a year and output the corresponding chinese zodiac animal
def chinese_zodiac():
    print("This program displays the chinese zodiac animal for the year entered.")
    year = input("Please enter a year: ")
    ind = int(year) % 12
    arr = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]
    print(f"The animal for {year} is {arr[ind]}")


def guess_num():
    num = random.randint(0, 101)
    print("This program randomly generates a number from 0 to 100.")
    print(num)
    while True:
        guess = input("Please guess a number: ")
        if int(guess) == num:
            print("Correct!")
            break
        else:
            print("Incorrect, please try again")


def multiplication_table():
    while True:
        n = int(input("Enter the table size for the NxN multiplication table (N must be between 0 and 31: "))
        if 0 < n <= 31:
            break
        else:
            print("N must be between 0 and 31, please enter another number.")

    # add 2 to n to allow for extra rows and columns
    n += 2

    # Use list comprehension to initialize multidimensional list to represent the table
    arr = [['0'] * n for i in range(n)]

    # Set 0,0 of table to X
    arr[0][0] = '  X'

    # Set first row and column to 0 through n
    for x in range(1, n):
        # Add spaces before numbers to evenly print table
        arr[0][x] = f"  {x - 1}" if x <= 10 else f" {x - 1}"
        arr[x][0] = f"  {x - 1}" if x <= 10 else f" {x - 1}"

    # Iterate through N to populate multidimensional list with products
    for i in range(1, n):
        for j in range(1, n):
            temp = (i - 1) * (j - 1)
            # Determine amount of spaces to add before products to evenly print table
            if int(temp) < 10:
                # 2 spaces
                arr[i][j] = f"  {temp}"
            elif 10 <= int(temp) < 100:
                # 1 space
                arr[i][j] = f" {temp}"
            if 100 <= int(temp):
                # 0 spaces
                arr[i][j] = f"{temp}"

    # Print table
    for i in range(0, n):
        print(arr[i])


# Prompt for tuition and yearly rate, output years until the tuition has doubled
def tuition_calc():
    # Initialize with default values
    start = 10000.00
    rate = 1.07
    years = 0

    # Allow user to overwrite default values
    if 'y' == input("Would you like to enter your own tuition and percent increases per year (y/n)? ").lower():
        start = int(input("Enter starting tuition: "))
        rate = float(input("Enter yearly tuition increase in decimal (i.e. 1.07 for 7% increase) "))

    # Loop until tuition has doubled
    current = start
    while current < (start * 2):
        current *= rate
        years += 1

    # Print results
    start = round(start, 2)
    current = round(current, 2)
    print(f"Your tuition of ${start} will be doubled to ${current} in {years} years, at a rate of {rate} per year.")


def main():
    while True:
        inp = input("Enter 1 for ASCII characters program, 2 for math study tool, 3 for BMI calculator program, "
                    "4 for leap year program, 5 for chinese zodiac program, 6 for number guessing program, "
                    "7 for multiplication table, 8 for tuition calculator, or anything else to exit: ")
        print("")
        if inp == '1':
            print(gen_letter())
        elif inp == '2':
            math_tool()
        elif inp == '3':
            bmi_calc()
        elif inp == '4':
            is_leap_year()
        elif inp == '5':
            chinese_zodiac()
        elif inp == '6':
            guess_num()
        elif inp == '7':
            multiplication_table()
        elif inp == '8':
            tuition_calc()
        else:
            print("Exiting...")
            break
        print("")


# Run main function
if __name__ == '__main__':
    main()
