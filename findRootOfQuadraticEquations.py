import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
elif discriminant > 0:
    # Two distinct real roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are real and different:\nRoot 1 = {root1}\nRoot 2 = {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print(f"Roots are real and same:\nRoot = {root}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Roots are complex:\nRoot 1 = {real_part} + {imaginary_part}i\nRoot 2 = {real_part} - {imaginary_part}i")
