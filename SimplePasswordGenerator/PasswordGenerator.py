
# Simple password generator
import random

# User inputs
length = int(input("How long would you like your password to be: "))
print("Please enter yes or no for the following options")
upper = input("Do you want uppercase letters in your password: ")
lower = input("Do you want lowercase letters in your password: ")
numbers = input("Do you want numbers in your password: ")
characters = input("Do you want special characters in your password: ")


# character sets
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
specialCharacters = "~`!@#$%^&*()_-+={[]}|\\\"':;<,>.?/"
Numbers = "1234567890"


# determining user selections for password composition
selection = []
if upper[0] == "y":
    selection.append(1)
if lower[0] == "y":
    selection.append(2)
if characters[0] == "y":
    selection.append(3)
if numbers[0] == "y":
    selection.append(4)

password = ""

# generator loop
for i in range(length):
    length = len(selection)
    characterType = random.randint(0,length-1)
    if selection[characterType] == 1:
        randomValue = random.randint(0,25)
        password += upperCase[randomValue]
    elif selection[characterType] == 2:
        randomValue = random.randint(0,25)
        password += lowerCase[randomValue]
    elif selection[characterType] == 3:
        randomValue = random.randint(0,31)
        password += specialCharacters[randomValue]
    elif selection[characterType] == 4:
        randomValue = random.randint(0,9)
        password += Numbers[randomValue]

# prints password to user
print(password)

