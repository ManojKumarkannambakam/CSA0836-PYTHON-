# User input for two strings
S1 = input("Enter the first string: ")
S2 = input("Enter the second string: ")

# Initialize a counter for matches
match_count = 0

# Check if the lengths of both strings are the same
if len(S1) == len(S2):
    # Iterate through each index of the strings
    for i in range(len(S1)):
        # Check if characters at the same index match
        if S1[i] == S2[i]:
            match_count += 1

# Display the number of matches
print("Number of matches:", match_count)
