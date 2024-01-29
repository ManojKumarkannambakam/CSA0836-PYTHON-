special_characters = set("!@#$%^&*()_-+={}[]|\:;'<>?,./\"")
count = 0

given_statement = input("Enter a statement: ")

for char in given_statement:
    if char in special_characters:
        count += 1

print("Number of special characters:", count)
