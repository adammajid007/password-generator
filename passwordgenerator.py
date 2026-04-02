# Generates a random password.

import random

randomCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnpqrstuvwxyzZ1234567898"
symbols = "@/#!"

try:
    passwordLength = int(input("Password length: "))
    symbolsQuestion = input("Would you like to add symbols to the password? (y/n):  ").lower()

    characters = randomCharacters

    if symbolsQuestion == "y":
        characters += symbols

        randomPassword = ""

        for i in range(passwordLength):
            randomPassword += random.choice(characters)

        print(randomPassword)

    if symbolsQuestion == "n":
        randomPassword = ""

        for i in range(passwordLength):
            randomPassword += random.choice(characters)

        print(randomPassword)

except ValueError:
    print("Invalid input. Please try again.")
