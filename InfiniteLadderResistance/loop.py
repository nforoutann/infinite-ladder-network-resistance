def calculate_req(R1, R2, tolerance=1e-6, max_iterations=1000):
    # Initialize R_eq with an arbitrary guess, say 2 ohms
    R_eq = 2.0
    iteration = 0

    while iteration < max_iterations:
        # Calculate the new R_eq using the recursive formula
        new_R_eq = R1 + (R2*R_eq)/(R2+R_eq)

        # Check if the difference between the new and old value is within the tolerance
        if abs(new_R_eq - R_eq) < tolerance:
            break

        # Update the equivalent resistance for the next iteration
        R_eq = new_R_eq
        iteration += 1

    # Return the final value of R_eq
    return R_eq


# Run the function and print the result
R1 = int(input('Please Enter The Value of R1: '))
R2 = int(input('Please Enter The Value of R2: '))
equivalent_resistance = calculate_req(R1, R2)
print(f"Equivalent resistance of the infinite ladder network: {equivalent_resistance:.6f} ohms")