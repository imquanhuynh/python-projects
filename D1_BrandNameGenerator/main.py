import random
import string
from string import punctuation

print("Welcome to the Brand Name Generator!")
while True:
    grow_up = input("Which city did you grow up in? ").strip()
    if grow_up:
        break;
while True:
    pet_name = input("What is your pet's name (or something you like)? ").strip()
    if pet_name:
        break;
grow_up = grow_up.title()
pet_name = pet_name.title()
punctuation = random.choice([" ","-","_"])
if random.choice([True,False]):
    brand_name =grow_up + punctuation + pet_name
else:
    brand_name = pet_name + punctuation + grow_up
print(brand_name)

