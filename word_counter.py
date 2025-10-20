# Word Counter Program
# Created by Harshitha HM

print("📝 Word Counter Program")

text = input("Enter a sentence: ")

# Split the text into words
words = text.split()

# Count the number of words
word_count = len(words)

print(f"Your sentence has {word_count} words.")