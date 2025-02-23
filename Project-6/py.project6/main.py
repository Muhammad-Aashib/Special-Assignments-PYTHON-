import random

print("WELCOME TO PASSWORD GENERATOR")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&()_" 

number = input("Input the amount of passwords to generate: ")
number = int(number)

length = input("input the length of Password: ")
length = int(length)

print("\n Here are your Passwords: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)