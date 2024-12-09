# Input from the user
original_string = input("Enter a string: ").lower()  # Convert to lowercase for case-insensitive comparison

# Initialize variables
reversed_string = ""
index = len(original_string) - 1

# Reverse the string using a while loop
while index >= 0:
    reversed_string += original_string[index]
    index -= 1

# Check if the original string is equal to the reversed string
if original_string == reversed_string:
    print(f'"{original_string}" is a palindrome.')
else:
    print(f'"{original_string}" is not a palindrome.')
