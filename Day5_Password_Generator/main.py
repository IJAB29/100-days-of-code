#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# totalLen = nr_numbers + nr_symbols + nr_letters
# password = ""
# numbersCount = 0
# lettersCount = 0
# symbolsCount = 0
# while len(password) != totalLen:
#     randomList = random.randint(1, 4)
#     if randomList == 1 and numbersCount < nr_numbers:
#         password += random.choice(numbers)
#         numbersCount += 1
#     elif randomList == 2 and symbolsCount < nr_symbols:
#         password += random.choice(symbols)
#         symbolsCount += 1
#     elif randomList == 3 and lettersCount < nr_letters:
#         password += random.choice(letters)
#         lettersCount += 1

#Class Answer
password_list = []
password = ""
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)
random.shuffle(password_list)
password = password.join(password_list)

print(password)