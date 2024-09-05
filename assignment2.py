#function to take input for list
def get_integer_list():
    # Ask the user how many numbers they want to input
    num_values = int(input("How many values do you want to enter? "))
    
    values = []
    for i in range(num_values):
        while True:
            try:
                
                value = int(input(f"Enter integer {i + 1}: "))
                values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    return values
#function to compute the sum, avg & minimum values
def compute_statistics(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    minimum = min(numbers)
    
    return total_sum, average, minimum

numbers = get_integer_list()
total_sum, average, minimum = compute_statistics(numbers)

print(f"\nYou entered: {numbers}")
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Minimum: {minimum}")
