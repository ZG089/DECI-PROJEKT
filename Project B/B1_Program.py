import random
import string
import time
import os
os.system('cls')
print("Welcome To PassGen Tool !")
time.sleep(2)
print("")
print("Preparing Your Password......")
time.sleep(2)
print("")


def generate_password():
    length = 8
    what_to_be_in_the_password = string.ascii_letters + string.digits
    password = []
    for i in range(length):
        password.append(random.choice(what_to_be_in_the_password))
    password = ''.join(password)
    return password


'''
# Do not change the code below
'''
# Generate a password that meets the criteria
password = generate_password()
print(password)
