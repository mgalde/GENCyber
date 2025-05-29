from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def generate_key_pair():
    print("[*] Generating RSA key pair...")
    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as priv_file:
        priv_file.write(private_key)
    print("[+] Private key saved to private.pem")

    with open("public.pem", "wb") as pub_file:
        pub_file.write(public_key)
    print("[+] Public key saved to public.pem")

if __name__ == "__main__":
    generate_key_pair()
