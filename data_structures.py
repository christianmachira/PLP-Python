# Get user input for the list of integers
input_numbers = input("Enter a list of integers separated by spaces: ")
# Convert the input string into a list of integers
try:
        numbers = [int(num) for num in input_numbers.split()]
except ValueError:
    print("Invalid input. Please enter valid integers separated by spaces.")
# Calculate the sum of the integers
total_sum = sum(numbers)
# Display the result
print("List of integers:", numbers)
print("Sum of integers:", total_sum)


