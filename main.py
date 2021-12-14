import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789~`!£$%°^&*()-_+={}[]|\/:;<>.?"

while 1:
    password_length = int(input("What length would you like your password to be: "))
    password_count = int(input("How many password would you like to be generated: "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_length):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your Generated Passoword: ", password)



