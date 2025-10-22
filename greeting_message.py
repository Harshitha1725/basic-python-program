# Greeting Message Generator
# Created by Harshitha HM

print("👋 Welcome to the Greeting Message Generator!")

name = input("Enter your name: ")
time = input("Enter time of the day (morning/afternoon/evening): ").lower()

if time == "morning":
    print(f"🌞 Good morning, {name}! Have a bright day ahead!")
elif time == "afternoon":
    print(f"☀️ Good afternoon, {name}! Keep up the great energy!")
elif time == "evening":
    print(f"🌙 Good evening, {name}! Hope you had a wonderful day!")
else:
    print(f"💫 Hello {name}! Have a great time!")