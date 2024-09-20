import math

# Given values for the resistors
R1 = int(input('Please Enter The Value of R1: '))
R2 = int(input('Please Enter The Value of R2: '))

# Coefficients for the quadratic equation ax^2 + bx + c = 0
a = 1  # Coefficient of R_eq^2
b = -R1  # Coefficient of R_eq
c = -R1 * R2  # Constant term

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c

# Check if the discriminant is non-negative (there must be real solutions)
if discriminant >= 0:
    # Calculate the two possible solutions using the quadratic formula
    R_eq1 = (-b + math.sqrt(discriminant)) / (2 * a)
    R_eq2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # We are interested in the positive real solution for the equivalent resistance
    R_eq = max(R_eq1, R_eq2)

    # Print the result
    print(f"The equivalent resistance of the infinite ladder network is: {R_eq} ohms")
else:
    print("No real solution exists.")