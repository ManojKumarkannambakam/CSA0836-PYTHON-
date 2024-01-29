vowels = "AEIOUaeiou"
consonants_count = 0
vowels_count = 0

given_statement = input("Enter a statement: ")

for char in given_statement:
    if char.isalpha():
        if char.lower() in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

# Determine which count is maximum
if vowels_count > consonants_count:
    print(f"Number of vowels = {vowels_count} (Maximum)")
    print(f"Number of consonants = {consonants_count}")
elif consonants_count > vowels_count:
    print(f"Number of vowels = {vowels_count}")
    print(f"Number of consonants = {consonants_count} (Maximum)")
else:
    print(f"Number of vowels = {vowels_count}")
    print(f"Number of consonants = {consonants_count}")
