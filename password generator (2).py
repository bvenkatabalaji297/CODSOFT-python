import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices to generate a password of the specified length
    password = ''.join(random.choices(characters, k=length))

    return password

# Prompt the user for the desired password length
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            print("Password length must be greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Generate and display the password
password = generate_password(password_length)
print("Generated Password:", password)
