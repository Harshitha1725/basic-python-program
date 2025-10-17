# Temperature Converter
# Created by Harshitha HM

print("🌡️ Temperature Converter")

print("1️⃣ Convert Celsius to Fahrenheit")
print("2️⃣ Convert Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

try:
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("⚠️ Invalid choice. Please enter 1 or 2.")
except ValueError:
    print("⚠️ Please enter a valid number.")