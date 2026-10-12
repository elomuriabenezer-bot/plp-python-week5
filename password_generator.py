import random
import string


def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password


password_one = make_password()
password_two = make_password(12)

print("Password:", password_one)
print("Length:", len(password_one))
print("Password:", password_two)
print("Length:", len(password_two))

