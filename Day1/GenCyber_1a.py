# GenCyber_1a.py
# Day 1: Hashing Passwords

import hashlib
import os

# Clear the screen (works on Windows, macOS, and Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the banner
def show_banner():
    print("=" * 60)
    print("🔐 Why do we hash passwords?")
    print("-" * 60)
    print("When you create a password, websites don't store it as-is.")
    print("Instead, they turn it into a *hash*, which is like a digital")
    print("fingerprint. That way, even if hackers break in, they can't")
    print("see your real password — just the hash!")
    print("=" * 60 + "\n")

def main():
    clear_screen()
    show_banner()

    # Ask the user to type in a password
    password = input("Please enter your secret password: ")

    # Convert the password to bytes
    password_bytes = password.encode()

    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the password bytes
    md5_hash.update(password_bytes)

    # Get the hexadecimal digest (the hash)
    hashed_password = md5_hash.hexdigest()

    # Show the user the hashed result
    print("\nHere is your password's MD5 hash:")
    print(hashed_password)

    print("\n⚠️ Remember: Hashes are one-way. You can't easily turn them back into the original password!")

if __name__ == "__main__":
    main()
