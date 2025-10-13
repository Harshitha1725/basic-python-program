# Multiplication Table Generator
# Created by Harshitha HM

print("📘 Multiplication Table Generator")

try:
    num = int(input("Enter a number to generate its multiplication table: "))

    print(f"\nMultiplication Table for {num}:\n")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("⚠ Please enter a valid integer number.")
