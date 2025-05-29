# GenCyber_1c.py
# Demonstrates salting vs. unsalted hashes to show why salt matters

import hashlib
import os
import random
import string

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("=" * 65)
    print("🧂 Why Add Salt to Password Hashes?")
    print("-" * 65)
    print("Hashing a password alone gives the same result every time.")
    print("But if we add a random *salt*, it scrambles the hash to make it")
    print("much harder for hackers to crack passwords with a wordlist.")
    print("=" * 65 + "\n")

def generate_salt(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    clear_screen()
    show_banner()

    password = input("Enter a password to hash: ")
    print("\n🔓 Unsalted hash:")
    print(f"{password} → {md5_hash(password)}")

    print("\n🧂 Salted hashes (salt + password):")
    for i in range(3):
        salt = generate_salt()
        salted_input = salt + password
        salted_hash = md5_hash(salted_input)
        print(f"{salt} + {password} → {salted_hash}")

    print("\n💡 Notice how the salted hashes are different every time!")
    print("   Even though the password stayed the same.")

if __name__ == "__main__":
    main()
