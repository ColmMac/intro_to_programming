import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for _  in range(length))
    return password


length = int(input("Enter desired password length: "))
print(f"Your generated password is {generate_password(length)}")

