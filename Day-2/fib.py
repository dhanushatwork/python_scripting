n = int(input("Enter the number of terms: "))

# Validate input
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two terms
    a, b = 0, 1
    count = 0

    print("Fibonacci Sequence:")
    while count < n:
        print(a, end=" ")
        # Update values for the next iteration
        a, b = b, a + b
        count += 1
