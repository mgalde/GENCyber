import os
import base64
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

PUBLIC_KEY_FILE = "public.pem"
INPUT_FILE = "signed_message.txt"

def verify_signature(message: str, signature_b64: str, public_key_file: str) -> bool:
    with open(public_key_file, "rb") as f:
        public_key = RSA.import_key(f.read())

    hash_obj = SHA256.new(message.encode())
    signature = base64.b64decode(signature_b64)

    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False

if __name__ == "__main__":
    print("=== GenCyber Signature Verifier ===")

    if not os.path.exists(PUBLIC_KEY_FILE):
        print(f"[!] Missing {PUBLIC_KEY_FILE}.")
        print("[!] Run GenCyber_3a.py or place public.pem in the same folder.")
        exit(1)

    if not os.path.exists(INPUT_FILE):
        print(f"[!] Missing {INPUT_FILE}.")
        print("[!] Make sure signed_message.txt exists.")
        exit(1)

    try:
        with open(INPUT_FILE, "r") as f:
            lines = f.read().split("===SIGNATURE===\n")
            if len(lines) != 2:
                raise ValueError("Invalid signed message format.")
            message = lines[0].strip()
            signature_b64 = lines[1].strip()

        if verify_signature(message, signature_b64, PUBLIC_KEY_FILE):
            print("[+] Signature is VALID. The message is authentic.")
            print(f"[+] Message: {message}")
        else:
            print("[!] Signature is INVALID. The message may have been forged.")
    except Exception as e:
        print(f"[!] Verification failed: {e}")
