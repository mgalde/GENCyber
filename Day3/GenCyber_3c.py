import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

PRIVATE_KEY_FILE = "private.pem"
INPUT_FILE = "message.txt"

def decrypt_message(encrypted_b64: str, private_key_file: str) -> str:
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())

    encrypted_bytes = base64.b64decode(encrypted_b64)
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    return decrypted_bytes.decode()

if __name__ == "__main__":
    print("=== GenCyber Message Decryptor ===")

    if not os.path.exists(PRIVATE_KEY_FILE):
        print(f"[!] Missing {PRIVATE_KEY_FILE}.")
        print("[!] Run GenCyber_3a.py or place private.pem in the same folder.")
        exit(1)

    if not os.path.exists(INPUT_FILE):
        print(f"[!] Missing {INPUT_FILE}.")
        print("[!] Make sure message.txt exists and contains an encrypted message.")
        exit(1)

    try:
        with open(INPUT_FILE, "r") as f:
            encrypted_b64 = f.read().strip()

        decrypted_message = decrypt_message(encrypted_b64, PRIVATE_KEY_FILE)
        print("\n[+] Decrypted message:")
        print(decrypted_message)
    except Exception as e:
        print(f"[!] Decryption failed: {e}")
