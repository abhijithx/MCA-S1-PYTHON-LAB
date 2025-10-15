s = input("Enter a string: ")

if len(s) <= 1:
    # If string has 0 or 1 character, it stays the same
    result = s
else:
    # Swap first and last characters
    result = s[-1] + s[1:-1] + s[0]

print("String after swapping first and last characters:", result)
