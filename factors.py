# Function to find the factors of a number
def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# Function to print the first N factors of a number
def print_first_n_factors(number, N):
    factors = find_factors(number)
    
    # Print the number of factors
    print(f"Number of factors = {len(factors)}")
    
    # Print the first N factors
    print(f"1st {N} factors are: {', '.join(map(str, factors[:N]))}")

# Sample Input
num = 100
N = 4

# Call the function to print factors
print_first_n_factors(num, N)

  
