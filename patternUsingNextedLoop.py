n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):       # Outer loop for rows
    for j in range(i):           # Inner loop for columns
        print("*", end="")      # Print star without newline
    print()                     # Move to next line after each row
