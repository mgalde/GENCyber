# GenCyber_4b.py
# Sends a UDP broadcast packet disguised as a fake DNS request

import socket
import random
import struct

def create_fake_dns_payload(message: str) -> bytes:
    # Convert message to a fake DNS query by splitting on "."
    # Example: "secret.message.here"
    transaction_id = random.randint(0, 65535)
    flags = 0x0100  # Standard query
    questions = 1
    answer_rrs = 0
    authority_rrs = 0
    additional_rrs = 0

    # Build DNS header
    header = struct.pack("!HHHHHH", transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs)

    # Convert message into DNS QNAME format
    qname = b''.join((bytes([len(part)]) + part.encode() for part in message.split('.'))) + b'\x00'
    qtype = struct.pack("!H", 1)   # Type A
    qclass = struct.pack("!H", 1)  # Class IN

    return header + qname + qtype + qclass

def send_disguised_broadcast(message: str, port: int = 1337):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    try:
        payload = create_fake_dns_payload(message)
        s.sendto(payload, ('<broadcast>', port))
        print(f"[+] Sent disguised message: {message}")
    except Exception as e:
        print(f"[!] Error sending message: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    print("Format your message like a DNS name, e.g., secret.message.here")
    user_input = input("Enter disguised message: ")
    send_disguised_broadcast(user_input)
