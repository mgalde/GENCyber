# GenCyber_1b.py
# Simulates password hashing for a wordlist to show how attackers might crack hashes

import hashlib
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print("=" * 65)
    print("🔍 Simulating Password Cracking with a Wordlist")
    print("-" * 65)
    print("Attackers often use wordlists to guess passwords by hashing each")
    print("word and comparing it to a stolen password hash.")
    print("This demo shows what that process looks like using MD5 hashes.")
    print("=" * 65 + "\n")

def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def main():
    clear_screen()
    show_banner()

    if len(sys.argv) != 2:
        print("Usage: python GenCyber_1b.py wordlist.txt")
        sys.exit(1)

    wordlist_path = sys.argv[1]

    if not os.path.exists(wordlist_path):
        print(f"Error: File '{wordlist_path}' not found.")
        sys.exit(1)

    with open(wordlist_path, 'r') as file:
        passwords = [line.strip() for line in file.readlines() if line.strip()]

    print(f"{'Password':<20} | {'MD5 Hash'}")
    print("-" * 65)

    for pwd in passwords:
        hashed = hash_md5(pwd)
        print(f"{pwd:<20} | {hashed}")

    print("\n🧠 Now imagine a hacker comparing these hashes to a stolen one!")

if __name__ == "__main__":
    main()
