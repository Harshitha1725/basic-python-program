# Even or Odd Number Checker

print("🔢 Even or Odd Number Checker")

try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"{number} is an EVEN number.")
    else:
        print(f"{number} is an ODD number.")

except ValueError:
    print("⚠ Please enter a valid integer number.")
