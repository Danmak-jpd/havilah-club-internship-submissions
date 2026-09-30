# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# EXERCISE 1: VARIABLES AND DATA TYPES
student_name = "Daniel"
age = 25
average_score = 85.5
is_engineering_student = True

print("Student Name:", student_name)
print("Data type:", type(student_name))

print("Age:", age)
print("Data type:", type(age))

print("Average Score:", average_score)
print("Data type:", type(average_score))

print("Engineering Student:", is_engineering_student)
print("Data type:", type(is_engineering_student))


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO:# EXERCISE 3: TEMPERATURE CONVERTER
# Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("\n===== CELSIUS TO FAHRENHEIT =====")
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)


# Convert Fahrenheit to Kelvin

fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))

kelvin = (fahrenheit_input - 32) * 5 / 9 + 273.15

print("\n===== FAHRENHEIT TO KELVIN =====")
print("Fahrenheit:", fahrenheit_input)
print("Kelvin:", kelvin)


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# EXERCISE 2: TWO NUMBER CALCULATOR

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

sum_result = first_number + second_number
difference = first_number - second_number
product = first_number * second_number

print("\n===== CALCULATION RESULTS =====")

print("First Number:", first_number)
print("Second Number:", second_number)
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)

if second_number != 0:
    quotient = first_number / second_number
    remainder = first_number % second_number

    print("Quotient:", quotient)
    print("Remainder:", remainder)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot divide by zero")
