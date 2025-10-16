# Positive or Negative Number Checker
# Created by Harshitha HM

print("🔢 Positive or Negative Number Checker")

try:
    number = float(input("Enter any number: "))

    if number > 0:
        print(f"{number} is a Positive number ✅")
    elif number < 0:
        print(f"{number} is a Negative number ❌")
    else:
        print("The number is Zero ⚪")

except ValueError:
    print("⚠️ Please enter a valid number!")