# Ask the user to input a positive integer
n = int(input("Enter a positive integer: "))

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Collatz sequence:")
    # Generate the Collatz sequence using a while loop
    while n != 1:
        print(n, end=" → ")  # Print the current value of n
        if n % 2 == 0:  # If n is even
            n = n // 2
        else:  # If n is odd
            n = 3 * n + 1
    print(1)  # Print the final number in the sequence
