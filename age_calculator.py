# Age Calculator Program
# Created by Harshitha HM

print("🎂 Welcome to the Age Calculator!")

try:
    birth_year = int(input("Enter your birth year: "))
    current_year = int(input("Enter the current year: "))

    age = current_year - birth_year
    print(f"You are {age} years old. 🎉")

except ValueError:
    print("⚠️ Please enter valid numbers only!")