import string
import random


letters = list(string.ascii_lowercase)
numbers = list(string.digits)
symbols = ['!','@','#','$','%','^','&','*','(',')','-','+']

# print(letters)
# print(numbers)

nr_letters =  int(input("How many letters do you want in password\n"))
nr_numbers =  int(input("How many numbers do you want?\n"))
nr_symbols =  int( input("How many symbols do you want?\n"))

mixed_arr = []
for _ in range(nr_letters):
    mixed_arr.append(random.choice(letters))
for _ in range(nr_numbers):
    mixed_arr.append(random.choice(numbers))
for _ in range(nr_symbols):
    mixed_arr.append(random.choice(symbols))

random.shuffle(mixed_arr)
print(f"Your Password is : {"".join(mixed_arr)} ")
