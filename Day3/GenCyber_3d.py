import os
import base64
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

PRIVATE_KEY_FILE = "private.pem"
OUTPUT_FILE = "signed_message.txt"

def sign_message(message: str, private_key_file: str) -> str:
    with open(private_key_file, "rb") as f:
        private_key = RSA.import_key(f.read())

    hash_obj = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    return base64.b64encode(signature).decode()

if __name__ == "__main__":
    print("=== GenCyber Message Signer ===")

    if not os.path.exists(PRIVATE_KEY_FILE):
        print(f"[!] Missing {PRIVATE_KEY_FILE}.")
        print("[!] Run GenCyber_3a.py or place private.pem in the same folder.")
        exit(1)

    message = input("Enter the message to sign: ")

    try:
        signature_b64 = sign_message(message, PRIVATE_KEY_FILE)

        with open(OUTPUT_FILE, "w") as f:
            f.write(message + "\n")
            f.write("===SIGNATURE===\n")
            f.write(signature_b64)

        print(f"[+] Message and signature saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"[!] Signing failed: {e}")
