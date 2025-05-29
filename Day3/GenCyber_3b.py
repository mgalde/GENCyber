import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

PUBLIC_KEY_FILE = "public.pem"
OUTPUT_FILE = "message.txt"

def encrypt_message(message: str, public_key_file: str) -> str:
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)
    encrypted_bytes = cipher.encrypt(message.encode())
    encrypted_b64 = base64.b64encode(encrypted_bytes).decode()

    return encrypted_b64

if __name__ == "__main__":
    print("=== GenCyber Message Encryptor ===")

    if not os.path.exists(PUBLIC_KEY_FILE):
        print(f"[!] Missing {PUBLIC_KEY_FILE}.")
        print("[!] Run GenCyber_3a.py or place public.pem in the same folder.")
        exit(1)

    message = input("Enter the message you want to encrypt: ")

    try:
        encrypted_message = encrypt_message(message, PUBLIC_KEY_FILE)
        print("\n[+] Encrypted message (Base64):")
        print(encrypted_message)

        with open(OUTPUT_FILE, "w") as f:
            f.write(encrypted_message)

        print(f"[+] Message saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"[!] Encryption failed: {e}")
