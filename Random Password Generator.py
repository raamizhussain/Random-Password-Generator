import random

letters = ['a','b','c','d','e','f','g','h','i','j']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','#','$','%']

numofletters = int(input("No. of letters: "))
numofnumbers = int(input("No. of numbers: "))
numofsymbols = int(input("No. of symbols: "))

password = ""
passwordlist = []
for letter in range(1,numofletters + 1):
    passwordlist += random.choice(letters)
for number in range(1,numofnumbers + 1):
    passwordlist += random.choice(numbers)
for symbol in range(1 , numofsymbols + 1):
    passwordlist += random.choice(symbols)

random.shuffle(passwordlist)

for numberrr in passwordlist:
    password += numberrr

print(password)

