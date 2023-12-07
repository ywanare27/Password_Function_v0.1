import random
import string


def random_password(letters, numbers):
    special = "!@#$%^&*"

    password1 = random.choices(
        string.ascii_lowercase+string.ascii_uppercase, k=letters-4)
    password2 = random.choices(special+string.digits, k=4)
    return "".join(password2+password1)


length = 0
numbers = 2

while length < 8:
    try:
        length = int(
            input("How many character should that password be (min 8 character): "))
    except ValueError as err:
        print("------>   Please input numbers only! ")

print(random_password(length, numbers))
