def is_happy_number(num):
    seen_numbers = set()

    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = sum(int(digit)**2 for digit in str(num))

    return num == 1

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a happy number
if is_happy_number(num):
    print(f"{num} is a Happy Number.")
else:
    print(f"{num} is not a Happy Number.")
