print("✨ Welcome to Basic Python Program ✨\n")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"\nHello {name}! You are {age} years old.")

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print(f"The sum of {a} and {b} is {a + b}")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i, end=' ')

def greet(person):
    return f"\n\nHave a great day, {person}!"

print(greet(name))
