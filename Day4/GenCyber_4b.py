# GenCyber_4b.py
# Sends a UDP broadcast message with Base64 encoding

import socket
import base64

def send_encoded_broadcast(message: str, port: int = 1337):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        encoded = base64.b64encode(message.encode())
        s.sendto(encoded, ('<broadcast>', port))
        print(f"[+] Sent encoded message: {encoded.decode()}")
    except Exception as e:
        print(f"[!] Error sending message: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    user_message = input("Enter your secret agent message: ")
    send_encoded_broadcast(user_message)
