import random
import string

def password_generator():
    print("Welcome to the the Password Generator!")

    # Ask user for password length
    length = int(input("Enter the desired password length: "))

    # Characters to use
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    print("Generated Passowrd:", password)

    password_generator()
