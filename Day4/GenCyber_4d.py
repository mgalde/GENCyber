# GenCyber_4d.py
# Sends a UDP broadcast message that mimics an HTTP GET request

import socket

def create_http_like_payload(message: str) -> bytes:
    http_request = (
        f"GET /search?q={message.replace(' ', '+')} HTTP/1.1\r\n"
        f"Host: www.fake-search.com\r\n"
        f"User-Agent: SecretAgent/1.0\r\n"
        f"Accept: */*\r\n"
        f"\r\n"
    )
    return http_request.encode()

def send_http_disguised_broadcast(message: str, port: int = 80):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        payload = create_http_like_payload(message)
        s.sendto(payload, ('<broadcast>', port))
        print(f"[+] Sent disguised HTTP message: {message}")
    except Exception as e:
        print(f"[!] Error sending message: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    user_input = input("Enter your secret search message: ")
    send_http_disguised_broadcast(user_input)
