# Encrypt program
import string
import random

# Variables for Encrypt
chars = " " + string.digits + string.ascii_letters + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key) # now key variable is shuffled.

# Encrypt

plain_message = input("Enter a message to encrypt: ")
cipher_message = ""

for letter in plain_message:
    index = chars.index(letter)
    cipher_message += key[index]

print(f"Encrypt message: {cipher_message}")

# Decrypth

cipher_message = input("enter a message to decrypt: ")
plain_message = ""

for letter in cipher_message:
    index = key.index(letter)
    plain_message += chars[index]

print(f"Decrypted message: {plain_message}")