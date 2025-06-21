import random
import string

def generate_password(length=20):
    # Define the characters to be used in the password (letters, digits, and punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters to form a password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Generate and print 20 strong passwords
for _ in range(20):
    print(generate_password())
