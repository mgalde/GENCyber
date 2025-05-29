# GenCyber_4a.py
# Sends a UDP broadcast message in plaintext

import socket

def send_broadcast_message(message: str, port: int = 1337):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        s.sendto(message.encode(), ('<broadcast>', port))
        print(f"[+] Sent message: {message}")
    except Exception as e:
        print(f"[!] Error sending message: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    user_message = input("Enter your secret agent message: ")
    send_broadcast_message(user_message)
