# Sum of 2 numbers
x = int(input("Enter value for A "))
y = int(input("Enter value for B "))
z = x + y
print(z)
# Printing average
print("Average of x and y =", z/2)
# printing remainder of 2 numbers
print("Modules of X and Y =", x % y)

# Difference between 2 numbers
z = x -y
print(z)

# Multiplication tables for input number
mul = int(input("Enter a number to get their multiplications till 10 "))
for i in range(1, 11):
    print(i, "*", mul, "=", i * mul)

