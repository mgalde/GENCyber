# GenCyber_1d.py
# Given a salt and a wordlist, generate salted MD5 hashes to help crack login hashes

import hashlib
import sys
import os

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    print("🧂 Salted Hash Generator (GenCyber_1d)")
    print("--------------------------------------")

    salt = input("Enter the salt (e.g., a username): ").strip()

    try:
        with open("wordlist.txt", "r") as file:
            words = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("⚠️ Error: wordlist.txt not found.")
        sys.exit(1)

    print(f"\nUsing salt: '{salt}'\n")
    print(f"{'Password':<20} | {'Salt + Password Hash'}")
    print("-" * 65)

    for word in words:
        combined = salt + word
        hashed = md5_hash(combined)
        print(f"{word:<20} | {hashed}")

    print("\n🧠 Use this output to find which password matches a given salted hash!")

if __name__ == "__main__":
    main()
