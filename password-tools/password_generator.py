import random
import string

def generate_password(length=16, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choices(characters, k=length))
    return password

print("=== Secure Password Generator ===\n")
length = int(input("Password length (default 16): ") or 16)
symbols = input("Include symbols? (y/n): ").lower() == 'y'

for i in range(5):
    print(f"Option {i+1}: {generate_password(length, symbols)}")
